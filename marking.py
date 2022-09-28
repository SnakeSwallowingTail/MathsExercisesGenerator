"""
    @Author: Shay Lin & WhiteDemon
    @Date: 2022/9/24
    @Copyright: Shay Lin & WhiteDemon
    @Description:
"""
Corret = []  # 答题正确题号的列表
Wrong = []  # 答题错误题号的列表
corretCount = 0  # 答题正确的数量
wrongCount = 0  # 答题错误的数量


def CheckAnswer():
    fileExe = open("example_exercises.txt", "r", encoding="UTF-8")
    fileAns = open("example_answers.txt", "r", encoding="UTF-8")
    lineExe = fileExe.readline()
    lineAns = fileAns.readline()
    exeIndex = 1  # 用于记录题号
    while (lineExe and lineAns):
        strExe = lineExe
        strAns = lineAns
        listExe = strExe.split(" ")  # 对表达式做去空格处理
        # 删除表达式列表中的序号和"="
        del listExe[0]
        del listExe[-1]
        # 删除答案字符串中的序号和"\n"
        if strAns[-1] == '\n':
            strAns = strAns[2:-1]
        else:
            strAns = strAns[2:]
        strAns = strAns.replace(" ", '')  # 去掉答案字符串中的空格
        print(listExe)
        print(strAns)
        lineExe = fileExe.readline()  # 读取题目文件的下一行
        lineAns = fileAns.readline()  # 读取答案文件的下一行
    fileExe.close()
    fileAns.close()


if __name__ == "__main__":
    CheckAnswer()
