from openai import OpenAI
from dotenv import load_dotenv
#import Graph
import re
load_dotenv()

import os

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def build_tree():
    object_tree = TreeNode("Object")

    object_layer1 = ["Molecule", "Experimental Reagent", "Cell & Animal Models", "Disease/Condition"]
    object_tree.children = [TreeNode(name) for name in object_layer1]

    molecule_layer1 = ["DNA/RNA", "Protein", "Small Molecule"]
    object_tree.children[0].children = [TreeNode(name) for name in molecule_layer1]

    experimental_reagent_layer1 = ["Kits", "Solution", "Cell Model", "Small Molecule"]
    object_tree.children[1].children = [TreeNode(name) for name in experimental_reagent_layer1]

    cell_animal_models_layer1 = ["Cell Line", "Animal Model"]
    object_tree.children[2].children = [TreeNode(name) for name in cell_animal_models_layer1]

    disease_condition_layer1 = ["Neurological Disease", "Other Disease"]
    object_tree.children[3].children = [TreeNode(name) for name in disease_condition_layer1]

    action_tree = TreeNode("Action")

    action_layer1 = ["Cell Culturing", "Treatment", "Sample Extraction", "Molecular Biology Experiment"]
    action_tree.children = [TreeNode(name) for name in action_layer1]

    molecular_biology_experiment_layer1 = ["Western Blot", "qPCR"]
    action_tree.children[3].children = [TreeNode(name) for name in molecular_biology_experiment_layer1]

    master_icon_db = TreeNode("Master Icon DB")
    master_icon_db.children = [object_tree, action_tree]

    return master_icon_db

def get_completion(word, prompt, model="gpt-4-0125-preview"):
    client = OpenAI(
    api_key = "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"
    )
    
    messages = [
            {f"Is '{word}' a {prompt}? For example, if it is an action, simply answer 'action'. Please be conservative in your answer. If you are not very sure if the given word belongs to any classification, answer 'none'. Thanks!"}
            ]
    response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message["content"]

def classify_word(word, node):
    # Query ChatGPT to classify the word against each child node's description
    
    if not node.children:
        return node.name

    prompt = " "

    for child in node.children:
        prompt += child.name
        prompt += ", or, "

    response = get_completion(word, prompt)

    for child in node.children:
        if child.name == response:
            classify_word(word, child)

    # If no match found among children, return the node's name
    return "none"


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Classify a word based on a tree structure using ChatGPT")
    # parser.add_argument("word", type=str, help="The word to classify")
    # args = parser.parse_args()

    tree = build_tree()
    classification = classify_word("protein", tree)

    print(f"The word 'protein' is classified as: {classification}")
    
