import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 5, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

# Starting node
start_node = 'A'

# Run Dijkstra's algorithm
distances = dijkstra(graph, start_node)

# Output distances
print("Shortest distances from", start_node, ":")
for node, distance in distances.items():
    print("Distance to", node, ":", distance)
