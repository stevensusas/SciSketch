import IconMappingDictionary

Steps_mapping = IconMappingDictionary.IconMappingDictionary()

Steps_mapping.add_key_value('Preparation of wild-type and ASH1L-depleted astrocyte cultures', 'Cell Culture')
Steps_mapping.add_key_value('Exposure of astrocyte cultures to PBS (control), LPS, and Poly(I:C)', 'Treatment')
Steps_mapping.add_key_value('Isolation of RNA from treated astrocytes', 'Sample Extraction')
Steps_mapping.add_key_value('Conversion of RNA to cDNA', 'Kits')
Steps_mapping.add_key_value('Quantification of IL6 and TNF expression using RT-qPCR', 'qPCR')

Objects_mapping = IconMappingDictionary.IconMappingDictionary()

Objects_mapping.add_key_value('Wild-type astrocytes', 'Cell Model')
Objects_mapping.add_key_value('ASH1L-depleted astrocytes', 'Cell Culture')
Objects_mapping.add_key_value('PBS', 'Experimental Reagent')
Objects_mapping.add_key_value('LPS', 'Solution')
Objects_mapping.add_key_value('Poly(I:C)', 'Small Molecule')
Objects_mapping.add_key_value('RNA Isolation Kit', 'Kits')
Objects_mapping.add_key_value('Reverse Transcription Reagents', 'Master Icon DB')
Objects_mapping.add_key_value('RT-qPCR Reagents (including IL6 and TNF specific primers)', 'Kits')