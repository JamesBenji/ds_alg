"""
Depth First Search Algorithm (DFS)

Purpose: Illustrate the base implementation of DFS. This can be adapted for other use-cases
Input: graph structure (dictionary: Adjacency list) and start vertex/node
Output: Print statements of tree traversal

"""

# Key = Node
# Value = Connected nodes hence edges

graph_dict = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1, 5],
    4: [1, 2, 5],
    5: [3, 4]
}

visited = set()

def DFS(current_node):
    # base case: if visited, return
    if current_node in visited:
        return

    # any current node processing logic

    print(f"Processing {current_node}")

    visited.add(current_node)

    for neighbour in graph_dict.get(current_node):
        DFS(neighbour)


start_node = 0
DFS(start_node)
