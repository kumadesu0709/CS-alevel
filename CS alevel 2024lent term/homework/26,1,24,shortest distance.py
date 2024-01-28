from itertools import permutations
def CalculateDeliveryCost(self):
    ListOfOutlets = self.__GetListOfOutlets()
    permutated_list = list(permutations(ListOfOutlets))
    all_distance = []
    for Current in range (0, len(permutated_list)):
        distance = 0.0
        combination = permutated_list[Current]
        for i in range (0, len(combination)):
            distance += self.__GetDistanceBetweenTwoOutlets(ListOfOutlets[i], ListOfOutlets[i + 1])
        all_distance.append(distance)
    all_distance.sort()
    TotalCost = all_distance[0] * self._FuelCostPerUnit
    return TotalCost