class CircularQueue:
    def __init__(self, maxlength):
        self._data = []
        self._maxlength = maxlength

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def add(self, e):
        if len(self._data) < self._maxlength:
            self._data.append(e)
        else:
            return print(f"Queue is full, so {e} can't be added into the queue.")
    
    def remove(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data.remove(self._data[0])
    
    def is_full(self):
        if len(self._data) == self._maxlength:
            return "Queue is full"
        else:
            return "Queue is not full"
    
    def __str__(self):
        return str(self._data)

class Empty(Exception):
            pass

S = CircularQueue(4)
S.add(5)
S.add(10)
print(S)
print(S.is_full())
S.add(11)
S.add(13)
print(S.is_full())
S.remove()
S.remove()
S.remove()
print(S)
