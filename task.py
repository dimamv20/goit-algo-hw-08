import heapq

def min_const_to_connect_cables(cable_legths):
    if not cable_legths:
        return 0 
    heapq.heapify(cable_legths)
    print(cable_legths)
    total_cost = 0
    
    while len(cable_legths) > 1:
        first = heapq.heappop(cable_legths)
        second = heapq.heappop(cable_legths)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(cable_legths,cost)
        print('After push: ', cable_legths)
        
    return total_cost   


if __name__ == '__main__':
    cable_lengths = [15,4,6,8,12]
    print('Мінімальні витрати на  об\'єднання кабелів:', min_const_to_connect_cables(cable_lengths)) 