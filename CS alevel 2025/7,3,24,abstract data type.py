class Stack:
    def __init__(self, size:int) -> None:
        self.memory = [None] * size
        self.top = 0
    
    def add(self, data:str):
        self.memory[self.top] = data
        self.top += 1
    
    def remove(self) -> str:
        self.top -= 1
        popped = self.memory[self.top]
        self.memory[self.top] = None
        return popped

    def show_stack(self):
        return self.memory

stack_one = Stack(5)
stack_one.add("300")
print(stack_one.remove())
print(stack_one.show_stack())


