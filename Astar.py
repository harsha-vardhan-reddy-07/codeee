
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}    

H = { 'A':1,
      'B':1,
      'C':1,
      'D':1
}

        
def algorithm(start_node, stop_node, adjacency_list, H):
    open_list = set([start_node])
    closed_list = set([])
    g = {}
    g[start_node] = 0
    parents = {}
    parents[start_node] = start_node
    
    while len(open_list) > 0:
        n = None
        
        for v in open_list:
            if n == None or g[v] + H[v] < g[n] + H[n]:
                n = v
        
        if n == None:
            print("No path found!!")
            pass
        
        if n == stop_node:
            path = []
            while parents[n] != n:  ## till we reach back strt node as for strt node parents[strt] = strt
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print(f"Path found: {path}")
            return path
        
        for (m, weight) in adjacency_list[n]:
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n 
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)
        
        open_list.remove(n)
        closed_list.add(n)
    print("Path dosent exist")
    return None




algorithm('A', 'D', adjacency_list, H)
