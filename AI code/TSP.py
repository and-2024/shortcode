# TSP:
import sys

def all_visited(visited):
    return all(visited)

def tsp(visited, cost, current, path, n):
    global min_cost, ans
    if(all_visited(visited)):
        if (cost+graph[current][0]<min_cost):
            min_cost=cost+graph[current][0]
            ans=path+[0]
        return
    for i in range(n):
        if not visited[i] and i!=current:
            visited[i]=True
            tsp(visited,cost+graph[current][i],i,path+[i], n)
            visited[i]=False

if __name__=="__main__":
    print("Enter Total No of Vertices:")
    n=int(input())
    graph=[]

    for i in range (n):
        row=[]
        for j in range(n):
            if(i!=j):
                print(f"Enter the Distance of {i} to {j}")
                dist=int(input())
                row.append(dist)
            else:
                row.append(0)
        graph.append(row)


    for i in range(n):
        for j in range(n):
            print(graph[i][j], end="\t")
        print()
    
    path = []  # For storing the shortest path
    visited = [False] * n  # Initializing visited array with all False values
    min_cost = sys.maxsize
    visited[0] = True  # Marking the first node as visited

    tsp(visited, 0, 0, [0], n)
    print("Shortest Path:", ans)
    print("Cost:", min_cost)
 
# output:
# Enter Total No of Vertices:
# 4
# Enter the Distance of 0 to 1
# 10
# Enter the Distance of 0 to 2
# 15
# Enter the Distance of 0 to 3
# 20
# Enter the Distance of 1 to 0
# 10
# Enter the Distance of 1 to 2
# 35
# Enter the Distance of 1 to 3
# 25
# Enter the Distance of 2 to 0
# 15
# Enter the Distance of 2 to 1
# 35
# Enter the Distance of 2 to 3
# 30
# Enter the Distance of 3 to 0
# 20
# Enter the Distance of 3 to 1
# 25
# Enter the Distance of 3 to 2
# 30
# 0       10      15      20
# 10      0       35      25
# 15      35      0       30
# 20      25      30      0
# Shortest Path: [0, 1, 3, 2, 0]
# Cost: 80
