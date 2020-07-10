#!/bin/bash

# Download the .mdp for the NVT equilib
wget http://www.mdtutorials.com/gmx/lysozyme/Files/npt.mdp

# Pre-process the input files, prediec PME load
grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr

# Run the NVT equilibration:
mdrun -deffnm md_0_1	# ON CPU
# mdrun -deffnm md_0_1 -nb gpu	# ON ONE GPU
# ON MULTIPLE GPUS???

# Create plot of pressure, ensure T is stable
energy -f npt.edr -o pressure.xvg

# Create plot of density
energy -f npt.edr -o density.xvg