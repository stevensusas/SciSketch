import Graph as Graph
from graphviz import Digraph

def generate_graph_with_images(adjacency_list, entity_images):
    dot = Digraph(comment='Graph Visualization', format='png')
    dot.attr('node', shape='plaintext')  # Use plaintext for HTML-like labels

    # Define standard image width and height (in inches)
    image_width = "0.5"
    image_height = "0.5"
    
    for entity in adjacency_list.keys():
        if entity in entity_images:
            # Create an HTML-like label combining the image with standardized size and the entity name
            label = f'''<
                <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
                  <TR>
                    <TD><IMG SRC="{entity_images[entity]}" WIDTH="{image_width}" HEIGHT="{image_height}"/></TD>
                  </TR>
                  <TR>
                    <TD>{entity}</TD>
                  </TR>
                </TABLE>
            >'''
            dot.node(entity, label=label)
        else:
            # Fallback for entities without images
            dot.node(entity, entity)

    for source, targets in adjacency_list.items():
        for target, annotation in targets:
            dot.edge(source, target, label=annotation)

    output_path = 'graph-output/graph'
    dot.render(output_path, cleanup=True)
    return output_path + '.png'

if __name__ == "__main__":
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

    images = {
        "TRIM11": "../assets/DNA:RNA.png",
        "metazoan tripartite motif family": "../assets/Protein.png",
        "protein aggregates": "../assets/Molecule.png",
        "amyloid fibrils": "../assets/Small Molecule.png",
        "normal proteins": "../assets/Protein.png",
        "SUMO ligase activity": "../assets/Protein.png",
        "aberrant proteins": "../assets/Molecule.png",
        "α-synuclein": "../assets/Small Molecule.png",
        "Parkinson's disease": "../assets/Neurological Disease.png"
    }
    graph_image_path = generate_graph_with_images(graph.adjacency_list, images)
    print(graph_image_path)