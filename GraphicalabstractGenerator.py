import sys
import json
import os
from graphviz import Digraph
from openai import OpenAI
from dotenv import load_dotenv
import Graph 
import re

def get_graph_from_abstract(abstract):
    load_dotenv()
    client = OpenAI(
      api_key=os.environ.get('mykey')
    )
    attempt = 0
    max_attempts = 5
    success = False

    while not success and attempt < max_attempts:
        try:
            completion = client.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=[
                  {"role": "user", "content": "identify a list of entities in this science abstract and their relations, storing the list of entities as an array of three element tuple of strings and the relations as an array of tuples in the format of (Entity A, Entity B, Relationship), do not add quotation marks around entity and relationship:" + abstract},
                ],
            )

            message = completion.choices[0].message.content
            entities_output = re.findall(r'\d+\.\s+(.*)', message)
            relations = [tuple(item[1:-1].split(', ')) for item in entities_output if item.startswith('(') and item.endswith(')')]

            graph = Graph.Graph()
            for relation in relations:
                if len(relation) == 3:
                    entity_a, entity_b, annotation = relation
                    graph.add_vertex(entity_a)
                    graph.add_vertex(entity_b)
                    graph.add_edge(entity_a, entity_b, annotation)

            success = True 
            return graph.adjacency_list

        except Exception as e:
            attempt += 1

    return None

def generate_graph_with_images(adjacency_list, entity_images):
    dot = Digraph(comment='Graph Visualization', format='png')
    
    for entity in adjacency_list.keys():
        if entity in entity_images:
            dot.node(entity, label='', image=entity_images[entity], shape='none')
        else:
            dot.node(entity, entity)

    for source, targets in adjacency_list.items():
        for target, annotation in targets:
            dot.edge(source, target, label=annotation)

    output_path = 'graph-output/graph'
    dot.render(output_path, cleanup=True)
    return output_path + '.png'

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py 'Your abstract here'")
    else:
        abstract = sys.argv[1]
        adjacency_list = get_graph_from_abstract(abstract)
        if adjacency_list:
            # Assume entity_images is defined somewhere, or pass an empty dict if not available
            entity_images = {"Neurodegenerative diseases": "./assets/Neurodegenerative diseases.jpeg",}  # Example: {"EntityName": "path/to/image.png"}
            graph_image_path = generate_graph_with_images(adjacency_list, entity_images)
            print(graph_image_path)
        else:
            print("Failed to generate graph from abstract.")
