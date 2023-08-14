# Veronica Delsoglio
# date: 02.2022
# THIS SCRIPT: calcolates the distances between the terminal atom C6 of a ligand and respectively 2 FE atoms in the binding pocket

#!/usr/bin/env python
# coding: utf-8

# import libraries

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

file = open('results.txt', 'w')

#open PDB files18 (https://stackoverflow.com/questions/38991923/how-to-open-multiple-files-in-a-directory)
Path = "/home/veronica/Cluster/January2022/KOURIST/GA_ligand_dock_script/Script_1/RepackMinimise/"
filelist = os.listdir(Path)
for x in filelist:
    if x.endswith(".pdb"):
        # open every single pdb file present in the list
        with open (x) as fout:
            for riga in fout:
                # IMP: substraction of the respective points coordiantes
                if riga.startswith("HETATM") and riga.split()[3] == "FI2":
                    coord_a1 = float(riga.split()[6])
                    coord_b1 = float(riga.split()[7])
                    coord_c1 = float(riga.split()[8])
                    FE_atom1 = np.array([coord_a1, coord_b1, coord_c1])
                    #print(FE_atom)

                if riga.startswith("HETATM") and riga.split()[3]=="FI3":
                    coord_A1 = float(riga.split()[6])
                    coord_B1 = float(riga.split()[7])
                    coord_C1 = float(riga.split()[8])
                    FE_atom2 = np.array([coord_A1, coord_B1, coord_C1])

                if riga.startswith("HETATM") and riga.split()[2]=="C6":
                    coord_a2 = float(riga.split()[6])
                    coord_b2 = float(riga.split()[7])
                    coord_c2 = float(riga.split()[8])
                    C6_atom = np.array([coord_a2, coord_b2, coord_c2])
                    #print(C6_atom)


                    # numpy linear algebra
                    dist_FI2_C6 = np.linalg.norm((FE_atom1 - C6_atom))
                    dist_FI3_C6 = np.linalg.norm((FE_atom2 - C6_atom))

                    print(x)
                    print("dist_FI2_C6: ", dist_FI2_C6)
                    print("dist_FI3_C6: ", dist_FI3_C6)

                    file.write(str(x) + '\n')
                    file.write("dist_FI2_C6: " + str(dist_FI2_C6) + '\n')
                    file.write("dist_FI3_C6: " + str(dist_FI3_C6) + '\n')

file.close()

            # write output file with saved distances
                #with open ('results.txt', 'w') as f:
                #    f.write(str(x))
                    #f.write(str(dist_FI2_C6))
                    #f.write(str(dist_FI3_C6))
