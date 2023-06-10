#!/usr/bin/env python
# coding: utf-8

# In[44]:


#Developed 07/13/2020 by Jeffrey Hu with assistance from Professor Jianjun Hu
#Sorts materials cif files by element number and space group
from pymatgen.io.cif import CifParser
from shutil import copyfile
from pymatgen.core.composition import Composition
import glob
import statistics 

import numpy as np
from pymatgen import MPRester
from pymatgen.core.structure import Structure
from matminer.featurizers.site import CrystalNNFingerprint
from matminer.featurizers.structure import SiteStatsFingerprint
import multiprocessing as mp
import pandas as pd

elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 
                        'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
                        'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 
                        'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 
                        'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 
                        'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
print(len(elements))


# In[43]:


ElementContactMap={}
df = pd.read_csv('data/atom-lteq-12.csv')
files = df.values[:,0]

print(len(files))
def base(file):
    crystal = Structure.from_file('data/cifs/%s.cif'%file)
    shortestDistance={}
    for i,x1 in enumerate(crystal.sites):
        for j,y1 in enumerate(crystal.sites):
            if i==j or i>j:
                continue
            #print(x1.specie)
            x=str(x1.specie)
            y=str(y1.specie)
            if not (x,y) in shortestDistance:
                shortestDistance[(x,y)]=crystal.distance_matrix[i,j]
            else:
                if crystal.distance_matrix[i,j]< shortestDistance[(x,y)]:
                    shortestDistance[(x,y)]=crystal.distance_matrix[i,j]
    return shortestDistance


pool = mp.Pool(processes=6)
results = [pool.apply_async(base, args=(f,)) for f in files]

for p in results:
    if p.get() is not None:
        temp = p.get()
        for pair in temp:
            if pair in ElementContactMap:
                ElementContactMap[pair].append(temp[pair])
            else:
                ElementContactMap[pair]=[temp[pair]]
print(len(results))

elementDistanceMap={}
for pair in ElementContactMap:
    mean=sum(ElementContactMap[pair])/len(ElementContactMap[pair])
    if len(ElementContactMap[pair]) ==1:
        std=0
    else:
        std =statistics.stdev(ElementContactMap[pair])
    elementDistanceMap[pair] = (mean,std)

    
#save to data
with open("data/contactmaplist.csv",'w') as ofile1:
    for pair in ElementContactMap:
        ofile1.write(f"{pair},{','.join([f'{x:.5f}' for x in ElementContactMap[pair]])}\n")

with open("data/contactdistances.csv",'w') as ofile2:
    for pair in elementDistanceMap:
        ofile2.write(f"{pair},{elementDistanceMap[pair][0]:.5f},{elementDistanceMap[pair][1]:.5f}\n")





