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