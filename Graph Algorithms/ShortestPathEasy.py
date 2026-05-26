"""
Shortest Path Algorithm

As a continuation of BFS. This option is meant to show the link between BFS and shortest path as an incremental step.
For a self-contained solution, consider the ShortestPath.py
"""

from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4, 5],
    4: [2, 3],
    5: [3]
}

for_processing_queue = deque()

viewed_items = set()

parent_map = {}

def BFS(start_node):
    for_processing_queue.append(start_node)
    viewed_items.add(start_node)
    parent_map[start_node] = None

    while for_processing_queue:
        current_node = for_processing_queue.popleft()
        neighbours = graph.get(current_node)

        for neighbour in neighbours:
            if neighbour not in viewed_items:
                for_processing_queue.append(neighbour)
                viewed_items.add(neighbour)
                parent_map[neighbour] = current_node


def find_shortest_path(destination):
    return parent_map.get(destination, None)

BFS(0)

path = []
target = 5
k = target

while k is not None:
    path.append(k)
    k = find_shortest_path(k)

path.reverse()
print(path)

print(viewed_items)