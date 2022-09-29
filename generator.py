"""
    @Author: Shay Lin & WhiteDemon
    @Date: 2022/9/23
    @Copyright: Shay Lin & WhiteDemon
    @Description:
"""
from stack import Stack, Operator
import random

hashTable = []


def OprGenerator():
    # 随机确定一共有几个运算符，运算符个数范围[1,3]
    oprNum = random.randint(1, 3)
    # 生成本题的运算符列表
    oprList = []
    lPri = 0
    hPri = 0
    for i in range(oprNum):
        randOpr = random.randint(1, 4)
        opr = Operator()
        if randOpr == 1:
            opr.opr = "+"
        elif randOpr == 2:
            opr.opr = "-"
        elif randOpr == 3:
            opr.opr = "×"
        else:
            opr.opr = "÷"
        if 1 <= randOpr <= 2:
            opr.pri = 1
            lPri = lPri + 1
        else:
            opr.pri = 2
            hPri = hPri + 1
        oprList.append(opr)
    brackets = random.randint(0, 1)  # 随机决定是否生成括号
    return oprNum, oprList, brackets


def GCD(a, b):  # 求最大公约数
    while a != 0:
        a, b = b % a, a
    return b


def NumGenerator(oprNum, r):
    # 生成本题的操作数列表
    numList = []
    for i in range(oprNum + 1):
        # 本程序中设定每个参与运算的数字为分数的概率为20%
        isFraction = random.randint(1, 100)
        if 80 <= isFraction <= 100:
            num = ""
            denominator = random.randrange(2, r)  # 生成分母
            # 分子生成前先设定为和分母互质的数
            numerator = random.randrange(1, denominator)
            while GCD(denominator, numerator) != 1:  # 如果分母和分子不互质则重新生成分子
                numerator = random.randrange(1, denominator)
            num = num + str(numerator) + "/" + str(denominator)
            numList.append(num)
        else:
            num = random.randrange(0, r)
            numList.append(num)
    return numList


def ExGenerator(n, r):  # 生成题目
    f = open("./exercises.txt", "w", encoding="UTF-8")
    count = 0
    while count < n:
        exer = []  # 题目
        RPN = []  # 逆波兰式
        oprNum, oprList, brackets = OprGenerator()
        numList = NumGenerator(oprNum, r)
        oprIndex = 0
        numIndex = 0
        # 生成括号
        if brackets != 0:
            lBF = False
            rBF = False
            while numIndex <= oprNum:
                if lBF is False:  # 如果还没有左括号
                    flag1 = random.randint(1, 10)
                    # 70%几率生成左括号
                    if 3 < flag1 <= 10:
                        exer.append("(")
                        lBF = True
                exer.append(numList[numIndex])
                numIndex = numIndex + 1
                if lBF is True and rBF is False and exer.index("(") != exer.index(numList[numIndex - 1]) - 1:  # 如果还未生成右括号，且左括号不是刚生成的
                    flag2 = random.randint(1, 10)
                    # 70%几率生成右括号
                    if 3 < flag2 <= 10:
                        exer.append(")")
                        rBF = True
                if oprIndex == oprNum and lBF is True and rBF is False:  # 如果表达式结尾还没生成右括号则生成右括号
                    exer.append(")")
                    rBF = True
                if oprIndex < oprNum:  # 插入运算符
                    exer.append(oprList[oprIndex])
                    oprIndex = oprIndex + 1
        else:  # 没有括号的情况
            while numIndex <= oprNum:
                # 按顺序访问运算符列表和操作数列表并按中缀表达式顺序生成题目
                exer.append(numList[numIndex])
                numIndex = numIndex + 1
                if oprIndex < oprNum:
                    exer.append(oprList[oprIndex])
                    oprIndex = oprIndex + 1
        RPN = RPNBuild(exer)
        if CalcCheck(RPN) is True:  # 如果检查出存在负数运算过程则重新生成
            continue
        if HashCheck(RPN) is True:  # 如果检查出重复则重新生成
            continue
        # 生成答案
        ansStatus = AnsGenerator(RPN, count)
        if ansStatus is False:  # 如果生成答案过程中发现题目有问题则重新生成题目
            continue
        # 将列表中存储的题目转为字符串
        output = ""
        for item in exer:
            if type(item) is str or type(item) is int:
                output = output + str(item) + " "
            else:
                output = output + item.opr + " "
        output = output + "="
        f.write(f"{count + 1}. {output}\n")
        count = count + 1
    f.close()


