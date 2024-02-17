from graphviz import Digraph
import os

def generate_graph_with_images(adjacency_list, entity_images):
    dot = Digraph(comment='Graph Visualization', format='png')
    
    # Iterate over entities to add nodes
    for entity in adjacency_list.keys():
        if entity in entity_images:
            # Entity has an associated image
            dot.node(entity, label='', image=entity_images[entity], shape='none')  # Use image for node
        else:
            # Fallback for entities without images
            dot.node(entity, entity)  # Use default shape and label the node with the entity name

    # Add edges with annotations
    for source, targets in adjacency_list.items():
        for target, annotation in targets:
            dot.edge(source, target, label=annotation)

    # Render the graph to a file (e.g., PNG)
    dot.render('graph-output/graph', cleanup=True)
    # print("Graph image generated at 'graph-output/graph.png'")

