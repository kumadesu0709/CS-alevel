"""
stack = []
s = -1
def pushing():
    item = int(input("input your item: "))
    if s < 4:
        s = s+1
        stack.append(item)
    else:
        print('stack full')
def poping():
    if s >= 0:
        stack.pop(stack[-1])
        s = s-1
    else:
        print("stack empty")
"""

class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

class Empty(Exception):
            pass

S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)