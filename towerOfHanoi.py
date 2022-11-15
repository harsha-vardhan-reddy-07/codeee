n = int(input("No.of disks: "))
source = input("Enter source rod: ")
destination = input("Enter destination rod: ")
auxilary = input("Enter auxilary rod: ")

def TowerOfHanoi(n, source, auxilary, destination):
    if n == 1:
        print(f"Move disk {n} from {source} to {destination}")
        return
    TowerOfHanoi(n-1, source, auxilary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    TowerOfHanoi(n-1, auxilary, destination, source)


TowerOfHanoi(n, source, auxilary, destination)  
            
            
        
        
