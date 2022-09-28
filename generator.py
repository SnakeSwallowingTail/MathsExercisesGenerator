"""
    @Author: Shay Lin & WhiteDemon
    @Date: 2022/9/23
    @Copyright: Shay Lin & WhiteDemon
    @Description:
"""
from stack import Stack, Operator
import random

global hashTable
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
        RPN = RPNBuild(exer)
        if CalcCheck(RPN):  # 如果检查出存在负数运算过程则重新生成
            count = count - 1
            continue
        if HashCheck(exer):  # 如果检查出重复则重新生成
            count = count - 1
            continue
        AnsGenerator(exer, count)
        # exer = exer + "="
        for item in exer:
            if type(item) is str or type(item) is int:
                print(item, end=" ")
            else:
                print(item.opr, end=" ")
        print()
        f = open("./exersices.txt", "w+", encoding="UTF-8")
        f.close()


def CalcCheck(rpn):  # 运算过程检查,筛出含有负数运算过程的题目
    flag = False
    s = Stack()
    for i in range(len(rpn)):
        n1 = None
        n2 = None
        if type(rpn[i]) == Operator:
            n2 = s.pop()
            n1 = s.pop()
            for f in [n1, n2]:
                if type(f) == str:
                    f = int(f[0]) / int(f[2])
            if rpn[i].opr == "+":
                n = n1 + n2
            elif rpn[i].opr == "-":
                n = n1 - n2
            elif rpn[i].opr == "×":
                n = n1 * n2
            else:
                n = n1 / n2
                if n2 == 0:
                    return True
            if n < 0:
                return True
            s.push(n)
        else:
            s.push(rpn[i])
    return False


def HashCheck(rpn):  # 对生成的题目进行哈希并检查是否重复
    P = 131
    hash = 0
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
    return rpn


if __name__ == "__main__":
    ExGenerator(10000, 10)

    """print(HashCheck([9, 9, 9, 9, Operator(opr="÷", pri=1), Operator(opr="÷", pri=1), Operator(opr="÷", pri=1)]))
    print(HashCheck([9, 9, 9, Operator(opr="÷", pri=1), 9, Operator(opr="÷", pri=1), Operator(opr="÷", pri=1)]))"""
    pass
