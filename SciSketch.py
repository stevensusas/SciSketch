import classification
import ExperimentalProcedureGenerator
import GraphicalabstractGenerator
import TreeNode
import BuildTree
import IconMappingDictionary

Abstract = "Here, we show that TRIM11, a member of the metazoan tripartite motif (TRIM) family, both prevents the formation of protein aggregates and dissolves pre-existing protein deposits, including amyloid fibrils. These molecular chaperone and disaggregase activities are ATP independent. They enhance folding and solubility of normal proteins and cooperate with TRIM11 SUMO ligase activity to degrade aberrant proteins. TRIM11 abrogates α-synuclein fibrillization and restores viability in cell models of Parkinson's disease (PD). Intracranial adeno-associated viral delivery of TRIM11 mitigates α-synuclein-mediated pathology, neurodegeneration, and motor impairments in a PD mouse model."

Protocol = "We will expose wild-type astrocytes and ASH1L-depleted astrocytes to PBS (control), LPS, and Poly(I:C) in vitro. We will then use RT-qPCR to quantify the expression of IL6 and TNF, two pro-inflammatory cytokine encoding genes upregulated by astrocytes upon activation, in all samples [9]."

#Takes in Abstract/Procedure and return the graph/array and Icon-Picture Mapping Dictionary
def SciSketch(Option, Input):
    node = BuildTree.build_tree()

    if Option == "Abstract":
        Graph = GraphicalabstractGenerator.generate_graphical_abstract(Input)
        mapping = IconMappingDictionary.IconMappingDictionary()
        for item in Graph.get_vertex_list():
            mapping.add_key_value(item, classification.classify_word(item, node))
        
        print(Graph.display())
        print(mapping.display())
        return mapping
        

    elif Option == "Procedure":
        StepsArray, ReagentsArray = ExperimentalProcedureGenerator.getExperimentalProcedure(Input)
        Steps_mapping = IconMappingDictionary.IconMappingDictionary()
        for item in StepsArray:
            Steps_mapping.add_key_value(item, classification.classify_word(item, node))

        Reagents_mapping = IconMappingDictionary.IconMappingDictionary()
        for item in ReagentsArray:
            Reagents_mapping.add_key_value(item, classification.classify_word(item, node))

        print(StepsArray)
        print(ReagentsArray)
        print(Steps_mapping.display())
        print(Reagents_mapping.display())

        return (StepsArray, ReagentsArray, Steps_mapping, Reagents_mapping)
        
SciSketch("Abstract", Abstract)