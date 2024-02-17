

#this method returns steps_array and reagents_objects_array
def getExperimentalProcedure(Protocol):

  from openai import OpenAI
  from dotenv import load_dotenv
  import Graph
  import re
  load_dotenv()

  import os
 
  client = OpenAI(
    api_key= os.environ.get('mykey')
  )

  #Protocol goes here

  completion = client.chat.completions.create(
    model= "gpt-4-0125-preview",
    messages=[
      {"role": "user", "content": "Identify the key steps and reagents/objects used in this biological experiment procedure, and generate two python arrays that store respectively strings describing the key steps and another python array that stores the reagents/objects "+ Protocol},
    ],
  )



  message = completion.choices[0].message.content

  #print(message)

  steps_match = re.search(r'steps = (\[.*?\])', message, re.DOTALL)
  reagents_objects_match = re.search(r'reagents_objects = (\[.*?\])', message, re.DOTALL)

  if steps_match and reagents_objects_match:
      steps_array = eval(steps_match.group(1))
      reagents_objects_array = eval(reagents_objects_match.group(1))
      print("Steps array:", steps_array)
      print("Reagents/objects array:", reagents_objects_array)
  else:
      print("Arrays not found in the output")

  return (steps_array, reagents_objects_array)
  #steps_array and reagents_objects_array are the final output of this script