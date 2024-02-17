import TreeNode

object_tree = TreeNode.TreeNode("Object")

object_layer1 = ["Molecule", "Experimental Reagent", "Cell & Animal Models", "Disease/Condition"]

object_tree.add_child_array(object_layer1)

Molecule_layer1 = ["DNA/RNA", "Protein", "Small Molecule"]

object_tree.get_child("Molecule").add_child_array(Molecule_layer1)

Experimental_Reagent_layer1 = ["Kits", "Solution", "Cell Model", "Small Molecule"]

object_tree.get_child("Experimental Reagent").add_child_array(Experimental_Reagent_layer1)

Cell_Animal_Models_layer1 = ["Cell Line", "Animal Model"]

object_tree.get_child("Cell & Animal Models").add_child_array(Cell_Animal_Models_layer1)

action_tree = TreeNode.TreeNode("Action")

action_layer1 = ["Cell Culturing", "Treatment", "Sample Extraction", "Molecular Biology Experiment"]

Molecular_Biology_Experiment_layer1 = ["Western Blot", "qPCR"]

action_tree.add_child_array(action_layer1)

action_tree.get_child("Molecular Biology Experiment").add_child_array(Molecular_Biology_Experiment_layer1)

Disease_Condition_layer1 = ["Neurological Disease", "Other Disease"]

object_tree.get_child("Disease/Condition").add_child_array(Disease_Condition_layer1)

Master_Icon_DB = TreeNode.TreeNode("Master Icon DB")

Master_children_array = ["Object", "Action"]

Master_Icon_DB.add_children(Master_children_array)
