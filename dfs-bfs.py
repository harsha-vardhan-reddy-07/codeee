graph = {}
dfs_visited = []
bfs_visited = []
queue = []

c = 1 
while c==1:
    key = input("Enter the node: ")
    values = list(input("Enter neighbor nodes: ").split(' '))
    graph[key] = values
    c = int(input("Enter 1 to continue, 0 to exit: "))

start = input("Enter the start node: ")

def dfs(graph, dfs_visited, node):
    if node not in dfs_visited:
        print(node, end=' ')
        dfs_visited.append(node)
        
        if node in graph.keys():
            for neighbor in graph[node]:
                dfs(graph, dfs_visited, neighbor)

def bfs(graph, bfs_visited, node, queue):
    bfs_visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        
        if m in graph.keys():
            for neighbor in graph[m]:
                if neighbor not in bfs_visited:
                    queue.append(neighbor)
                    bfs_visited.append(neighbor)

dfs(graph, dfs_visited, start)
bfs(graph, bfs_visited, start, queue)




