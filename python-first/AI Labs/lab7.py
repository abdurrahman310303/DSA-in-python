
# Write a Python code to implement an undirected graph using an adjacency list and 
# perform the following operations:
# a. Add a vertex to the graph.
# b. Add an edge between two vertices.
# c. Remove an edge between two vertices.
# d. Check if there is a path between two vertices.
# e. Print all the vertices and their corresponding adjacent vertices.
# Make sure to include the necessary functions and data structures to support the 
# operations mentioned above

import networkx as nx
import matplotlib.pyplot as plt

class Graph_LAB7:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 not in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].append(vertex2)
            if vertex1 not in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def has_path(self, vertex1, vertex2):
        visited = set()

        def dfs(current_vertex):
            if current_vertex == vertex2:
                return True
            visited.add(current_vertex)
            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(vertex1)

    def print_graph(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex}: {neighbors}")

    def plot_graph(self):
        G = nx.Graph()
        for vertex, neighbors in self.adjacency_list.items():
            G.add_node(vertex)
            for neighbor in neighbors:
                G.add_edge(vertex, neighbor)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
        plt.show()

# Example usage
graph = Graph_LAB7()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('D', 'C')

graph.plot_graph()
