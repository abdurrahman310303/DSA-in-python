from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    # Add a vertex to the graph
    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    # Add an edge between two vertices
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    # Remove a vertex and all associated edges
    def remove_vertex(self, v):
        if v in self.graph:
            for node in list(self.graph):
                if v in self.graph[node]:
                    self.graph[node].remove(v)
            del self.graph[v]

    # Remove an edge between two vertices
    def remove_edge(self, u, v):
        if v in self.graph[u]:
            self.graph[u].remove(v)
        if u in self.graph[v]:
            self.graph[v].remove(u)

    # Depth-First Search (DFS)
    def dfs(self, start):
        visited = set()
        self._dfs_util(start, visited)
        return visited
    
    def _dfs_util(self, v, visited):
        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self._dfs_util(neighbour, visited)

    # Breadth-First Search (BFS)
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(self.graph[vertex]) - visited)
        return visited

    # Find all paths between two vertices
    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    # Find shortest path between two vertices using BFS
    def find_shortest_path(self, start, end):
        visited = {start: None}
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex == end:
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = visited[vertex]
                return path[::-1]
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited[neighbour] = vertex
                    queue.append(neighbour)
        return None

    # Print the graph
    def print_graph(self):
        for key, values in self.graph.items():
            print(f"{key}: {values}")

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.print_graph()
    print("DFS starting from A:", g.dfs("A"))
    print("BFS starting from A:", g.bfs("A"))
    print("All paths from A to C:", g.find_all_paths("A", "C"))
    print("Shortest path from A to C:", g.find_shortest_path("A", "C"))
    g.remove_edge("A", "B")
    g.print_graph()
    g.remove_vertex("C")
    g.print_graph()
