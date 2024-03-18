graph = {
    'S': [('A', 2), ('B', 3), ('D', 5)],
    'A': [('C', 4)],
    'B': [('D', 4)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 5)],
    'G': []
}
def pathCost(path):
    totalCost = 0
    for node, cost in path:
        totalCost += cost
    return totalCost, path[-1][0]

def ucs(start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=pathCost)
        path = queue.pop(0)
        node = path[-1][0]
        if node == goal:
            return path
        if node not in visited:
            visited.append(node)
            for child in graph.get(node, []):
                queue.append(path + [child])

print("The Path is: ", ucs('S', 'S'))