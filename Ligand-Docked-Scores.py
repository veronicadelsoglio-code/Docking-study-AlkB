# Veronica Delsoglio
# date: 05.2022
# THIS SCRIPT: extrapolates the score values of the docked ligands from the docking .pdb outputs

#!/usr/bin/env python
# coding: utf-8
#import libraries

# NOTE: 2 main files can be generated: ligand_score (scores + names of the pdb) or just_ligscore (just score values to make analysis with dataframe)
# select or deselect the one of interest (line 25,26,29,30,46,47,48,49)  depending on which file you want to use


import Bio.PDB
from Bio.PDB import *
import os
import numpy as np
import pathlib
import glob
import pandas as pd
import seaborn as sns
import matplotlib as plt

# Open a new file where to save the values
name_structure= open("name_pdb.csv", "w")
#ligand_score = open('ligand_score.csv', 'w')
#just_ligscores = open("just_ligscore", "w")
header = str("name_pdb" + '\n')
#header = str('score_ligand' + "name_file" + '\n' )
#ligand_score.writelines(header)
name_structure.writelines(header)
#just_ligscores.writelines(header)

#  Open all the docking pdb outputs

Path = "/home/veronica/Cluster/2022/May2022/KOURIST/IsoprenylAcetate/Docking_Script02/Docking_secondTime/Ligand_analysis/"
filelist = os.listdir(Path)
for pdb in filelist:
    if pdb.endswith(".pdb"):
        with open (pdb) as fout:
        
# Reading through the text of each pdb file selecting the one of interest
            for line in fout:
                if line.startswith("LG1_404"):
                   # print(line)
                    LG1_score = line.split() [-1]
                    #print(LG1_score)
                    #print("LG1_score: ", line.split() [-1])
                    print(str(pdb))
                    name_structure.write(str(pdb) + '\n')
                    #ligand_score.write(LG1_score + '\t'+ str(pdb) + '\n')
#                    just_ligscores.write(LG1_score + '\n')
#ligand_score.close()
#just_ligscores.close()
name_structure.close() 
