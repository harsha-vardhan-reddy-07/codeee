import math

n = int(input("No of nodes: "))
scores=[]
for i in range(n):
    x = int(input("Enter node score: "))
    scores.append(x)
    

target_depth = math.log(len(scores), 2)

min_value, max_value = -1000, 1000

def alphabeta(current_depth, node_index, max_turn, alpha, beta, scores, target_depth):
    if current_depth == target_depth:
        return(scores[node_index])
    
    if max_turn:
        best = min_value
        for i in range(2):
            val = alphabeta(current_depth+1, node_index * 2 + i, False, alpha, beta, scores, target_depth)
            best = max(val, best)
            alpha = max(alpha, best)
            
            if(alpha >= beta):
                break
        return best
    
    else:
        best = max_value
        for i in range(2):
            val = alphabeta(current_depth+1, node_index*2+i, True, alpha, beta, scores, target_depth)
            best = min(val, best)
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best

print(alphabeta(0, 0, True, min_value, max_value, scores, target_depth))
            
            
            
    
    
    

