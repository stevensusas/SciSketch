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

    output_path = 'graph-output/procedure'
    dot.render(output_path, cleanup=True)
    return output_path + '.png'


if __name__ == "__main__":
    graph = Graph.Graph()

    steps_array = ['Preparation of wild-type and ASH1L-depleted astrocyte cultures', 'Exposure of astrocyte cultures to PBS (control), LPS, and Poly(I:C)', 'Isolation of RNA from treated astrocytes', 'Conversion of RNA to cDNA', 'Quantification of IL6 and TNF expression using RT-qPCR']

    reagents_objects_array = ['wild-type astrocytes', 'ASH1L-depleted astrocytes', 'PBS', 'LPS', 'Poly(I:C)', 'RNA', 'cDNA', 'RT-qPCR reagents']

    for vertex in steps_array:
        graph.add_vertex(vertex)

    # for vertex in reagents_objects_array:
    #     graph.add_vertex(vertex)

    edges = [
        ("Preparation of wild-type and ASH1L-depleted astrocyte cultures", "Exposure of astrocyte cultures to PBS (control), LPS, and Poly(I:C)", ""),
        ("Exposure of astrocyte cultures to PBS (control), LPS, and Poly(I:C)", "Isolation of RNA from treated astrocytes", ""),
        ("Isolation of RNA from treated astrocytes", "Conversion of RNA to cDNA", ""),
        ("Conversion of RNA to cDNA", "Quantification of IL6 and TNF expression using RT-qPCR", "")
        ]
    
    for edge in edges:
        graph.add_edge(*edge)

    images = {
        "Preparation of wild-type and ASH1L-depleted astrocyte cultures": "../assets/Cell Culture.png",
        "Exposure of astrocyte cultures to PBS (control), LPS, and Poly(I:C)": "../assets/Treatment.png",
        "Isolation of RNA from treated astrocytes": "../assets/Sample Extraction.png",
        "Conversion of RNA to cDNA": "../assets/Kits.png",
        "Quantification of IL6 and TNF expression using RT-qPCR": "../assets/qPCR.png",
        "wild-type astrocytes": "../assets/Cell Model.png",
        "ASH1L-depleted astrocytes": "../assets/Cell Culture.png",
        "PBS": "../assets/Experimental Reagent.png",
        "LPS": "../assets/Solution.png",
        "Poly(I:C)": "../assets/Small Molecule.png",
        "RNA": "../assets/Kits.png",
        "cDNA": "../assets/Master Icon DB.png",
        "RT-qPCR reagents": "../assets/Kits.png"
    }

    graph_image_path = generate_graph_with_images(graph.adjacency_list, images)
    print(graph_image_path)


