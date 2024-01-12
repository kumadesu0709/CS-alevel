class Node:
    def __init__(self, data, next_node):
        self._data = data
        self._next_node = next_node
    def get_data(self):
        return self._data
    def set_next_node(self, new_node):
        self._next_node = new_node
class Stack:
    def __init__(self, headNodeData):
        self._size = 0
        self._headnode = Node(headNodeData, None)
    def push(self, data):
        new_node = Node(data, self._headnode)
        self._headnode = new_node
        self._size = self._size + 1
    def pop(self): 
        retdata = self._headnode._data
        self._headnode = self._headnode._next_node
        self._size -= 1
        return retdata
    def get_size(self):
        return self._size

LList = Stack("A")
LList.push("A")
LList.push("B")
print(LList.pop())
print(LList.get_size())
LList.push("ANC")
print(LList.pop())


#Sir is there a way for me to display the entire linked list?