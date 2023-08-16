Cooperation project with research group of Uni.-Prof. Robert Kourist:
A new biosynthetic route from Isoprenol to tuli- palin A – Steps towards fermentative production of the polymer precursor”. (December 2021 - December 2022)

Here you can find the main scripts used for docking study of AlkB GPo1 enzyme with Isoprenyl-acetate ligand. 
The main points of the method adopted are:

A) Introduction of the di-iron cluster inside the protein scaffold, minimisation and optimization of the overall structure;
B) After ligand initialization inside the protein scaffold, docking study performed with Rosetta software;
C) Data analysis of the docking results. This step is divided in further substeps:
                         1) evaluation of the docked ligand position inside the protein scaffold
                         2) ligand orientation respect to the Fe atoms
                         3) distance of the docked ligand to the catalytic site residues to find the closest ones
D) based on previous data analysis: mutation of the specific selected positions of the protein active site. 





COMPUTATIONAL METHOD OF DOCKING STUDY AND RESPECTIVE ROSETTA (.xml) AND PYTHON (.py) SCRIPTS 

******** SCRIPT FOR POINT A ********

The Fe atoms were fixed inside the protein scaffolds with a RosettaScript script, using the AddOrRemoverMatchCsts and EnzRepackMinimize movers
To run the Rosetta xml script the following command was used:
(Run Rosetta xml script )
/ROSETTA/main/source/bin/rosetta.script.linuxgccrelease - s input.pdb
-parser:protocol Iron-introduction.xml -extra_res_fa FI2.params -extra_res_fa FI3.params -match:geometric_constraint_file CST_file.cst @enzflags

+++ (list of files used: Iron-introduction.xml; FI2.params, FI3.params, CST_file.cst, enzflags)





******** SCRIPT FOR POINT B ********

To script running was performed with the following command, generating 100 output (-nstruct 100) pdb:
(Run command 4)
(ROSETTA)/main/source/bin/rosetta.script.linuxgccrelease - s input.pdb -parser:protocol docking_script.xml -extra_res_fa FI2.params -extra_res_fa FI3.params -extra_res_fa ligand.params -match:geometric_constraint_file constraints_file.cst - nstruct 100 @enzflags

+++ (list of files used: docking_script.xml; enzflags (same of previous step); FI2.params and FI3.params (same of previous step))



******** SCRIPTS FOR POINT C ******** 

Data analysis of docking generated outputs:
C1) Score of docked ligands.
A Python script was generated to evaluate the ligand score in a docked fashion inside the protein scaffold.
C2) Ligand orientation inside the catalytic active site.
A Python script was generated to measure the distances from the two extremities of the ligand to the Fe2 - Fe3 atoms. Four CSV files were generated from the script run, one for each Fe atom - ligand ́s extremity distance combination. Analysing the CSV outputs, the shorter and the longer Fe-ligand ́s extremity distances were found. Moreover, it was possi- ble to evaluate how the ligand was most frequently orientation inside the catalytic pocket.
C3) Selection of the protein residues surrounding the best docked ligand molecule.
The residues surrounding the best docked ligand molecules were selected. Then, using a Python script, the distances from them and the respective extremities of the ligand were measured. In that way it was possible to find the closest residues of the catalytic pocket to the ligand.
C4) Residues of the Enzymatic catalytic pocket: REU evaluation.

+++ (list of files used: Ligand-Docked-Score.py, DiIronCluster-Ligand-Distances.py, CatalyticPocketResidues-Ligand-Distances.py, CatalyticPocketResidues-Score-REU.py)



********* SCRIPTS FOR POINT D ********

D1) Rosetta re-designing of the selected residues.
The residues sharing short distances from the best docked ligands, even bad REU energy, were gathered for being designed. A Rosetta xml script was used, FastDesign mover designed these positions, choosing just from other hydrophobic residues. A total of 100 outputs was generated.
D2)Re-designed substituents.
Python scripts were written to compare all the 100 output sequences at level of the re- designed positions. Which residues occurred most, their chemical nature and frequency provided us with the list of substituents to be tested by Kourist ́s group in the wet-lab
(Run Rosetta xml script )
/ROSETTA/main/source/bin/rosetta.script.linuxgccrelease - s input.pdb
-parser:protocol Mutation.xml -extra_res_fa FI2.params -extra_res_fa FI3.params @enzflags




+++ (list of files used: Mutation.xml; Evaluation-Mutated-Residues.py; FinalFrequency-NewResidues.py, FI2.params and FI3.params and enzflags (previous files))