def CalcCheck(rpn):  # 运算过程检查,筛出含有负数运算过程的题目
    s = Stack()  # 使用栈辅助RPN计算
    for item in rpn:
        if type(item) is Operator:  # 如果当前元素是操作符
            n2 = s.pop()  # RPN栈顶的是操作数
            n1 = s.pop()  # 第二个栈顶元素是被操作数
            # 如果是分数则进行字符串->数字的转换
            if type(n1) is str:
                div1 = n1.find("/")
                nume1 = int(n1[0:div1])
                deno1 = int(n1[div1 + 1:])
                n1 = nume1 / deno1
            if type(n2) is str:
                div2 = n2.find("/")
                nume2 = int(n2[0:div2])
                deno2 = int(n2[div2 + 1:])
                n2 = nume2 / deno2
            # 根据操作符对两数进行计算
            if item.opr == "+":
                n = n1 + n2
            elif item.opr == "-":
                n = n1 - n2
            elif item.opr == "×":
                n = n1 * n2
            else:
                if n2 == 0:
                    return True
                n = n1 / n2
            if n < 0:
                return True
            # 将计算完的被操作数重新压入栈中
            s.push(n)
        else:  # 如果当前元素为数字，则压入栈
            s.push(item)
    return False


def HashCheck(rpn):  # 对生成的题目进行哈希并检查是否重复
    P = 131
    hash = 0
    global hashTable
    for i in range(len(rpn)):  # 计算当前逆波兰式的哈希值
        if type(rpn[i]) == Operator:
            hash = hash + ord(rpn[i].opr) * (P ** i)
        else:
            tmp = str(rpn[i])
            for j in range(len(tmp)):
                hash = hash + ord(tmp[j]) * (P ** i)
    for i in range(len(hashTable)):  # 在哈希表中查询是否有相同值
        if hash == hashTable[i]:
            return True
    hashTable.append(hash)  # 将哈希值插入哈希表
    return False


