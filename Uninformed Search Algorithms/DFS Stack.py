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
            for child in reversed(graph[node]): # Reversed to make it go left branches
                stack.append(child)

print("Following is the Depth-First Search")
dfs(5)
