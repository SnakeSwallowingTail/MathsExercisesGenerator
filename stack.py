"""
    @Author: Shay Lin & Zhiyong He
    @Date: 2022/9/23
    @Copyright: Shay Lin & Zhiyong He
    @Description:
"""


class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def pop(self):
        if self.size == 0:
            return OverflowError
        item = self.data[self.size - 1]
        self.size = self.size - 1
        return item

    def push(self, item):
        self.data.append(item)
        self.size = self.size + 1


class Operator:
    def __init__(self):
        self.opr = None
        self.pri = None
