"""
DFS Application: Determining if a graph has connected components, ie, the graph data is not one large block.
The data is rather showing different smaller graphs being represented in the same dataset without interlinkages
"""

graph = {
    0: [1,2],
    1: [0,2],
    2: [0,1],
    3: [4],
    4: [3],
    5: []
}

number_of_nodes = len(graph)

visited = set()

components = {}

count = 0

def dfs(current_node):
    visited.add(current_node)
    components[current_node] = count

    for neighbour in graph[current_node]:
        if neighbour not in visited:
            dfs(neighbour)

def find_components():
    global count

    for node in range(number_of_nodes):
        if node not in visited:
            count += 1
            dfs(node)

    return count, components

total_components, node_mappings = find_components()

for node, component_id in node_mappings.items():
    print(f"Node {node} in component {component_id}")