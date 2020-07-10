#!/bin/bash

# Invoke the energy minimization
mdrun -v -deffnm em

# Plot energy chart for eminim 
energy -f em.edr -o potential.xvg