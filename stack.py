"""
    @Author: Shay Lin & WhiteDemon
    @Date: 2022/9/23
    @Copyright: Shay Lin & WhiteDemon
    @Description:
"""


class Stack:
    def __init__(self):
        self.data = list()
        self.top = 0

    def pop(self):
        if self.top == 0:
            return OverflowError
        item = self.data[self.top - 1]
        del self.data[self.top - 1]
        self.top = self.top - 1
        return item

    def push(self, item):
        t = self.data
        t.append(item)
        self.top = self.top + 1

    def IsEmpty(self):
        if self.top == 0:
            return True


class Operator:
    def __init__(self):
        self.opr = ""
        self.pri = int()
