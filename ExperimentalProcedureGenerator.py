import os
import re
import json
import ast
from openai import OpenAI
from dotenv import load_dotenv

def process_sequential_protocol(protocol):
    load_dotenv()

    client = OpenAI(
      api_key=os.environ.get('mykey')
    )

    completion = client.chat.completions.create(
      model="gpt-4-0125-preview",
      messages=[
        {"role": "user", "content": "Identify the key steps and reagents/objects used in this biological experiment procedure, and generate two python arrays that store respectively strings describing the key steps and another python array that stores the reagents/objects " + protocol},
      ],
    )

    message = completion.choices[0].message.content

    steps_match = re.search(r'steps = (\[.*?\])', message, re.DOTALL)
    reagents_objects_match = re.search(r'reagents_objects = (\[.*?\])', message, re.DOTALL)

    if steps_match and reagents_objects_match:
        try:
            steps_array = ast.literal_eval(steps_match.group(1))
            reagents_objects_array = ast.literal_eval(reagents_objects_match.group(1))
            return json.dumps({"steps": steps_array, "reagents/objects": reagents_objects_array})
        except ValueError as e:
            return json.dumps({"error": f"Error processing the extracted data: {str(e)}"})
    else:
        return json.dumps({"error": "No steps or reagents/objects found in the response"})

if __name__ == "__main__":
    import sys
    protocol = " ".join(sys.argv[1:])
    print(process_sequential_protocol(protocol))
