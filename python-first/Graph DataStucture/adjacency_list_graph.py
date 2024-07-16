class GraphAdjList:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, src, dest):
        if src in self.graph and dest in self.graph:
            self.graph[src].append(dest)

    def remove_edge(self, src, dest):
        if src in self.graph and dest in self.graph[src]:
            self.graph[src].remove(dest)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for edges in self.graph.values():
                if vertex in edges:
                    edges.remove(vertex)

    def dfs(self, source):
        visited = set()
        stack = [source]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbour in self.graph[node]:
                    if neighbour not in visited:
                        stack.append(neighbour)
        return result

    def bfs(self, source):
        visited = set()
        queue = [source]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbour in self.graph[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        return result

    def has_path_dfs(self, src, dest):
        visited = set()

        def dfs(v):
            if v == dest:
                return True
            visited.add(v)
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False

        return dfs(src)

    def has_path_bfs(self, src, dest):
        visited = set()
        queue = [src]

        while queue:
            node = queue.pop(0)
            if node == dest:
                return True
            if node not in visited:
                visited.add(node)
                for neighbour in self.graph[node]:
                    queue.append(neighbour)
        return False

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Example usage:
g = GraphAdjList()
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")
g.add_edge("a", "b")
g.add_edge("a", "d")
g.add_edge("d", "c")
g.display()
print("DFS:", g.dfs("a"))
print("BFS:", g.bfs("a"))
print("Has path DFS (a to c):", g.has_path_dfs("a", "c"))
print("Has path BFS (a to c):", g.has_path_bfs("a", "c"))
