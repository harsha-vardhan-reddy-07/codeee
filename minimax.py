import math
n = int(input("No of leaves: "))
scores = []
for i in range(n):
    x = int(input("Enter score: "))
    scores.append(x)

def minmax(current_depth, node_index, max_turn, scores, target_depth):
    if current_depth == target_depth:
        return scores[node_index]
    
    if max_turn:
        return max(minmax(current_depth+1, node_index*2, False, scores, target_depth), minmax(current_depth+1, node_index*2 + 1, False, scores, target_depth))
    else:
        return min(minmax(current_depth+1, node_index*2, True, scores, target_depth), minmax(current_depth+1, node_index*2 +1, True, scores, target_depth))
        

target_depth = math.log(len(scores),2)
print("The final score is: ",end="")
print(minmax(0, 0, True, scores, target_depth))
