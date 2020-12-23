

# %%
# imports

import pdbutils
import elemSpecificPH

import scipy

from ripser import ripser
from persim import plot_diagrams

import matplotlib.pyplot as plt

# %%
# get the structure
struc = pdbutils.createStruct("6VXX.pdb")
# %%
# separate it by its elements
coords = elemSpecificPH.getPositionArray(struc)

# %%
strucarray = elemSpecificPH.struc2elemPosArrays(struc)
# %%
a = strucarray[1]

# %%
# for each substructure (element selection) to analyze,
for i in list(range(strucarray)):
    # PERSISTENT HOMOLOGY
    elemSpecificPH.printPHDiagram(a, i) # print the persistent homology diagram
    
    # KMAPPER
    elemSpecificPH.visKMapper(a, i)

# %%

