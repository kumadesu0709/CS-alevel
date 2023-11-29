class Wagon:

    def __init__(self, owner_name:str, weight: float, number_of_wheels: int):
        self._owner_name = owner_name
        self._weight = weight
        self._number_of_wheels = number_of_wheels

    def GetOwnerName(self):
        return self._owner_name

    def GetWeight(self):
        return self._weight

    def GetNumberOfWheels(self):
        return self._number_of_wheels
    
    def set_next_wagon(self, new_wagon):
        self._next_wagon = new_wagon

    def __str__(self):
        return f'Wagon: {self._owner_name}'

class OpenWagon(Wagon):
    pass

class ClosedWagon(Wagon):
    pass

class Sidings:

    def __init__(self):
        self._wagons = [None] * 30
        self._top_pointer = -1
    

    def push(self, new_wagon : Wagon):
        if self._top_pointer < 30:
            self._top_pointer += 1
            self._wagons[self._top_pointer] = new_wagon
        else:
            return f"The siding is already full"

    def pop(self): 
        if self._top_pointer > -1:
            popped_wagon = self._wagons[self._top_pointer] 
            self._top_pointer -= 1
            return f'{popped_wagon} is popped'
        else:
            return f"Siding is empty"
    
    def get_size(self):
        return (int(self._top_pointer) + 1)
    
class Yard:
    def __init__(self, number_of_sidings : int):
        self._number_of_sidings = number_of_sidings
        self._sidings = [Sidings()] * number_of_sidings

            
    def add_wagon_to_siding(self, wagon_to_add:Wagon, siding_number:int):
        if siding_number < self._number_of_sidings:
            self._sidings[siding_number].push(wagon_to_add)
        else:
            return "The siding that you want doesn't exist"
    
    def pop_wagon_from_siding(self,wagon_to_pop,siding_number):
        if siding_number < self._number_of_sidings:
            self._sidings[siding_number].pop(wagon_to_pop)
        else:
            return "The siding that you want doesn't exist"
    
        
        

wagon1 = Wagon("james", 2.8, 12)
wagon2 = Wagon("james g", 2.8, 12)
siding1 = Sidings()
siding1.push(wagon1)
siding1.push(wagon2)
print(siding1.pop())
print(siding1.pop())
print(siding1.pop())