def AnsGenerator(rpn, id):  # 生成答案
    f = open("./answers.txt", "a", encoding="UTF-8")
    s = Stack()  # 使用栈辅助RPN计算
    for item in rpn:
        if type(item) is Operator:  # 如果当前元素是操作符
            n2 = s.pop()  # RPN栈顶的是操作数
            n1 = s.pop()  # 第二个栈顶元素是被操作数
            # 根据操作符对两数进行计算
            if type(n1) == type(n2) and type(n1) is int:  # 如果均为整数
                if item.opr == "+":
                    n = n1 + n2
                elif item.opr == "-":
                    n = n1 - n2
                elif item.opr == "×":
                    n = n1 * n2
                else:
                    n = str(n1) + "/" + str(n2)
            else:
                # 如果存在分数则将操作数全转化为分数形式
                if type(n1) is str:
                    div1 = n1.find("/")
                    nume1 = int(n1[0:div1])
                    deno1 = int(n1[div1 + 1:])
                else:
                    nume1 = n1
                    deno1 = 1
                if type(n2) is str:
                    div2 = n2.find('/')
                    nume2 = int(n2[0:div2])
                    deno2 = int(n2[div2 + 1:])
                else:
                    nume2 = n2
                    deno2 = 1
                # 以分数形式进行计算
                if item.opr == "+":
                    if deno1 == deno2:
                        n = str(nume1 + nume2) + "/" + str(deno1)
                    else:
                        gcd = GCD(deno1, deno2)
                        deno = int(deno1 * deno2 / gcd)  # 通分计算后强制类型转化为整型，防止后续出现字符串中的浮点数（如“8.0”）无法转化为整型的情况
                        nume = int(nume1 * deno2 / gcd + nume2 * deno1 / gcd)
                        n = str(nume) + "/" + str(deno)
                elif item.opr == "-":
                    if deno1 == deno2:
                        n = str(nume1 - nume2) + "/" + str(deno1)
                    else:
                        gcd = GCD(deno1, deno2)
                        deno = int(deno1 * deno2 / gcd)
                        nume = int(nume1 * deno2 / gcd - nume2 * deno1 / gcd)
                        n = str(nume) + "/" + str(deno)
                # 乘除计算不进行约分，后续统一约分，节省运算量
                elif item.opr == "×":
                    deno = deno1 * deno2
                    nume = nume1 * nume2
                    n = str(nume) + "/" + str(deno)
                else:
                    deno = deno1 * nume2
                    nume = nume1 * deno2
                    n = str(nume) + "/" + str(deno)
            # 将计算完的被操作数重新压入栈中
            s.push(n)
        else:  # 如果当前元素为数字，则压入栈
            s.push(item)
    ans = s.pop()  # 最后入栈的一定是结果
    if type(ans) is str:  # 如果结果是分数
        div = ans.find("/")
        nume = int(ans[0:div])
        deno = int(ans[div + 1:])
        if deno <= 0 or nume < 0:  # 如果运算结果的分母为0或分子分母其中之一出现负数，说明题目有瑕疵，重新生成题目
            return False
        if nume == deno:  # 分子等于分母
            ans = 1
            f.write(f"{id + 1}. {ans}\n")
            return True
        elif nume == 0:  # 分子等于0
            ans = 0
            f.write(f"{id + 1}. {ans}\n")
            return True
        # 剩余情况为真分数或假分数
        plus = None
        if nume > deno:  # 如果是带分数
            plus = int(nume / deno)
            nume = nume - plus * deno  # 分子减去整数部分
        if nume == 0:  # 如果正好是整数
            ans = plus
            f.write(f"{id + 1}. {ans}\n")
            return True
        gcd = GCD(nume, deno)
        if gcd != 1:  # 对分子分母进行约分
            nume = int(nume / gcd)
            deno = int(deno / gcd)
        else:
            pass
        if plus:  # 构建带分数形式的输出
            ans = str(plus) + "'" + str(nume) + "/" + str(deno)
        else:  # 构建常规分数形式的输出
            ans = str(nume) + "/" + str(deno)
    f.write(f"{id + 1}. {ans}\n")
    return True


