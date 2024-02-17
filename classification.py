from openai import OpenAI
from dotenv import load_dotenv
#import Graph
import re
load_dotenv()
import BuildTree
import os

def get_completion(word, prompt, model="gpt-4-0125-preview"):
    client = OpenAI(
    api_key = "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"
    )
    
    completion = client.chat.completions.create(
    model= "gpt-4-0125-preview",
    messages=[
        {"role": "user", "content": "Is '{word}' a {prompt}? Give a one word response--the best fit, or none. For example, if it is an action, simply answer 'action'. Please be conservative in your answer. If you are not very sure if the given word belongs to any classification, answer 'none'. Give a one word response. Thanks!"}
            ],
  )
    
    message = completion.choices[0].message.content
    return message

def classify_word(word, node):
    # Query ChatGPT to classify the word against each child node's description
    if not node.children:
        return node.name
    prompt = ""

    for child in node.children:
        prompt += child.name
        prompt += ", or, "

    response = get_completion(word, prompt)

    for child in node.children:
        if child.name == response:
            classify_word(word, child)

    # If no match found among children, return the node's name
    return "none"
    
