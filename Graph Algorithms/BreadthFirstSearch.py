"""
Breadth First Search (BFS)

Idea: Each node may be connected to other nodes. These node-to-node connections repeat forming a node hierarchy.
The nodes a certain node N is connected to are finite, and we can find the target element by first looking
at those nodes we are connected to before going deep into the graph. The graph representation provides a list
of the direct connections to N. It is possible to iterate over these direct connections in search for the target.
If not found, we can iterate through their connections. But how do we ensure that the direct connections are processed
first regardless of order? By using a queue (First In, First Out)

Since the graph is undirected and fully connected with only one component, traversal in both directions is possible
meaning we can start from any node and still span the entire graph. This allows the use of any node as the start.

Items added to the queue must immediately be marked as viewed.
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

def BFS(start_node):
    for_processing_queue.append(start_node)
    viewed_items.add(start_node)

    while for_processing_queue:
        current_node = for_processing_queue.popleft()
        neighbours = graph.get(current_node)

        for neighbour in neighbours:
            if neighbour not in viewed_items:
                for_processing_queue.append(neighbour)
                viewed_items.add(neighbour)

BFS(0)

print(viewed_items)