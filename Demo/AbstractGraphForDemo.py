import Graph

graph = Graph.Graph()

# Add vertices
vertices = [
    "TRIM11", "metazoan tripartite motif family", "protein aggregates",
    "amyloid fibrils", "normal proteins", "SUMO ligase activity",
    "aberrant proteins", "α-synuclein", "Parkinson's disease"
]
for vertex in vertices:
    graph.add_vertex(vertex)

# Add edges
edges = [
    ("TRIM11", "metazoan tripartite motif family", "member"),
    ("TRIM11", "protein aggregates", "prevents formation"),
    ("TRIM11", "protein aggregates", "dissolves pre-existing"),
    ("TRIM11", "amyloid fibrils", "dissolves"),
    ("TRIM11", "normal proteins", "enhances folding and solubility"),
    ("TRIM11", "SUMO ligase activity", "cooperates with"),
    ("TRIM11", "aberrant proteins", "degrades"),
    ("TRIM11", "α-synuclein", "abrogates fibrillization"),
    ("TRIM11", "Parkinson's disease", "restores viability in cell models")
]
for edge in edges:
    graph.add_edge(*edge)

# Display the graph
graph.display()