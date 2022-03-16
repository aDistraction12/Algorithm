print("Name : Sumit Singh\nRoll No : 4354\nPrim's Algorithm\n\n")

INF = 9999999
V = 5
G = [[12, 56, 75, 0, 0],
     [19, 0, 59, 39, 44],
     [77, 94, 0, 53, 67],
     [0, 20, 52, 0, 33],
     [0, 42, 68, 31, 0]]
selected = [0, 0, 0, 0, 0]
no_edge = 0
selected[0] = True
print("Edge : Weight\n")
while (no_edge < V - 1):
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1
 
