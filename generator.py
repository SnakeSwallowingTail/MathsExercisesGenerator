"""
    @Author: Shay Lin & Zhiyong He
    @Date: 2022/9/23
    @Copyright: Shay Lin & Zhiyong He
    @Description:
"""
from stack import Stack, Operator
import random

global hashTable
hashTable = []


def HashInit():  # 初始化哈希表，大小设为10k
    global hashTable
    for i in range(10000):
        hashTable.append(-1)


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
    if oprNum == 3 and hPri == 1:  # 若高优先级操作符数目比低优先级操作符数目少1，且操作符总数目为3，则最多两对括号
        brackets = random.randint(0, 2)
    elif oprNum - hPri == 1 and oprNum != 1:  # 若高优先级操作符数目比低优先级操作符数目多1，且操作符总数目不为1，则最多一对括号
        brackets = random.randint(0, 1)
    else:  # 若操作符全部同级
        brackets = 0
    return oprNum, oprList, brackets


def NumGenerator(oprNum, r):
    # 生成本题的操作数列表
    numList = []
    for i in range(oprNum + 1):
        # 本程序中设定每个参与运算的数字为分数的概率为20%
        isFraction = random.randint[1, 100]
        if 80 <= isFraction <= 100:
            num = ""
            denominator = random.randrange(2, r)  # 生成分母
            # 分子生成前先设定为和分母互质的数
            numerator = r + 1
            while denominator % numerator == 0 or numerator == r + 1:  # 如果分母和分子不互质则重新生成分子
                if numerator == r + 1:
                    numerator = random.randrange(1, denominator)
                numerator = random.randrange(1, denominator)
            num = num + str(numerator) + "/" + str(denominator)
            numList.append(num)
        else:
            num = random.randrange(0, r)
            numList.append(num)
    return numList


def ExGenerator(n, r):  # 生成题目
    HashInit()
    for count in range(n):
        exer = ""  # 题目
        RPN = ""  # 逆波兰式
        oprNum, oprList, brackets = OprGenerator()
        numList = NumGenerator(oprNum, r)

        oprStack = Stack()
        numStack = Stack()
        if CalcCheck(exer):  # 如果检查出存在负数运算过程则重新生成
            count = count - 1
        if HashCheck(exer):  # 如果检查出重复则重新生成
            count = count - 1
        else:
            pass


def CalcCheck(e):  # 运算过程检查,筛出含有负数运算过程的题目
    if e:
        return True
    return False


def AnsGenerator(e):  # 生成答案
    return False


def HashCheck(e):  # 对生成的题目进行哈希并检查是否重复
    if e:
        return True
    return False


if __name__ == "__main__":
    pass
