"""
    @Author: Shay Lin & Zhiyong He
    @Date: 2022/9/23
    @Copyright: Shay Lin & Zhiyong He
    @Description:
"""
import os.path
import sys


def ParaIn():  # 读取命令行参数并检查
    exeCount = None     #题目数量
    numRange = None     #数值范围
    exePath = None      #题目路径
    ansPath = None      #答案路径
    if len(sys.argv) > 5:
        print("[-]参数过多，请减少参数数目")
        exit(0)
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == "-n":             #代表后面的参数为题目数量
            try:
                exeCount = int(sys.argv[i + 1])
            except IndexError:
                print("[-]缺少参数，请输入自然数")
            #   exit(0)                         #一遇到错误或异常情况就退出？
            except ValueError:
                print("[-]参数不合法，应为自然数")
            #   exit(0)
        elif sys.argv[i] == "-r":           #代表后面的参数为数值范围
            try:
                numRange = int(sys.argv[i + 1])
            except IndexError:
                print("[-]缺少参数")
            #   exit(0)
            except ValueError:
                print("[-]参数不合法，应为自然数")
            #   exit(0)
        elif sys.argv[i] == "-e":           #代表后面的参数为题目文件的路径
            try:
                exePath = sys.argv[i + 1]
            except IndexError:
                print("[-]缺少参数")
            #   exit(0)
            #if not os.path.exists(exePath):        #直接在这里检查文件是否存在？
            #    print("[-]题目路径不存在")
            #    exit(0)
        elif sys.argv[i] == "-a":           #代表后面的参数为答案文件的路径
            try:
                ansPath = sys.argv[i + 1]
            except IndexError:
                print("[-]缺少参数")
            #if not os.path.exists(ansPath):        #直接在这里检查文件是否存在？
            #    print("[-]答案路径不存在")
            #    exit(0)
        else:
            print("[-]参数不合法")
            exit(0)






def ParaCheck(exeCount, numRange, exePath, ansPath):   #或许不用检查exeCount和numRange?只需检查文件路径，
                                                        # 然后检查直接在ParaIn里检查，不用另写函数
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
        print("[-]参数过多，请减少参数数目")


if __name__ == "__main__":
    ParaIn()
    pass
