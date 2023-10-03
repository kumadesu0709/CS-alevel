class ArrayStack:
    def __init__(self, maxlength):
        self._data = []
        self._maxlength = maxlength

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        if len(self._data) << self._maxlength:
            self._data.append(e)
        else:
            return "Queue is full"
    
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[1]
    
    def pop(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data.remove(self._data[1])

class Empty(Exception):
            pass