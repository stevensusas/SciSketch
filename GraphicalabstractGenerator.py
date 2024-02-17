
#This methods returns graph as the output
def generate_graphical_abstract(Abstract):
  from openai import OpenAI
  from dotenv import load_dotenv
  import Graph
  import re
  load_dotenv()

  import os
  client = OpenAI(
    api_key= os.environ.get('mykey')
  )


  completion = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": "identify a list of entities in this science abstract and their relations, storing the list of entities as an array of three element tuple of strings and the relations as an array of tuples in the format of (Entity A, Entity B, Relationship):" + Abstract},
    ],
  )

  message = completion.choices[0].message.content

  print(message)

  entities_output = re.findall(r'\d+\.\s+(.*)', message)

  entities = []
  relations = []

  for item in entities_output:
      if item.startswith('(') and item.endswith(')'):
          # Remove the parentheses and split by commas
          relation = tuple(item[1:-1].split(', '))
          relations.append(relation)

  print(relations)

  relations_filtered = [item for item in relations if len(item) <= 3]

  graph = Graph.Graph()

  for relation in relations_filtered:
      entity_a, entity_b, annotation = relation
      graph.add_vertex(entity_a)
      graph.add_vertex(entity_b)
      graph.add_edge(entity_a, entity_b, annotation)

  graph.display()
  return graph

  #graph is the final output of this program