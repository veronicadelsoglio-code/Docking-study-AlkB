# Veronica Delsoglio
# date: 04.2022
# THIS SCRIPT: finds uot the BP residues which are far from the
# respective FI2 and FI3 iron atoms of a certain distance

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

# OPEN A NEW FILE where to save all the distances

fileFI2_atom = open("fileFI2_atom.csv", "w")
header = str("distances" + '\n')
fileFI2_atom.writelines(header)

# OPEN THE PDB FILE and CALCULATE the distances between FI2 and all the atoms
# distances saved in a new file.

with open ("/home/veronica/Cluster/December2021/KOURIST/StrutturaFinale/AlkB_Fi2_Fi3_0001.pdb", "w") as pdbfile:
    for riga in pdbfile:
        if riga.startswith("HETATM") and riga.split()[3] =="FI2":
            coord_a1 = float(riga.split()[6])
            coord_b1 = float(riga.split()[7])
            coord_c1 = float(riga.split()[8])
            FE_atom1 = np.array([coord_a1, coord_b1, coord_c1])

        if riga.startswith("ATOM"):
            coord_A1 = float(riga.split()[6])
            coord_B1 = float(riga.split()[7])
            coord_C1 = float(riga.split()[8])
            atom = np.array([coord_A1, coord_B1, coord_C1])

            distanza_FI2_AtomoGenerico = np.linalg.norm((FE_atom1- atom))
            fileFI2_atom.write(str(distanza_FI2_AtomoGenerico))

fileFI2_atom.close()

#new file with saved distances opened. Sorted just the distances < = TOT

with open ("fileFI2_atom.csv", "w") as newfile:
    for riga in newfile:
        if riga = < float(11.0):
            print (riga)
