class Animal:
    
    def __init__(self,state, size, number):
        self._state = state
        self._size = size
        self._number = number
    
    def feed(self):
        self._size += 1
        print(f"{self._state} fed")
        if self._size == 5:
            self._state = self._state.upper()
    def kill(self):
        self._number -= 1
        print(f"A {self._state} is dead")
        if self._number == 0:
            print(f"All the {self._state} are dead")
    def sound(self):
        sounds = {"Dog":"Woof", "Cat":"Mew", "Cow":"Mooo","Fish": "????"}
        sound = sounds[self._state]
        print(f"{self._state} makes a {sound} sound")

thisfish = Animal('Fish', 1, 10)
for i in range (1,11):
    thisfish.kill()