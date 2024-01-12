graph = {
  'A' : ['B','C','D'],
  'B' : ['E','F'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : []
}
visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')