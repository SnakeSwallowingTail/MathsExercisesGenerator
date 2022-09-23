"""
    @Author: Shay Lin & Zhiyong He
    @Date: 2022/9/23
    @Copyright: Shay Lin & Zhiyong He
    @Description:
"""
import os.path
import sys
from stack import Stack


def ParaIn():  # 读取命令行参数并检查
    exeCount = None
    numRange = None
    exePath = ""
    ansPath = ""
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == "-n":
            try:
                exeCount = int(sys.argv[i + 1])
            except IndexError:
                print("[-]缺少参数，请检查参数是否正确")
        elif sys.argv[i] == "-r":
            try:
                numRange = int(sys.argv[i + 1])
            except IndexError:
                print("[-]缺少参数，请检查参数是否正确")
        elif sys.argv[i] == "-e":
            try:
                exePath = sys.argv[i + 1]
            except IndexError:
                print("[-]缺少参数，请检查参数是否正确")

        elif sys.argv[i] == "-a":
            try:
                ansPath = sys.argv[i + 1]
            except IndexError:
                print("[-]缺少参数，请检查参数是否正确")
        else:
            print("[-]参数不合法，请检查参数是否正确")
            exit(0)
    if exeCount is None or numRange is None:
        print("[-]题目个数或数值范围未给定，请检查参数是否正确")
        exit(0)


if __name__ == "__main__":
    ParaIn()
    pass
