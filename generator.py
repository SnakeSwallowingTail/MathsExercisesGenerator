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
    brackets = random.randint(0, 1)
    return oprNum, oprList, brackets


def gcd(a, b):  # 求最大公约数
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
            while gcd(denominator, numerator) != 1:  # 如果分母和分子不互质则重新生成分子
                numerator = random.randrange(1, denominator)
            num = num + str(numerator) + "/" + str(denominator)
            numList.append(num)
        else:
            num = random.randrange(0, r)
            numList.append(num)
    return numList


def ExGenerator(n, r):  # 生成题目
    f = open("./exercises.txt", "w+", encoding="UTF-8")
    for count in range(n):
        exer = []  # 题目
        RPN = []  # 逆波兰式
        oprNum, oprList, brackets = OprGenerator()
        numList = NumGenerator(oprNum, r)
        oprIndex = 0
        numIndex = 0
        if brackets != 0:
            lBF = False
            rBF = False
            while numIndex <= oprNum:
                if lBF is False:
                    flag1 = random.randint(1, 10)
                    if 3 < flag1 <= 10:
                        exer.append("(")
                        lBF = True
                exer.append(numList[numIndex])
                numIndex = numIndex + 1
                if lBF is True and rBF is False and exer.index("(") != exer.index(numList[numIndex - 1]) - 1:
                    flag2 = random.randint(1, 10)
                    if 3 < flag2 <= 10:
                        exer.append(")")
                        rBF = True
                if oprIndex == oprNum and lBF is True and rBF is False:
                    exer.append(")")
                    rBF = True
                if oprIndex < oprNum:
                    exer.append(oprList[oprIndex])
                    oprIndex = oprIndex + 1
        else:
            while numIndex <= oprNum:
                exer.append(numList[numIndex])
                numIndex = numIndex + 1
                if oprIndex < oprNum:
                    exer.append(oprList[oprIndex])
                    oprIndex = oprIndex + 1
        if CalcCheck(RPN):  # 如果检查出存在负数运算过程则重新生成
            count = count - 1
            continue
        if HashCheck(exer):  # 如果检查出重复则重新生成
            count = count - 1
            continue
        for item in exer:
            if type(item) is str or type(item) is int:
                print(item, end=" ")
            else:
                print(item.opr, end=" ")
        RPN = RPNBuild(exer)
        print()
        for item in RPN:
            if type(item) is str or type(item) is int:
                print(item, end=" ")
            else:
                print(item.opr, end=" ")
        print()
        output = ""
        for item in exer:
            if type(item) is str or type(item) is int:
                output = output + str(item) + " "
            else:
                output = output + item.opr + " "
        output = output + "="
        """
        AnsGenerator(exer, count)
        # exer = exer + "="
        
        for item in exer:
            if type(item) is str or type(item) is int:
                print(item, end=" ")
            else:
                print(item.opr, end=" ")
        print()
        """

        f.write(f"{count}. {output}\n")
    f.close()


def CalcCheck(rpn):  # 运算过程检查,筛出含有负数运算过程的题目
    s = Stack()  # 使用栈辅助RPN计算
    for i in range(len(rpn)):
        if type(rpn[i]) is Operator:  # 如果当前元素是操作符
            n2 = s.pop()  # RPN栈顶的是操作数
            n1 = s.pop()  # 第二个栈顶元素是被操作数
            # 如果是分数则进行字符串->数字的转换
            if type(n1) is str:
                n1 = float(int(n1[0]) / int(n1[2]))
            if type(n2) is str:
                n2 = float(int(n2[0]) / int(n2[2]))
            # 根据操作符对两数进行计算
            if rpn[i].opr == "+":
                n = n1 + n2
            elif rpn[i].opr == "-":
                n = n1 - n2
            elif rpn[i].opr == "×":
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
            s.push(rpn[i])
    return False


def HashCheck(rpn):  # 对生成的题目进行哈希并检查是否重复
    P = 131
    hash = 0
    global hashTable
    for i in range(len(rpn)):
        if type(rpn[i]) == int:
            hash = hash + ord(str(rpn[i])) * (P ** i)
        elif type(rpn[i]) == Operator:
            hash = hash + ord(rpn[i].opr) * (P ** i)
        else:
            for j in range(len(rpn[i])):
                hash = hash + ord(rpn[i][j]) * (P ** i)
    for i in range(len(hashTable)):
        if hash == hashTable[i]:
            return True
    hashTable.append(hash)
    return False


def AnsGenerator(rpn, n):  # 生成答案
    f = open("./answers.txt", "w+", encoding="UTF-8")
    f.close()
    pass


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
        elif (type(item) is str and len(item) == 3) or type(item) is int:  # 如果是数值
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
                        if type(n1) is str:
                            value1 = int(n1[0]) / int(n1[2])
                        elif type(n1) is int:
                            value1 = n1
                        if type(n2) is str:
                            value2 = int(n2[0]) / int(n2[2])
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
                    if type(n1) is str:
                        value1 = int(n1[0]) / int(n1[2])
                    elif type(n1) is int:
                        value1 = n1
                    if type(n2) is str:
                        value2 = int(n2[0]) / int(n2[2])
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
                if type(n1) is str:
                    value1 = int(n1[0]) / int(n1[2])
                elif type(n1) is int:
                    value1 = n1
                if type(n2) is str:
                    value2 = int(n2[0]) / int(n2[2])
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
            s2.push(s1.pop())
        s1.pop()
    rpnStack = Stack()
    while not s2.IsEmpty():  # s2栈底到栈顶的顺序为RPN，为了方便插入列表中，进行顺序转换
        rpnStack.push(s2.pop())
    while not rpnStack.IsEmpty():  # 将转化好的栈进一步转化为RPN列表
        rpn.append(rpnStack.pop())
    return rpn


if __name__ == "__main__":
    ExGenerator(15, 10)

    """print(HashCheck([9, 9, 9, 9, Operator(opr="÷", pri=1), Operator(opr="÷", pri=1), Operator(opr="÷", pri=1)]))
    print(HashCheck([9, 9, 9, Operator(opr="÷", pri=1), 9, Operator(opr="÷", pri=1), Operator(opr="÷", pri=1)]))"""
    pass
