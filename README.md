# mdcode

A library of research notebooks produced to interpret MD trajectories related to ligand binding on several target complexes. This repository is to document the progress during SURE 2020 at Oregon State University.

# Analysis components
- Possession and intensity of various protein dynamic modes along the protein surface from experimental (PCA from NMR) and computational (ANM from XRD) sources.
- Occupancy and probability of various protein ensembles of low-energy states from experimental (ensembles produced by Ensemblator) and computational (Markov Models from PyEMMA) sources.
- Transition path, committor, and network transition analysis for ligand binding to the protein target.
- Analysis of residence time for a ligand in a binding pocket of a target protein with respect to unsupervised or supervised learned features *via* a PyTorch Machine learning model.
- Generation of a ligand with maximal residence time as a potential drug target.