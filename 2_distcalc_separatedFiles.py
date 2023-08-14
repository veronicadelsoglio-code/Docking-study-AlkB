# Veronica Delsoglio
# date: 02.2022
# THIS SCRIPT: calcolates the distances between:
# terminal C6 - FI2   one terminal atom of esane is C6
# terminal C6 - FI3
# terminal C5 - FI2   the other terminal atom of esane is C5
# terminal C5 - FI3

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

                                          ### CARBON C6
                             ### FIRST FILE for FI2 - C6 distances measurements
file1 = open('results_FI2_C6.csv', 'w')
header = str('distances' + '\n' )
file1.writelines(header)

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


                if riga.startswith("HETATM") and riga.split()[2]=="C6":
                    coord_a2 = float(riga.split()[6])
                    coord_b2 = float(riga.split()[7])
                    coord_c2 = float(riga.split()[8])
                    C6_atom = np.array([coord_a2, coord_b2, coord_c2])

                    # numpy linear algebra
                    dist_FI2_C6 = np.linalg.norm((FE_atom1 - C6_atom))


                    print(dist_FI2_C6)
                    file1.write(str(dist_FI2_C6) + '\n')

file1.close()

                                      ### CARBON 6 ###
                       ### SECOND FILE for FI3 - C6 distances measurements
file2 = open('results_FI3_C6.csv', 'w')
header = str('distances' + '\n' )
file2.writelines(header)
#open PDB files18 (https://stackoverflow.com/questions/38991923/how-to-open-multiple-files-in-a-directory)
Path = "/home/veronica/Cluster/January2022/KOURIST/GA_ligand_dock_script/Script_1/RepackMinimise/"
filelist = os.listdir(Path)
for x in filelist:
    if x.endswith(".pdb"):
        # open every single pdb file present in the list
        with open (x) as fout:
            for riga in fout:
                # IMP: substraction of the respective points coordiantes
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


                    dist_FI3_C6 = np.linalg.norm((FE_atom2 - C6_atom))

                    print(dist_FI3_C6)
                    file2.write(str(dist_FI3_C6) + '\n')

file2.close()





                                     ### CARBON 5 ###
                      ### FIRST FILE for FI2 - C5 distances measurements
file3 = open('results_FI2_C5.csv', 'w')
header = str('distances' + '\n' )
file3.writelines(header)
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


                if riga.startswith("HETATM") and riga.split()[2]=="C5":
                    coord_a2 = float(riga.split()[6])
                    coord_b2 = float(riga.split()[7])
                    coord_c2 = float(riga.split()[8])
                    C5_atom = np.array([coord_a2, coord_b2, coord_c2])

                    # numpy linear algebra
                    dist_FI2_C5 = np.linalg.norm((FE_atom1 - C5_atom))


                    print(dist_FI2_C5)
                    file3.write(str(dist_FI2_C5) + '\n')

file3.close()

                                    ### CARBON 5 ###
                   ### SECOND FILE for FI3 - C5 distances measurements
file4 = open('results_FI3_C5.csv', 'w')
header = str('distances' + '\n' )
file4.writelines(header)
#open PDB files18 (https://stackoverflow.com/questions/38991923/how-to-open-multiple-files-in-a-directory)

Path = "/home/veronica/Cluster/January2022/KOURIST/GA_ligand_dock_script/Script_1/RepackMinimise/"
filelist = os.listdir(Path)
for x in filelist:
    if x.endswith(".pdb"):
        # open every single pdb file present in the list
        with open (x) as fout:
            for riga in fout:
                # IMP: substraction of the respective points coordiantes
                if riga.startswith("HETATM") and riga.split()[3]=="FI3":
                    coord_A1 = float(riga.split()[6])
                    coord_B1 = float(riga.split()[7])
                    coord_C1 = float(riga.split()[8])
                    FE_atom2 = np.array([coord_A1, coord_B1, coord_C1])


                if riga.startswith("HETATM") and riga.split()[2]=="C5":
                    coord_a2 = float(riga.split()[6])
                    coord_b2 = float(riga.split()[7])
                    coord_c2 = float(riga.split()[8])
                    C5_atom = np.array([coord_a2, coord_b2, coord_c2])


                    dist_FI3_C5 = np.linalg.norm((FE_atom2 - C5_atom))

                    print(dist_FI3_C5)
                    file4.write(str(dist_FI3_C5) + '\n')

file4.close()
