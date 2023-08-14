# author: Veronica Delsoglio
# date: 02.2022

#!/usr/bin/env python
# coding: utf-8

# THIS SCRIPT: measures the distances between the terminal C of your ligand and respectively the 2 Fe atoms once the docking is performed

# online references I looked through: https://pymolwiki.org/index.php/Measure_Distance

# import libraries
import numpy as np
import matplotlib as plt
import pandas as import pd
import glob       #file_pattern analysis: it look through all the files located in the same folder
from pymol import cmd

# Open a file in writing ('w') mode where to save the distances results

DistanceFile = open ("/home/veronica/Cluster/January2022/KOURIST/GA_ligand_dock_script/Script_1/RepackMinimise/Filters/ddG/dist.txt", 'w')

# Look at all the files located on a speciic path, using glob
# load the file on PyMol to perform the measurements
# Calculate the distances between the C terminal atom - Fe1 and C terminal atom - Fe2
# Write the formatted dst value on the dist.txt file
# close the dist.txt file and quit cmd
for file in glob.glob ("/home/veronica/Cluster/January2022/KOURIST/GA_ligand_dock_script/Script_1/RepackMinimise/Filters/ddG/*1_000*.pdb"):
    cmd.load ("/home/veronica/Cluster/January2022/KOURIST/GA_ligand_dock_script/Script_1/RepackMinimise/Filters/ddG"+file)
    dstFe1 = cmd.distances('mol1///X/X', 'mol1///X/X' )
    dstFe2 = cmd.distance ('mol1///X/X', 'mol1///X/X')
    DistanceFile.write("%8.3f\n"%dstFe1)
    DistanceFile.write("%8.3f\n"%dstFe2)

    DistanceFile.close()

    cmd.quit()
