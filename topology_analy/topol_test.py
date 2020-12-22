

# %%
# imports

import pdbutils
import elemSpecificPH

import scipy

from ripser import ripser

# %%
# get the structure
struc = pdbutils.createStruct("6ZGI.pdb")
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
plot_diagrams(diagrams, show=True)