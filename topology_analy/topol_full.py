

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
# PERSISTENT HOMOLOGY

diagrams = ripser(a)['dgms']
plot_diagrams(diagrams, show=False)

plt.savefig("persistent_homology.png")

# %%
# KMAPPER

# Import the class
import kmapper as km

# Initialize
mapper = km.KeplerMapper(verbose=1)

# Fit to and transform the data
projected_data = mapper.fit_transform(data, projection=[0,1]) # X-Y axis

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(projected_data, data, nr_cubes=10)

# Visualize it
mapper.visualize(graph, path_html="make_circles_keplermapper_output.html",
                 title="make_circles(n_samples=5000, noise=0.03, factor=0.3)")