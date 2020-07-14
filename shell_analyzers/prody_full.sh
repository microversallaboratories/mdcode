#!/bin/bash

# CMDLNARGS: 
# $1 = name of path to file. (pdb format)

# Run ANM
prody anm -a -A -F png $1 

# Run GNM
prody gnm -a -A -F png $1 

# Run PCA
prody pca -a -A -F png $1 

# Run EDA
prody eda -a -A -F png $1 