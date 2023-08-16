#!/usr/bin/env python
# coding: utf-8

import Bio.PDB
import os

import numpy as np
import pathlib
import glob
import pandas as pd
import seaborn as sns
import matplotlib as plt
# open file di scrittura.1
# open file.pdb.1 
# estrapola il valore dalla colonna x iniziante con ATOM del file.pdb.1
# copia i valori nel file di scrittura.1 e chiudilo
# open file di scrittura.2
# open file.pdb.2
# estrapola REU
# copia in file scrittura.2
# chiudi file.2

REU_measures=open("REU_meas","w")
atom_names=["ALA", "MET", "ARG", "ILE", "LEU"]
with open (".pdb", "r") as fout:
    for line in fout:
        if line.startswith()[-1] :
            lista_REU=[]
            valuesREU=line.rsplit()[-1]
            print(valuesREU)
            lista_REU.append(valuesREU)
            REU_measures.write(str(lista_REU)+ '\n')
            
REU_measures.close()            

     



