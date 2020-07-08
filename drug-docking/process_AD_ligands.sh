#!/bin/sh

#%%%%%%%%%%%%%%%%%%%%<CONFIGURATION>%%%%%%%%%%%%%%%%%%%#

# Define the timestamp for the new simulation, to identify the simulation folder and files
JLN_SIM_TIMESTAMP=$(date +"%Y_%m_%d_%H_%M_%S")

# Define the simulation type (prefix)
JLN_SIM_TYPE='vrtscrn'

# Define PDB Filename, paths, & GROMACS Pameters
#JLN_SIM_PDBNAME='NANA'			# Should eventually take this in at runtime!
JLN_DATAPATH=/Users/jacobnorth/Box/extracurriculars/research/SURE_S2020_fileshare/sure_data		# Datafile path
JLN_SIM_PATH=$JLN_DATAPATH/$JLN_SIM_PDBNAME/"${JLN_SIM_TYPE}_${JLN_SIM_TIMESTAMP}"		# Simulation-specific datafile path
JLN_ANAPATH=$JLN_SIM_PATH/analysis		# Analysis filepath

# Make a directory for the current simulation (ANAPATH creates all three target directories)
mkdir -p /Users/jacobnorth/"$JLN_ANAPATH"

echo "Simulation filepath is:"
echo ${JLN_SIM_PATH}

#%%%%%%%%%%%%%%%%%%%</CONFIGURATION>%%%%%%%%%%%%%%%%%%%#

# Change directory to the simulation path
cd ${JLN_SIM_PATH}

# Create a directory to hold the files pulled from ZINC15
mkdir to_test
cd to_test

# Download the selected ZINC15 tranches
bash ZINC-downloader-3D-pdbqt.gz.wget

# Process the waterless file	(ASSUMES that water isn't important for the ligand interactions to the protein surface!!!)
obabel R.pdb -O temp.pdbqt -xh				# Setup a bounce file with all information from R.pdb
grep ATOM temp.pdbqt > receptor.pdbqt		# Place atoms in the receptor PDBqt file

# Unzip all the files in the folders downloaded from ZINC15
gunzip leads/*/*/*.gz

