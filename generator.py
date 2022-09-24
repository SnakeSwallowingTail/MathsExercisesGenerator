"""
    @Author: Shay Lin & Zhiyong He
    @Date: 2022/9/23
    @Copyright: Shay Lin & Zhiyong He
    @Description:
"""
from stack import Stack
import random

global hashTable
hashTable = []


def HashInit():  # 初始化哈希表，大小设为10k
    global hashTable
    for i in range(10000):
        hashTable.append(-1)


def ExGenerator(n, r):  # 生成题目
    for count in range(n):
        # 随机确定一共有几个运算符和括号，运算符个数范围[1,3]，括号对数范围[0,1]
        operNum = random.randint(1, 3)
        brankets = random.randint(0, 1)
        exer = ""

        if HashCheck(exer):  # 如果检查出重复则重新生成
            count = count - 1
        else:
            pass


def AnsGenerator(e):  # 生成答案
    pass


def HashCheck(e):  # 对生成的题目进行哈希并检查是否重复
    if True:
        return True
    else:
        return False


if __name__ == "__main__":
    pass
