graph = {
    5 : [3, 7],
    3 : [2, 4],
    7 : [8],
    2 : [],
    4 : [8],
    8 : []
}

visited = set()
def dfs(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))

print("Following is the Depth-First Search")
dfs(5)
