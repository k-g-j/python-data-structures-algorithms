from heapq import heappop, heappush
from math import inf

"""
Dijkstra's Algorithm

Find the shortest path from a start vertex to all other vertices in the graph.

Time Complexity: O((E+V)log V)
Space Complexity: O(V)
"""

graph = {
    'A': [('B', 10), ('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('A', 7)],
    'B': [('C', 3), ('D', 2)]
}


def dijkstras(graph, start):
    distances = {}

    for vertex in graph:
        distances[vertex] = inf

    distances[start] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    return distances


distances_from_d = dijkstras(graph, 'D')
print(f"\n\nShortest Distances: {distances_from_d}\n\n")
