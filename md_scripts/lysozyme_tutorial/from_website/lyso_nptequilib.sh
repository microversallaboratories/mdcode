#!/bin/bash

# Download the .mdp for the NVT equilib
wget http://www.mdtutorials.com/gmx/lysozyme/Files/npt.mdp

# Run an NVT equilibration
grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr

# Run the NVT equilibration
mdrun -deffnm npt

# Create plot of pressure, ensure T is stable
energy -f npt.edr -o pressure.xvg

# Create plot of density
energy -f npt.edr -o density.xvg