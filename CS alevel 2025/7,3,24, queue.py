class Queue:
    def __init__(self, size:int) -> None:
        self.memory = [None] * size
        self.front = 0
        self.rear = 0
    
    def add(self, data:str):
        self.memory[self.rear] = data
        self.rear += 1
    
    def remove(self) -> str:
        popped = self.memory[self.front]
        self.front += 1
        return popped

    def tidy(self):
        to_i = 0
        for from_i in range(self.front, self.rear):
            self.memory[to_i] = self.memory[from_i]
            to_i += 1
        self.rear = to_i
        self.front = 0
    def show_queue(self):
        return self.memory[self.front:self.rear]

queue_one = Queue(300)
for i in range(0,101):
    queue_one.add(str(i))
queue_one.remove()
print(queue_one.show_queue())