class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, annotation):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append((vertex2, annotation))
            self.adjacency_list[vertex2].append((vertex1, annotation))

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            for i, (vertex, annotation) in enumerate(self.adjacency_list[vertex1]):
                if vertex == vertex2:
                    del self.adjacency_list[vertex1][i]
                    break
            for i, (vertex, annotation) in enumerate(self.adjacency_list[vertex2]):
                if vertex == vertex1:
                    del self.adjacency_list[vertex2][i]
                    break

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for adjacent_vertex, _ in self.adjacency_list[vertex]:
                self.adjacency_list[adjacent_vertex] = [(v, a) for v, a in self.adjacency_list[adjacent_vertex] if v != vertex]
            del self.adjacency_list[vertex]

    def get_annotation(self, vertex1, vertex2):
        for vertex, annotation in self.adjacency_list[vertex1]:
            if vertex == vertex2:
                return annotation
        return None

    def is_empty(self):
        return len(self.adjacency_list) == 0
    
    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")
