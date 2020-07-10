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
#cd ${JLN_SIM_PATH}

# Create a directory to hold the files pulled from ZINC15
#mkdir to_test
#cd to_test

# Download the selected ZINC15 tranches
python3 AutoDock.py -d ZINC-downloader-3D-pdbqt.gz.wget

# Segment the large file into many files, with 24 structures per folder
python3 AutoDock.py -s ZINC15.pdbqt 24

# Process the waterless file with obabel	(ASSUMES that water isn't important for the ligand interactions to the protein surface!!!)
obabel R.pdb -O temp.pdbqt -xh				# Setup a bounce file with all information from R.pdb
grep ATOM temp.pdbqt > receptor.pdbqt		# Place atoms in the receptor PDBqt file

# Load the docking conda module, include vina, qvina2, and qvinaw (including split versions)
#conda activate docking

#%%%%%%%%%%%%%%%%%%%%<DIMENSIONS>%%%%%%%%%%%%%%%%%%%%%%#
#c_x=8
#c_y=-0.5
#c_z=10
#s_x=26
#s_y=22
#s_z=20

#%%%%%%%%%%%%%%%%%%%</DIMENSIONS>%%%%%%%%%%%%%%%%%%%%%%#

for f in ligands/*/*.pdbqt; do
	vina --config vina_config.txt --ligand ${f} --out ${f}_out.pdbqt --cpu 2
done

# Run the docking sim, pick one:
#vina --config vina_config.txt  --cpu 2 --out OUTPUT.pdbqt
#vina_split --config vina_config.txt --cpu 2 --out OUTPUT.pdbqt

#qvina2 --config vina_config.txt --cpu 2 --out OUTPUT.pdbqt
#qvina2_split --config vina_config.txt --cpu 2 --out OUTPUT.pdbqt

#qvinaw --config vina_config.txt --cpu 2 --out OUTPUT.pdbqt
#qvinaw_split --config vina_config.txt --cpu 2 --out OUTPUT.pdbqt

# Move files to the simulation path after the run is completed
#mv ligands *.pdbqt ${JLN_SIM_PATH}