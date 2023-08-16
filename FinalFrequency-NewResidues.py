# Veronica Delsoglio
# date: 07.2022
# THIS SCRIPT: looks into the generated csv files - one per residue position which was redesigned generating 100 outputs- and gives out respectively a csv file where the total number of new residues which was extimated by the mover in that specific redesigned position.  

#!/usr/bin/env python
# coding: utf-8


### Which residues were re-designed at the specific positions ###



# Residue 135
Res135= open("Res135.csv", "w")
word_list = open('135_BPresMuts.txt').read().split()
count_LEU= word_list.count("LEU")
count_TRP= word_list.count("TRP")
count_PHE= word_list.count("PHE")
count_TYR= word_list.count("TYR")

Res135.write("LEU= " + " " + str(count_LEU) + "\n" + "TRP= " + " " + str(count_TRP) + "\n" + "PHE= " + " " + str(count_PHE) + "\n" + "TYR= " + " " + str(count_TYR))
Res135.close()


# Residue 164
Res164= open("Res164.csv", "w")
word_list = open('164_BPresMuts.txt').read().split()
count_LEU= word_list.count("LEU")
count_TRP= word_list.count("TRP")
count_PHE= word_list.count("PHE")
count_TYR= word_list.count("TYR")

Res164.write("LEU= " + " " + str(count_LEU) + "\n" + "TRP= " + " " + str(count_TRP) + "\n" + "PHE= " + " " + str(count_PHE) + "\n" + "TYR= " + " " + str(count_TYR))
Res164.close()


# Residue 265
Res265= open("Res265.csv", "w")
word_list = open('265_BPresMuts.txt').read().split()
count_MET= word_list.count("MET")
count_LEU= word_list.count("LEU")
count_TRP= word_list.count("TRP")
count_PHE= word_list.count("PHE")
count_TYR= word_list.count("TYR")

Res265.write("MET= " + " " + str(count_MET) + "\n" + "LEU= " + " " + str(count_LEU) + "\n" + "TRP= " + " " + str(count_TRP) + "\n" + "PHE= " + " " + str(count_PHE) + "\n" + "TYR= " + " " + str(count_TYR))
Res265.close()

# Residue 268

Res268= open("Res268.csv", "w")
word_list = open('268_BPresMuts.txt').read().split()
count_LEU= word_list.count("LEU")
count_TRP= word_list.count("TRP")
count_PHE= word_list.count("PHE")
count_TYR= word_list.count("TYR")

Res268.write("LEU= " + " " + str(count_LEU) + "\n" + "TRP= " + " " + str(count_TRP) + "\n" + "PHE= " + " " + str(count_PHE) + "\n" + "TYR= " + " " + str(count_TYR))
Res268.close()


