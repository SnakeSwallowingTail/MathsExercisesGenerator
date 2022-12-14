"""
    @Author: Shay Lin & WhiteDemon
    @Date: 2022/9/23
    @Copyright: Shay Lin & WhiteDemon
    @Description:
"""
import os.path
import sys
import generator
import marking


def ParaIn():  # 读取命令行参数并检查
    exeCount = None  # 题目数量
    numRange = None  # 数值范围
    exePath = None  # 题目路径
    ansPath = None  # 答案路径
    if len(sys.argv) > 5:
        print("[-]参数过多，请减少参数数目")
        exit(0)
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == "-n":  # 代表后面的参数为题目数量
            try:
                exeCount = int(sys.argv[i + 1])
            except IndexError:
                print("[-]缺少参数，请输入自然数")
            except ValueError:
                print("[-]参数不合法，应为自然数")
        elif sys.argv[i] == "-r":  # 代表后面的参数为数值范围
            try:
                numRange = int(sys.argv[i + 1])
            except IndexError:
                print("[-]缺少参数")
            except ValueError:
                print("[-]参数不合法，应为自然数")
        elif sys.argv[i] == "-e":  # 代表后面的参数为题目文件的路径
            try:
                exePath = sys.argv[i + 1]
            except IndexError:
                print("[-]缺少参数")
        elif sys.argv[i] == "-a":  # 代表后面的参数为答案文件的路径
            try:
                ansPath = sys.argv[i + 1]
            except IndexError:
                print("[-]缺少参数")
        else:
            print("[-]参数不合法")
            exit(0)
    ParaCheck(exeCount, numRange, exePath, ansPath)
    return exeCount, numRange, exePath, ansPath


def ParaCheck(exeCount, numRange, exePath, ansPath):
    if not ((exeCount and numRange and exePath is None and ansPath is None)
            or (exeCount is None and numRange is None and exePath and ansPath)):
        # 既不是 1 1 0 0 ， 也不是0 0 1 1 时 执行下面的语句
        print("[-]给定的参数不合法，无法识别要执行的功能")
        exit(0)
    elif exeCount is None and numRange is None:  # 为对答案的命令时，exeCount和numRange应为None，检查两个路径是否都不为None
        if not os.path.exists(exePath):
            print("[-]题目路径不存在")
            exit(0)
        if not os.path.exists(ansPath):
            print("[-]答案路径不存在")
            exit(0)


if __name__ == "__main__":
    exeCount, numRange, exePath, ansPath = ParaIn()
    if exeCount and numRange:
        generator.ExGenerator(exeCount, numRange)
    else:
        marking.CheckAnswer(exePath, ansPath)
