class HashTable:
    def __init__(self, size: int) -> None:
        self.capacity = size
        self.memory = [None] * size

    def display_table(self) -> None:
        for i in range(len(self.memory)):
            if self.memory[i]:
                print(f'bucket=[{i}] hash=[{self.hash(self.memory[i][0])%self.capacity}]: {self.memory[i][0]} -> {self.memory[i][1]}')
                # print(f'[{i}]: {self.memory[i][0]} -> {self.memory[i][1]}')
            else:
                print(f'[{i}]: ---')
        print()

    def hash(self, key: str) -> int:
        #return len(key)
        return sum([ord(c) for c in key])

    def add(self, key: str, value: str) -> None:
        hash_val = self.hash(key) % self.capacity
        while self.memory[hash_val] != None:
            hash_val = (hash_val + 1) % self.capacity
        self.memory[hash_val] = (key, value)

    def find(self, key: str) -> str:
        hash_val = self.hash(key) % self.capacity
        looped_time = 0
        while looped_time < self.capacity:
            kv_pair = self.memory[hash_val]
            if kv_pair:
                if kv_pair[0] == key:
                    return kv_pair[1]
                else:
                    hash_val = (hash_val+1) % self.capacity
                    print("*", end="")
            looped_time += 1
        else:
            return None


ht = HashTable(10)
ht.add('one', 'I')
ht.add('two', 'II')
ht.add('three', 'III')
ht.add('four', 'IV')
ht.add('five', 'V')
ht.add('six', 'VI')
ht.add('seven', 'VII')
ht.add('eight', 'VIII')
ht.add('nine', 'IX')
ht.add('ten', 'X')


ht.display_table()
for look_for in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']:
    print(f'Looking for key="{look_for}", found: {ht.find(look_for)}')