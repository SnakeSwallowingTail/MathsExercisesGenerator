"""
    @Author: Shay Lin & WhiteDemon
    @Date: 2022/9/23
    @Copyright: Shay Lin & WhiteDemon
    @Description:
"""


class Stack:
    def __init__(self, data, size):
        self.data = data
        self.size = size

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
    def __init__(self, opr, pri):
        self.opr = opr
        self.pri = pri
