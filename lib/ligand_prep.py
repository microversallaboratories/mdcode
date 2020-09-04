# ligand_prep.py

#####################################################################
# TITLE: ligand_prep.py
# PURPOSE: Header file for ligand preparation module
# PRE-CONDITIONS: Ligand under study needs to be prepared
# POST-CONDITIONS: Applies ligand preparatory functions to produce random structures for ligand docking simulations
#####################################################################

###############
###FUNCTIONS###
###############

#####################################################################
# NAME: extract_lig_from_pro
# DESCRIPTION: Creates a file with the ligand, deletes ligand from protein, saves to PWD
# INPUTS: <ligand+protein>.pdb
# OUTPUTS: <ligand>.pdb <pw/ol>.pdb
# PRE-CONDITIONS: Protein file with ligand is in the PWD
# POST-CONDITIONS: Protein w/out ligand and ligand w/out protein pdbs are in the PWD
#####################################################################
def extract_from_pro(pwl):
	## CHECK INPUT
	# Check ligand+protein.pdb is in PWD
	# If error, exit with appropriate error code
	## CLEAN STRUCTURE
	# Check number of chains in the structure
	# If multiple chains, remove polymeric structure, return one protein-ligand pair
	
	## EXTRACT LIGAND
	# Select the ligand molecule, copy it to a new variable, save the new as <ligand>.pdb
	# Remove the ligand from the protein structure, copy it to a new variable, save it as <pw/ol>.pdb
	return  

#####################################################################
# NAME: choose_num_confs
# DESCRIPTION: Outputs five times the number of rotatable bonds for conf. coverage. May use diff algo
# INPUTS: <ligand>.pdb
# OUTPUTS: <opt_num_confs>.pdb
# PRE-CONDITIONS: Ligand file is in PWD
# POST-CONDITIONS: Outputs a good suggested number of conformations to sample conformation space
#####################################################################
def choose_num_confs(ligand):
	## CHECK INPUT
	# Check PWD for ligand.pdb
	# If error, exit with appropriate error code
	## COUNT DF FOR ROTATABLE BONDS
	# <num_rot_bonds> = calculate rotatable bonds
	## RETURN A HEALTHY NUMBER OF CONFORMATIONS
	return  # Return 5*num_rot_bonds

#####################################################################
# NAME: sample_confs
# DESCRIPTION: Allows the ligand to sample conformational space to pair with protein structures
# INPUTS: <ligand>.pdb <max_num_confs (int)>
# OUTPUTS: Folder in PWD entitled "confs_<ligand>" with all <ligand_confx> from x to <max_num_confs>
# PRE-CONDITIONS: Ligand file (3D or 2D - of a number of formats) exists in PWD 
# POST-CONDITIONS: Ligand file is randomized to a preset number of orientations
#####################################################################
def sample_confs(ligand, max_num_confs):
	## CHECK INPUT
	# Check PWD for ligand.pdb
	# Check max_num_confs > 0
	## GENERATE ANGLES
	# For all confs,
	# For all degrees of freedom in the molecule,
	# Randomly generate an angle
	# Store the angle in a vector at the proper position
	## WRITE FILES
	# For each x up to max_num_confs
	# Apply the angular transformations to the molecule
	# Save the molecule as a PDB file
	return  ## Return from function

#####################################################################
# NAME: 
# DESCRIPTION: 
# INPUTS: 
# OUTPUTS: 
# PRE-CONDITIONS: 
# POST-CONDITIONS: 
#####################################################################