def RPNBuild(e):
    rpn = []
    s1 = Stack()
    s2 = Stack()
    s1.push(Operator())
    s1.data[0].opr = '#'
    s1.data[0].pri = -1
    s1.top = 1
    for item in e:
        if item == '(':  # 如果是左括号
            s1.push(item)
        elif (type(item) is str and len(item) >= 3) or type(item) is int:  # 如果是数值
            s2.push(item)
        elif item != ')':  # 如果是操作符
            ele = s1.data[s1.top - 1]  # 取s1栈顶元素
            if ele == '(':  # 如果栈顶元素为左括号
                s1.push(item)
            else:  # 如果栈顶元素不为左括号
                if ele.pri < item.pri:  # 栈顶元素的优先级比当前元素的优先级低
                    s1.push(item)  # 往s1中压入当前元素
                else:  # 栈顶元素优先级比当前元素优先级高或同级
                    if ele.opr == "+" or ele.opr == "×":  # 如果栈顶元素的操作符是+、×，对两个操作数进行交换，使得小的在前
                        n2 = s2.pop()  # 先pop出来的是第二操作数
                        n1 = s2.pop()
                        value1 = None
                        value2 = None
                        div1 = None
                        div2 = None
                        if type(n1) is str:
                            div1 = n1.find("/")
                            value1 = int(n1[0:div1]) / int(n1[div1 + 1:])
                        elif type(n1) is int:
                            value1 = n1
                        if type(n2) is str:
                            div2 = n2.find("/")
                            value2 = int(n2[0:div2]) / int(n2[div2 + 1:])
                        elif type(n2) is int:
                            value2 = n2
                        if value1 and value2:
                            if value1 > value2:
                                s2.push(n2)
                                s2.push(n1)
                            else:
                                s2.push(n1)
                                s2.push(n2)
                        else:
                            s2.push(n1)
                            s2.push(n2)
                    s2.push(s1.pop())  # 把s1栈顶元素弹出并压入s2
                    s1.push(item)  # 把待插入元素压入s1
        else:  # 如果是右括号
            while s1.data[s1.top - 1] != '(':  # 把左括号上方的所有元素弹出并按顺序压入s2
                ele = s1.data[s1.top - 1]  # 取s1栈顶元素
                if ele.opr == "+" or ele.opr == "×":  # 如果栈顶元素的操作符是+、×，对两个操作数进行交换，使得小的在前
                    n2 = s2.pop()  # 先pop出来的是第二操作数
                    n1 = s2.pop()
                    value1 = None
                    value2 = None
                    div1 = None
                    div2 = None
                    if type(n1) is str:
                        div1 = n1.find("/")
                        value1 = int(n1[0:div1]) / int(n1[div1 + 1:])
                    elif type(n1) is int:
                        value1 = n1
                    if type(n2) is str:
                        div2 = n2.find("/")
                        value2 = int(n2[0:div2]) / int(n2[div2 + 1:])
                    elif type(n2) is int:
                        value2 = n2
                    if value1 and value2:
                        if value1 > value2:
                            s2.push(n2)
                            s2.push(n1)
                        else:
                            s2.push(n1)
                            s2.push(n2)
                    else:
                        s2.push(n1)
                        s2.push(n2)
                s2.push(s1.pop())  # 把s1栈顶元素弹出并压入s2
            s1.pop()
    if s1.top == 1:  # 如果s1中不存在操作符
        pass
    else:
        while s1.top != 1:  # 把s1的所有元素弹出并按顺序压入s2
            ele = s1.data[s1.top - 1]  # 取s1栈顶元素
            if ele.opr == "+" or ele.opr == "×":  # 如果栈顶元素的操作符是+、×，对两个操作数进行交换，使得小的在前
                n2 = s2.pop()  # 先pop出来的是第二操作数
                n1 = s2.pop()
                value1 = None
                value2 = None
                div1 = None
                div2 = None
                if type(n1) is str:  # 分数转换成数字
                    div1 = n1.find("/")
                    value1 = int(n1[0:div1]) / int(n1[div1 + 1:])
                elif type(n1) is int:
                    value1 = n1
                if type(n2) is str:
                    div2 = n2.find("/")
                    value2 = int(n2[0:div2]) / int(n2[div2 + 1:])
                elif type(n2) is int:
                    value2 = n2
                # 将pop出来的两个操作数压回s2中
                if value1 and value2:
                    if value1 > value2:
                        s2.push(n2)
                        s2.push(n1)
                    else:
                        s2.push(n1)
                        s2.push(n2)
                else:  # 如果n1或n2之一是运算符则压回
                    s2.push(n1)
                    s2.push(n2)
            s2.push(s1.pop())
        s1.pop()
    rpnStack = Stack()
    while not s2.IsEmpty():  # s2栈底到栈顶的顺序为RPN，为了方便插入列表中，进行顺序转换
        rpnStack.push(s2.pop())
    while not rpnStack.IsEmpty():  # 将转化好的栈进一步转化为RPN列表
        rpn.append(rpnStack.pop())
    return rpn


if __name__ == "__main__":
    f = open("./answers.txt", 'w', encoding="UTF-8")
    f.close()
    ExGenerator(500, 5)
