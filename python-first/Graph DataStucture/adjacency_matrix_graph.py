class GraphAdjMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        self.graph[src][dest] = 1

    def remove_edge(self, src, dest):
        self.graph[src][dest] = 0

    def dfs(self, source):
        visited = [False] * self.num_vertices
        stack = [source]
        result = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                result.append(node)
                for i in range(self.num_vertices):
                    if self.graph[node][i] == 1 and not visited[i]:
                        stack.append(i)
        return result

    def bfs(self, source):
        visited = [False] * self.num_vertices
        queue = [source]
        result = []

        while queue:
            node = queue.pop(0)
            if not visited[node]:
                visited[node] = True
                result.append(node)
                for i in range(self.num_vertices):
                    if self.graph[node][i] == 1 and not visited[i]:
                        queue.append(i)
        return result

    def has_path_dfs(self, src, dest):
        visited = [False] * self.num_vertices

        def dfs(v):
            if v == dest:
                return True
            visited[v] = True
            for i in range(self.num_vertices):
                if self.graph[v][i] == 1 and not visited[i]:
                    if dfs(i):
                        return True
            return False

        return dfs(src)

    def has_path_bfs(self, src, dest):
        visited = [False] * self.num_vertices
        queue = [src]

        while queue:
            node = queue.pop(0)
            if node == dest:
                return True
            if not visited[node]:
                visited[node] = True
                for i in range(self.num_vertices):
                    if self.graph[node][i] == 1 and not visited[i]:
                        queue.append(i)
        return False

    def display(self):
        for row in self.graph:
            print(row)

# Example usage:
g = GraphAdjMatrix(4)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(3, 2)
g.display()
print("DFS:", g.dfs(0))
print("BFS:", g.bfs(0))
print("Has path DFS (0 to 2):", g.has_path_dfs(0, 2))
print("Has path BFS (0 to 2):", g.has_path_bfs(0, 2))
