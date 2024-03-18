graph = {
    5 : [3, 7],
    3 : [2, 4],
    7 : [8],
    2 : [],
    4 : [8],
    8 : []
}

visited = set()
def dfs(node, target, depth):
    if node == target:
        return "Found"
    if depth == 0:
        return "Not Found"

    if node not in visited:
        visited.add(node)
        for child in graph.get(node, []):
            res = dfs(child, target, depth - 1)
            if res == "Found":
                return res

    return "Not Found"

# Driver Code
print("Following is the Depth-First Search")
print(dfs(5, 7, 1))
