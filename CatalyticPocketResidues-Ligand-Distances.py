import Bio.PDB
from Bio.PDB import *
import os
import numpy as np
import pathlib
import glob
import pandas as pd
import seaborn as sns
import matplotlib as plt



distancesC5 = open('53_DistancesBP_C5ligand.csv', 'w')
header = str('53_distancesBP_C5ligand' + '\n' )
distancesC5.writelines(header)

distancesC1 = open('53_DistancesBP_C1ligand.csv', 'w')
header = str('53_distancesBP_C1ligand' + '\n' )
distancesC1.writelines(header)


#parameters=[["CG","55"],["CD1","128"],["CD2","132"]]
parameters=[["CD1","55"],["CG2","128"],["CD1","132"],["ND2","135"],["CZ","164"],["CB","264"],["CD2","265"],["CB","268"],["ND2","269"],["CD1","271"],["CG1","305"],["CD1","306"],["CD1","309"],["CG","339"],["CG","343"]]
i=0
while i in range (len(parameters)):

#open PDB files18 (https://stackoverflow.com/questions/38991923/how-to-open-multiple-files-in-a-directory)
    Path = "/home/veronica/Cluster/2022/May2022/KOURIST/IsoprenylAcetate/Docking_Script02/Docking_secondTime/Distances_ligand_BP/"
    filelist = os.listdir(Path)
    for x in filelist:
        if x.endswith("53.pdb"):
           # print(x)
        # open every single pdb file present in the list
            with open (x) as fout:
                for riga in fout:
                    #print (str(parameters[i][1]))
                    if riga.startswith("ATOM") and riga.split()[2] == str(parameters[i][0]) and riga.split()[5] == str(parameters[i][1]):
                        #print(str(parameters[i][1]))
                        coord_a1 = float(riga.split()[6])
                        coord_b1 = float(riga.split()[7])
                        coord_c1 = float(riga.split()[8])
#                        i = i + 1                       
#                         print()
                        atom = np.array([coord_a1, coord_b1, coord_c1])
                        #print(str(parameters[i][1]))
 #                       i = i + 1           
    
                    if riga.startswith("HETATM") and riga.split()[2]=="C5":
                        coord_A1 = float(riga.split()[6])
                        coord_B1 = float(riga.split()[7])
                        coord_C1 = float(riga.split()[8])
                        LigandC5_atom = np.array([coord_A1, coord_B1, coord_C1])
 
                    if riga.startswith("HETATM") and riga.split()[2]=="C1":
                        coord_a2 = float(riga.split()[6])
                        coord_b2 = float(riga.split()[7])
                        coord_c2 = float(riga.split()[8])
                        LigandC1_atom = np.array([coord_a2, coord_b2, coord_c2])
 
                        dist_atom_C5 = np.linalg.norm((atom - LigandC5_atom))
                        dist_atom_C1 = np.linalg.norm((atom - LigandC1_atom))

                        print("BP_residue " + str(parameters[i][1]))                        
                        print("dist_atom_C5: ", dist_atom_C5)
                        print("dist_atom_C1: ", dist_atom_C1)

                     #   i = i + 1 

                        distancesC5.write(str(dist_atom_C5) + '\n')
                        distancesC1.write(str(dist_atom_C1) + '\n')
                        #distancesC7.write(str(dist_FI2_C7) + "," + str(parameters[i][1]) + '\n')
                        #distancesC6.write(str(dist_FI2_C6) + "," + str(parameters[i][1]) + '\n')
                        i = i + 1
distancesC5.close()
distanceC1.close()




                       
