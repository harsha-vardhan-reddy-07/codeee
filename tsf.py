from sys import maxsize
from itertools import permutations

n = 4

# s - strt point 

def tsf(graph, s):
    vertex = []
    for i in range(n):
        if i != s:
            vertex.append(i)
    
    min_cost = 10**9
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_cost = 0
        k = s
        for j in i:
            current_cost += graph[k][j]
            k = j 
        current_cost += graph[k][s]
        min_cost = min(min_cost, current_cost)
    return min_cost

graph = [[0, 10, 15, 20], [10, 0, 35, 25],
		[15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
print(tsf(graph, s))
        
        
        
            
            
            
    