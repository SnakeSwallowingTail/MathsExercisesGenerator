"""
    @Author: Shay Lin & WhiteDemon
    @Date: 2022/9/23
    @Copyright: Shay Lin & WhiteDemon
    @Description:
"""


class Stack:
    def __init__(self, data=list(), top=int()):
        self.data = data
        self.top = top

    def pop(self):
        if self.top == 0:
            return OverflowError
        item = self.data[self.top - 1]
        self.top = self.top - 1
        return item

    def push(self, item):
        self.data.append(item)
        self.top = self.top + 1

    def IsEmpty(self):
        if self.top == 0:
            return True


class Operator:
    def __init__(self, opr=str(), pri=int()):
        self.opr = opr
        self.pri = pri
