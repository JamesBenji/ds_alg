"""
Shortest Path Algorithm:

This algorithm is an adaptation of the BFS. The basic BFS algorithm node processing is appended with logic to also track
the parent-child relationship of each node. It is this parent-child relationship that we use to backtrack through the
graph starting from the destination to find the shortest path. Therefore, the role of BFS in this algorithm is to build
a parent-child relationship.

For reusability, the algorithm must isolate its internal data from the global scope therefore implemented as a function.

Input: Graph, Start node, Destination node
Output: Path list or None

Algorithm: Blackbox which must be defined
Algorithm definition:
    - Uses BFS, thus must have a set/list (to track "touched" nodes) and a queue (to order the traversal of touched nodes)
        Constraint: A touched node must only be added to the queue once. Therefore, the queue must only contain
        new nodes at any given time.
    - BFS is modified to record a parent-child relationship as a dictionary
    - Backtracking from the destination to the start node such that the path is [start node, ...nodes, destination node]

General cases:
    When destination node is not start node: Follow the algorithm definition

Special cases:
    When destination node is equal to starting node. Use a check + early return before running the expensive BFS

Special notes:
    - Use the deque from collections. It is optimized for data structures unlike Queue from queue module.
    - Use an adjacency list to represent the graph
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

def find_shortest_path(graph, start, target):
    """
    Finds the shortest path from start to target using BFS.
    Returns a list of nodes from start to target, or None if no path exists.
    """

    queue = deque([start])
    viewed = {start}

    parent_map = {start: None}

    # Run BFS
    while queue:
        current_node = queue.popleft()

        if current_node == target:
            break

        for neighbour in graph.get(current_node, []):
            if neighbour not in viewed:
                queue.append(neighbour)
                viewed.add(neighbour)
                parent_map[neighbour] = current_node

    if target not in parent_map:
        return None

    # Reconstruct the path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent_map[current]
        
    path.reverse()
    return path


shortest_path = find_shortest_path(graph, start=0, target=5)
print(f"Shortest path: {shortest_path}")  # Output: [0, 1, 3, 5]