# Veronica Delsoglio
# date: 05.2022
# THIS SCRIPT: extrapolates the score values of the docked ligands from the docking .pdb outputs

#!/usr/bin/env python
# coding: utf-8
#import libraries

import Bio.PDB
from Bio.PDB import *
import os
import weblogo
import numpy as np
import pathlib
import glob
import pandas as pd
import seaborn as sns
import matplotlib as plt

# Open a new file where to save the values

ligand_score = open('ligand_score.csv', 'w')
header = str('score_ligand' + '\n' )
ligand_score.writelines(header)

#  Open all the docking pdb outputs

Path = "/home/veronica/Cluster/2022/January2022/KOURIST/GA_ligand_dock_script/Script_2"
filelist = os.listdir(Path)
for pdb in filelist:
    if pdb.endswith(".pdb"):
        with open (pdb) as fout:

# Reading through the text of each pdb file selecting the one of interest
            for line in fout:
                if line.startswith("LG1_404"):
                    LG1_score = float( line [29])
                    print("LG1_score: ", line [29])

            ligand_score.write(LG1_score)
ligand_score.close()
 
