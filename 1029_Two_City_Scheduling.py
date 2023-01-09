#中等
from typing import List
def twoCitySchedCost(costs: List[List[int]]) -> int:
    totala = 0
    totalb = 0
    costa = 0
    costs.sort(key=lambda x:x[0]-x[1] )
    for a,b in costs:
        if costa < len(costs)//2:
            totala += a
            costa += 1
        else:
            totalb += b
    return totala+ totalb

if __name__ == "__main__":

    costs = [[10,20],[30,200],[400,50],[30,20]]
    Output=110
    print(twoCitySchedCost(costs))