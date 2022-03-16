print("Name : Sumit Singh\nRoll No : 4354\n")

graph = {
'2' : ['0','5'],
'0' : ['4','7'],
'5' : ['9'],
'4' : ['2'],
'7' : ['3'],
'9' : [],
'3' : [],
}

visited = set() #Set to keep track of visited nodes of graph

def dfs(visited , graph, node): #function for dfs
    if node not in visited :
        print(node)
        visited.add(node)
        for neighbour in graph[node] :
            dfs(visited, graph, neighbour)

#Driver Code
print("Following is the Depth-First Search")
dfs(visited,graph,'2')
