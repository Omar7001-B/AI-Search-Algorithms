graph = {
  5 : [3, 7],
  3 : [2, 4],
  7 : [8],
  2 : [],
  4 : [8],
  8 : []
}

visited = set()
def dfs(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for child in graph.get(node, []):
            dfs(child)

# Driver Code
print("Following is the Depth-First Search")
dfs(5)