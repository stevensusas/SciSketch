
import sys
import json
from openai import OpenAI
from dotenv import load_dotenv
import Graph 
import re
import os


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
                  {"role": "user", "content": "identify a list of entities in this science abstract and their relations, storing the list of entities as an array of three element tuple of strings and the relations as an array of tuples in the format of (Entity A, Entity B, Relationship):" + abstract},
                ],
            )

            message = completion.choices[0].message.content
            # print(message) 

            entities_output = re.findall(r'\d+\.\s+(.*)', message)

            relations = [tuple(item[1:-1].split(', ')) for item in entities_output if item.startswith('(') and item.endswith(')')]

            graph = Graph.Graph()

            for relation in relations:
                if len(relation) == 3:
                    entity_a, entity_b, annotation = relation
                    graph.add_vertex(entity_a)
                    graph.add_vertex(entity_b)
                    graph.add_edge(entity_a, entity_b, annotation)

            # graph.display()  # This will print the graph representation

            success = True 
            return json.dumps(graph.adjacency_list)

        except Exception as e:
            # print(f"Attempt {attempt + 1} failed with error: {e}")
            attempt += 1  # Increment the attempt counter and try again

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python GraphicalAbstractGenerator.py 'Your abstract here'")
    else:
        abstract = sys.argv[1]
        print(get_graph_from_abstract(abstract))

# "abstract":"Neurodegenerative diseases are characterized by the formation and propagation of protein aggregates, especially amyloid fibrils. However, what normally suppresses protein misfolding and aggregation in metazoan cells remains incompletely understood. Here, we show that TRIM11, a member of the metazoan tripartite motif (TRIM) family, both prevents the formation of protein aggregates and dissolves pre-existing protein deposits, including amyloid fibrils. These molecular chaperone and disaggregase activities are ATP independent. They enhance folding and solubility of normal proteins and cooperate with TRIM11 SUMO ligase activity to degrade aberrant proteins. TRIM11 abrogates α-synuclein fibrillization and restores viability in cell models of Parkinson's disease (PD). Intracranial adeno-associated viral delivery of TRIM11 mitigates α-synuclein-mediated pathology, neurodegeneration, and motor impairments in a PD mouse model. Other TRIMs can also function as ATP-independent molecular chaperones and disaggregases. Thus, we define TRIMs as a potent and multifunctional protein quality-control system in metazoa, which might be applied to treat neurodegenerative diseases."