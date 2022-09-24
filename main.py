"""
    @Author: Shay Lin & Zhiyong He
    @Date: 2022/9/23
    @Copyright: Shay Lin & Zhiyong He
    @Description:
"""
import os.path
import sys


def ParaIn():  # 读取命令行参数并检查
    exeCount = None
    numRange = None
    exePath = None
    ansPath = None
    if len(sys.argv) > 5:
        print("[-]参数过多，请减少参数数目")
        exit(0)
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == "-n":
            try:
                exeCount = int(sys.argv[i + 1])
            except IndexError:
                print("[-]缺少参数，请输入自然数")
            except ValueError:
                print("[-]参数不合法，应为自然数")
        elif sys.argv[i] == "-r":
            try:
                numRange = int(sys.argv[i + 1])
            except IndexError:
                print("[-]缺少参数")
            except ValueError:
                print("[-]参数不合法，应为自然数")
        elif sys.argv[i] == "-e":
            try:
                exePath = sys.argv[i + 1]
            except IndexError:
                print("[-]缺少参数")
        elif sys.argv[i] == "-a":
            try:
                ansPath = sys.argv[i + 1]
            except IndexError:
                print("[-]缺少参数")
        else:
            print("[-]参数不合法")
            exit(0)



def ParaCheck(exeCount, numRange, exePath, ansPath):
    if (exeCount is None or numRange is None) and \
            (exePath is not None and ansPath is not None):
        print("[-]题目个数或数值范围未给定，请检查参数是否正确")
        exit(0)
    if not os.path.exists(exePath):
        print("[-]题目路径不存在")
        exit(0)
    if not os.path.exists(ansPath):
        print("[-]答案路径不存在")
        exit(0)
    if exeCount and numRange and exePath and ansPath:
        print("[-]参数过多，")


if __name__ == "__main__":
    ParaIn()
    pass