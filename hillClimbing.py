


closed = []
graph = {}
c = 1 
while c ==1:
    node = input("enter node: ")
    child = [[s.split()[0]], int(s.split()[1])]
    for s in input("Enter neighbors of node: ").split(',')
    graph[node] = child
    choice = int(input("Enter 1 to continue: "))
start = input("Enter start node: ")
stHeuCost=int(input("Heu cost of start node: "))

def neighbors(n):
    if n in graph.keys():
        return graph[n]

def heuCost(N):
    return N[1]

def heuSort(l):
    l.sort(key=lambda x:x[1])

def hillClimbing(start, stHeuCost):
    global closed
    N = [start, stHeuCost]
    closed = closed + [N]
    print("Path till now",closed)
    child = neighbors(start)
    if child:
        heuSort(child)
        print("Sorted neighbors: ", child)
    else:
        print("No neighbors")
    while(child and heuCost(child[0])<heuCost(N)):
        N = child[0]
        closed += [N]
        print("Path till now", closed)
        child = neighbors(start)
    if child:
        heuSort(child)
        print("Sorted neighbors: ", child)
        
hillClimbing(start, stHeuCost)