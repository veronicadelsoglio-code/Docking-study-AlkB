# Veronica Delsoglio
# date: 06.2022
# THIS SCRIPT: 1) greps the REU + residue NAME at specific positions looking through a list of pdb outputs generated after sequence mutation.
#              2) looks at the list of new redesigned residues at each selected position and makes an evaluation of the frequency in occurrence of new residues in that position

#!/usr/bin/env python
# coding: utf-8
#import libraries

import os

                                                                             # point 1)

Mutations= open("Mutations.txt","w")


BP_listof_residues_POSITIONS=["135", "164", "265", "268", "309"]

i=0
while i in range (len(BP_listof_residues_POSITIONS)):
    #print(str(BP_listof_residues_POSITIONS[i]))
    Path = "/home/veronica/Cluster/2022/May2022/KOURIST/IsoprenylAcetate/Docking_Script02/Docking_secondTime/Mutation_of_BP_residues/"
    filelist = os.listdir(Path)
    for x in filelist:
        if x.startswith("sol_1.ref_0013_"):
         #   print(x)
         # open every single pdb file present in the list
            with open (x) as fout:
                for riga in fout:
                    if riga.startswith("ATOM"):
                        if riga.split()[2] == "N":
                      
                        #print(riga.split()[5])
                            if riga.split()[5] == str(BP_listof_residues_POSITIONS[i]):
                                risultato=str(x) + "  " + riga.split()[3] +  "  " + str(BP_listof_residues_POSITIONS[i] + "\n")
                                print(risultato)                       
                                Mutations.write(risultato)
# print (BP_listof_residues_POSITIONS[i])    
#print (riga.split()[3])
  #                  if riga.startswith("ATOM") and riga.split()[5] == str(BP_listof_residues_POSITIONS[i]):# and riga.split()[2] == "N"
#                        # print(str(riga.split()[3]) + "\n" + str(BP_listof_residues_POSITIONS[i])+ "\n" + str(x))
    i=i+1 
Mutations.close()


# open Mutations file and see the mutants at each selected position
# Residue_BP 135
res135Mutants = open ("135_BPresMuts.txt", "w")
with open ("Mutations.txt", "r") as fmut:
    for line in fmut:
       # print(line)
        if line.split()[2]== "135":
            ris=str(line.split()[1]) + "\n"
            #print(line.split()[1])
            res135Mutants.write(ris)
res135Mutants.close()

                                                                     # point 2)
# Residue 135
Res135= open("Res135.csv", "w")
word_list = open('135_BPresMuts.txt').read().split()
count_LEU= word_list.count("LEU")
count_TRP= word_list.count("TRP")
count_PHE= word_list.count("PHE")

Res135.write("LEU= " + " " + str(count_LEU) + "\n" + "TRP= " + " " + str(count_TRP) + "\n" + "PHE= " + " " + str(count_PHE))
Res135.close()


                                                                     # point 1)
# Residue_BP 164
res164Mutants = open ("164_BPresMuts.txt", "w")
with open ("Mutations.txt", "r") as fmut:
    for line in fmut:
          # print(line)
        if line.split()[2]== "164":
            ris=str(line.split()[1]) + "\n"
            #print(line.split()[1])
            res164Mutants.write(ris)
res164Mutants.close()
                                                                      # point 2)


# Residue 164
Res164= open("Res164.csv", "w")
word_list = open('164_BPresMuts.txt').read().split()
count_LEU= word_list.count("LEU")
count_TRP= word_list.count("TRP")
count_PHE= word_list.count("PHE")
count_TYR= word_list.count("TYR")

Res164.write("LEU= " + " " + str(count_LEU) + "\n" + "TRP= " + " " + str(count_TRP) + "\n" + "PHE= " + " " + str(count_PHE) + "\n" + "TYR= " + " " + str(count_TYR))
Res164.close()





                                                                       # point 1)

# Residue_BP 265
res265Mutants = open ("265_BPresMuts.txt", "w")
with open ("Mutations.txt", "r") as fmut:
    for line in fmut:
          # print(line)
        if line.split()[2]== "265":
            ris=str(line.split()[1]) + "\n"
            #print(line.split()[1])
            res265Mutants.write(ris)
res265Mutants.close()



                                                                         # point 2)


# Residue 265
Res265= open("Res265.csv", "w")
word_list = open('265_BPresMuts.txt').read().split()
count_LEU= word_list.count("LEU")
count_TRP= word_list.count("TRP")
count_PHE= word_list.count("PHE")
count_TYR= word_list.count("TYR")

Res265.write("LEU= " + " " + str(count_LEU) + "\n" + "TRP= " + " " + str(count_TRP) + "\n" + "PHE= " + " " + str(count_PHE) + "\n" + "TYR= " + " " + str(count_TYR))
Res265.close()




                                                                        # point 1)
# Residue_BP 268
res268Mutants = open ("268_BPresMuts.txt", "w")
with open ("Mutations.txt", "r") as fmut:
    for line in fmut:
          # print(line)
        if line.split()[2]== "268":
            ris=str(line.split[1]) + "\n"
            #print(line.split()[1])
            res268Mutants.write(ris)
res268Mutants.close()
                                                                         # point 2)


# Residue 268

Res268= open("Res268.csv", "w")
word_list = open('268_BPresMuts.txt').read().split()
count_LEU= word_list.count("LEU")
count_TRP= word_list.count("TRP")
count_PHE= word_list.count("PHE")
count_TYR= word_list.count("TYR")

Res268.write("LEU= " + " " + str(count_LEU) + "\n" + "TRP= " + " " + str(count_TRP) + "\n" + "PHE= " + " " + str(count_PHE) + "\n" + "TYR= " + " " + str(count_TYR))
Res268.close()



                                                                         # point 1)

# Residue_BP 309
res309Mutants = open ("309_BPresMuts.txt", "w")
with open ("Mutations.txt", "r") as fmut:
    for line in fmut:
          # print(line)
        if line.split()[2]== "309":
            ris=str(line.split()[1]) + "\n"

            #print(line.split()[1])
            res309Mutants.write(ris)
res309Mutants.close()

                                                                          # point 2)



 # Residue 309

Res309= open("Res309.csv", "w")
word_list = open('309_BPresMuts.txt').read().split()
count_LEU= word_list.count("LEU")
count_TRP= word_list.count("TRP")
count_PHE= word_list.count("PHE")
count_TYR= word_list.count("TYR")

Res309.write("LEU= " + " " + str(count_LEU) + "\n" + "TRP= " + " " + str(count_TRP) + "\n" + "PHE= " + " " + str(count_PHE) + "\n" + "TYR= " + " " + str(count_TYR))
Res309.close()

# After the point 1 txt files are generated (one x each residue position included in the mutation process). These files contain a list of all  the residues that the mover used to redesign those specific positions
# After the point 2 csv files are generated (one per each txt file generated in point 1). These files contain the residues name which were used to mutate that specific position + the total amount of each of them to see the most / less frequent one used by the mover. 
