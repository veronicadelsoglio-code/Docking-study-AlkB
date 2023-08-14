# Veronica Delsoglio
# date: 02.2022
# THIS SCRIPT: calcolates the distances between:
# terminal C6 - FI2   one terminal atom of esane is C6
# terminal C6 - FI3
# terminal C5 - FI2   the other terminal atom of esane is C5
# terminal C5 - FI3
# and find the ones HIGHER or SMALLER than a certain distance

#!/usr/bin/env python
# coding: utf-8
#import libraries


import Bio.PDB
from Bio.PDB import *
import os

import numpy as np
import pathlib
import glob
import pandas as pd
import seaborn as sns
import matplotlib as plt

                                    ### CARBON C6
### FIRST FILE for FI2 - C6 distances measurements
file1 = open('PROVA', 'w')
header = str('distances' + '\n' )
file1.writelines(header)

#open PDB files18 (https://stackoverflow.com/questions/38991923/how-to-open-multiple-files-in-a-directory)
Path = "/home/veronica/Cluster/January2022/KOURIST/GA_ligand_dock_script/Script_2/Docking_Output_Files"
filelist = os.listdir(Path)
for x in filelist:
    if x.endswith(".pdb"):
        with open (x) as fout:
            for riga in fout:
                if riga.startswith("HETATM") and riga.split()[3] == "FI2":
                    coord_a1 = float(riga.split()[6])
                    coord_b1 = float(riga.split()[7])
                    coord_c1 = float(riga.split()[8])
                    FE_atom1 = np.array([coord_a1, coord_b1, coord_c1])

                if riga.startswith("HETATM") and riga.split()[2]== "C6":
                    coord_a2 = float(riga.split()[6])
                    coord_b2 = float(riga.split()[7])
                    coord_c2 = float(riga.split()[8])
                    C6_atom = np.array([coord_a2, coord_b2, coord_c2])

                    dist_FI2_C6 = np.linalg.norm((FE_atom1 - C6_atom))
                    file1.write(str(dist_FI2_C6) + '\n')
                    lists = list(dist_FI2_C6)
            #x = 0
            #while dist_FI2_C6 >
file1.close()
