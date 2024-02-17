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

    max_attempts = 5
    attempt = 0
    success = False
    data = {"error": "Failed to process the protocol after multiple attempts."}

    while not success and attempt < max_attempts:
        try:
            completion = client.chat.completions.create(
              model="gpt-4-0125-preview",
              messages=[
                {"role": "user", "content": "Identify the key steps and reagents/objects used in this biological experiment procedure, and generate two python arrays that store respectively strings describing the key steps and another python array that stores the reagents/objects " + protocol},
              ],
            )

            message = completion.choices[0].message.content
            # print(message)  # Optional: For debugging purposes

            steps_match = re.search(r'steps = (\[.*?\])', message, re.DOTALL)
            reagents_objects_match = re.search(r'reagents_objects = (\[.*?\])', message, re.DOTALL)

            if steps_match and reagents_objects_match:
                steps_array = ast.literal_eval(steps_match.group(1))
                reagents_objects_array = ast.literal_eval(reagents_objects_match.group(1))
                data = {"steps": steps_array, "reagents_objects": reagents_objects_array}
                success = True

                return json.dumps(data)
            else:
                attempt += 1
                # print(f"Attempt {attempt}: Failed to find matches. Retrying...")  # Optional: For debugging purposes
        except Exception as e:
            attempt += 1
            # print(f"Attempt {attempt}: Error occurred - {str(e)}. Retrying...")  # Optional: For debugging purposes

    return json.dumps(data)

if __name__ == "__main__":
    import sys
    protocol = " ".join(sys.argv[1:])
    print(process_sequential_protocol(protocol))
    # print(result)  # Ensure the output is printed or logged
