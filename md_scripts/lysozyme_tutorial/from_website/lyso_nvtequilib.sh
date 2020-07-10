#!/bin/bash

# Download the .mdp for the NVT equilib
wget http://www.mdtutorials.com/gmx/lysozyme/Files/nvt.mdp

# Run an NVT equilibration
grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr

# Run the NVT equilibration
mdrun -deffnm nvt

# Create plot of temperature, ensure T is stable
energy -f nvt.edr -o temperature.xvg