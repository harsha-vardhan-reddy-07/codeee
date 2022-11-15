maze = [['strt', 'bre', 'pit', 'bre'],
        ['ste', 'ok', 'bre', 'ok'],
        ['wamp', 'bre', 'gold', 'bre'],
        ['bre', 'pit', 'bre', 'pit']]
        
i, j = 0, 0

print(f"You are at position {i},{j}")

while True:
    move = input("Enter L for left, R for right, T for Top, D for down: ")
    if move == 'L':
        if j == 0:
            print("You can't make this move")
            continue
        j = j-1
        
    if move == 'R':
        if j == 3:
            print("You can't make this move")
            continue
        j = j+1
    
    if move == 'T':
        if i == 0:
            print("You can't make this move")
            continue
        i = i-1
            
    if move == 'D':
        if i == 3:
            print("You can't make this move")
            continue
        i = i+1
    
    if maze[i][j] == 'bre':
        print("Carefull!! Pit is in your next room")
    
    elif maze[i][j] == 'ste':
        print("Carefull!! wampus is in your next room")
        
    elif maze[i][j] == 'ok':
        print("You are safe here!!")
    elif maze[i][j] == 'wamp':
        print("Better Luck next time!!")
        break
    elif maze[i][j] == 'pit':
        print("Better Luck next time!!")
        break
    elif maze[i][j] == 'gold':
        print("Congrats!! you won!")
        break