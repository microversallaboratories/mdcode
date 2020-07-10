#!/bin/bash

# Center the trajectory on the protein's center, don't allow periodity weirdness
trjconv -s md_0_1.tpr -f md_0_1.xtc -o md_0_1_noPBC.xtc -pbc mol -center

# Calculate RMSD on the corrected trajectory
rms -s md_0_1.tpr -f md_0_1_noPBC.xtc -o rmsd.xvg -tu ns

# Calc RMSD relative to crystal
rms -s em.tpr -f md_0_1_noPBC.xtc -o rmsd_xtal.xvg -tu ns

# Calc Radius of gyration
gyrate -s md_0_1.tpr -f md_0_1_noPBC.xtc -o gyrate.xvg