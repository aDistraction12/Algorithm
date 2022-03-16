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

visited = [] # List to keep track of visited nodes.
queue = []   #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    a = queue.pop(0) 
    print (a, end = " ") 

    for neighbour in graph[a]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Breadth First Search")
bfs(visited, graph, '2')
