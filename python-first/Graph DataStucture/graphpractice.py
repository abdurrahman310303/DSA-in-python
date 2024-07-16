Directed_graph = {
    "a": ["b", "d"],
    "b": [],
    "c": [],
    "d": ["e", "g"],
    "e": ["c"],
    "f": [],
    "g": ["f"]
}

Undirected_graph = {
    "a": ["b", "c"],
    "b": ["a", "f", "d"],
    "c": ["a"],
    "d": ["b", "g", "i"],
    "e": ["f", "h"],
    "f": ["b", "e"],
    "g": ["d", "h"],
    "h": ["e", "g"],
    "i": ["d"]
}

def Directed_DFS(graph, source):
    stack = []
    stack.append(source)

    while stack:
        node = stack.pop(-1)
        print(node, end=" ")
        for neighbours in graph[node]:
            stack.append(neighbours)

def Directed_BFS(graph, source):
    queue = []
    queue.append(source)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbours in graph[node]:
            queue.append(neighbours)

def hasPath(src, dest, graph):
    if src == dest:
        return True
    ans = False
    for neighbour in graph[src]:
        ans = ans or hasPath(neighbour, dest, graph)
    return ans

def Undirected_HasPath(src, dest, graph, vis):
    if src == dest:
        return True
    vis.add(src)
    ans = False
    for neighbour in graph[src]:
        if neighbour not in vis:
            ans = ans or Undirected_HasPath(neighbour, dest, graph, vis)
    return ans

print("Directed DFS:")
Directed_DFS(Directed_graph, "a")
print("\nDirected BFS:")
Directed_BFS(Directed_graph, "a")

src = "a"
dest = "e"
print(f"\nPath exists from {src} to {dest} in Directed Graph: {hasPath(src, dest, Directed_graph)}")

src = "a"
dest = "f"
vis = set()
print(f"\nPath exists from {src} to {dest} in Undirected Graph: {Undirected_HasPath(src, dest, Undirected_graph, vis)}")
