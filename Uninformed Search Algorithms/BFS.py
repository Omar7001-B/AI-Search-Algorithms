graph = {
  5 : [3, 7],
  3 : [2, 4],
  7 : [8],
  2 : [],
  4 : [8],
  8 : []
}

visited = set()
def bfs(start):
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph.get(node, []))

print("Following is the Breadth-First Search")
bfs(5)