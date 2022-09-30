"""
    @Author: Shay Lin & WhiteDemon
    @Date: 2022/9/24
    @Copyright: Shay Lin & WhiteDemon
    @Description:
"""
from stack import Operator, Stack
from generator import RPNBuild
import os


def CheckAnswer(exePath, ansPath):
    fileExe = open(exePath, "r", encoding="UTF-8")
    fileAns = open(ansPath, "r", encoding="UTF-8")
    lineExe = fileExe.readline()
    lineAns = fileAns.readline()
    exeIndex = 1  # 用于记录题号
    Correct = []  # 答题正确题号的列表
    Wrong = []  # 答题错误题号的列表
    correctCount = 0  # 答题正确的数量
    wrongCount = 0  # 答题错误的数量
    while lineExe and lineAns:
        # print("第%d题" % exeIndex)
        strExe = lineExe
        strAns = lineAns
        listExe = strExe.split(" ")  # 对表达式做去空格处理
        # 删除表达式列表中的序号和"="
        del listExe[0]
        del listExe[-1]
        # 将表达式中的整数转为int
        for i in range(len(listExe)):
            item = listExe[i]
            if item.find('/') == -1 \
                    and (item != '+' and item != '-' and item != '×' and item != '÷' and item != '(' and item != ')'):
                listExe[i] = int(item)
            else:
                pass
        # 删除答案字符串中的序号和"\n"
        div = strAns.find('.')
        if strAns[-1] == '\n':
            strAns = strAns[div + 1:-1]
        else:
            strAns = strAns[div + 1:]
        strAns = strAns.replace(" ", '')  # 去掉答案字符串中的空格
        # 将表达式列表中的运算符由字符类型转为Operator类
        for i in range(len(listExe)):
            opr = Operator()
            if listExe[i] == '+':
                opr.opr = '+'
                opr.pri = 1
                listExe[i] = opr
            elif listExe[i] == '-':
                opr.opr = '-'
                opr.pri = 1
                listExe[i] = opr
            elif listExe[i] == '×':
                opr.opr = '×'
                opr.pri = 2
                listExe[i] = opr
            elif listExe[i] == '÷':
                opr.opr = '÷'
                opr.pri = 2
                listExe[i] = opr
            else:
                pass
        # 将答案strAns中的字符转为数字  ans
        firstIndex = strAns.find('\'')  # 用于判断是否为带分数，若是，则返回该符号所在位置，默认为-1
        secondIndex = strAns.find('/')  # 用于判断是否为分数，若是，则返回该符号所在位置，默认为-1
        if not firstIndex == -1:  # 为带分数时
            num1 = int(strAns[:firstIndex])
            num2 = int(strAns[firstIndex + 1:secondIndex])
            num3 = int(strAns[secondIndex + 1:])
            ans = round((num1 * num3 + num2) / num3, 6)
        elif not secondIndex == -1:  # 为分数时
            num1 = int(strAns[:secondIndex])
            num2 = int(strAns[secondIndex + 1:])
            ans = round(num1 / num2, 6)
        else:  # 为整数时
            ans = round(int(strAns), 6)
        # 得出题目表达式列表listExe的计算结果 calcExe
        # 先生成RPN
        rpn = RPNBuild(listExe)
        calcExe = CalcExe(rpn)
        # 比较结果
        if ans == calcExe:
            correctCount = correctCount + 1  # 答题正确的题目数加1
            Correct.append(exeIndex)  # 记录答题正确的题号
        else:
            wrongCount = wrongCount + 1  # 答题错误的题目数加1
            Wrong.append(exeIndex)  # 记录答题错误的题号
        exeIndex = exeIndex + 1  # 题号数加1
        lineExe = fileExe.readline()  # 读取题目文件的下一行
        lineAns = fileAns.readline()  # 读取答案文件的下一行
    fileExe.close()
    fileAns.close()
    # 在Grade.txt内生成结果
    fileGra = open("./Grade.txt", "w", encoding="UTF-8")
    fileGra.write("Correct:" + str(correctCount) + str(Correct) + "\nWrong:" + str(wrongCount) + str(Wrong))
    fileGra.close()


def CalcExe(rpn):
    # 找出逆波兰式中的分数，并将其由字符转为数字
    for i in range(len(rpn)):
        if type(rpn[i]) is str:
            div = rpn[i].find('/')
            if div == -1:
                pass
            else:
                nume = int(rpn[i][:div])
                deno = int(rpn[i][div + 1:])
                rpn[i] = nume / deno
        else:
            pass
    # print(rpn)
    s1 = Stack()
    for item in rpn:
        if type(item) is Operator:
            num2 = s1.pop()
            num1 = s1.pop()
            if item.opr == '+':
                num = num1 + num2
            elif item.opr == '-':
                num = num1 - num2
            elif item.opr == '×':
                num = num1 * num2
            else:
                num = num1 / num2
            s1.push(num)
        else:
            s1.push(item)
    calcExe = s1.pop()
    return round(calcExe, 6)


if __name__ == "__main__":
    # CheckAnswer("example_exercises.txt", "example_answers.txt")
    CheckAnswer("./测试样例/exer6.txt", "./测试样例/ans6.txt")
