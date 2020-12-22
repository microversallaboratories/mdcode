

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
#a = scipy.spatial.distance.pdist(strucarray)
# %%
diagrams = ripser(a)['dgms']

# %%
plot_diagrams(diagrams, show=False)

plt.savefig("persistent_homology.png")