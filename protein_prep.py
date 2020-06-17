# protein_prep.py

#####################################################################
# TITLE: protein_prep.py
# PURPOSE: Header file for protein preparation module
# PRE-CONDITIONS: Protein under study needs to be prepared
# POST-CONDITIONS: Applies prep preparatory functions to produce set of structures for ligand docking simulations
#####################################################################

###############
###FUNCTIONS###
###############

#####################################################################
# NAME: clean_pdb
# DESCRIPTION: Cleans a PDB file by removing unwanted residues, ligands, etc.
# INPUTS: <pro>.pdb, [res_exclud]
# OUTPUTS: <pro>_processed.pdb
# PRE-CONDITIONS: <pro>.pdb exists in the PWD
# POST-CONDITIONS: <pro>_processed.pdb is output to the PWD
#####################################################################
def clean_pdb(pro, max_breaks):
	## CHECK INPUT
	# Verify files are in the PWD
	# Verify len(res_exclud) < len(res_pdb)

	## LOOP THROUGH RESIDUES, REMOVE UNNEEDED ONES
	# For each residue in the PDB file,
	# If !protein and !in_res_excluded,
	# Delete from the PDB structure

	## VALIDATE STRUCTURE PRODUCED
	# If num_breaks > max_breaks
	# Return error
	
	## SAVE FILE
	# Save final structure to <pro>_processed.pdb

	return

#####################################################################
# NAME: ensemble_sampler
# DESCRIPTION: Computes several experimentally-valid stable conformations for a protein to take
# INPUTS: <prox>.pdb from x to num, num
# OUTPUTS: ensemble_<prox>.pdb
# PRE-CONDITIONS: List of protein structures (to serve as the ensemble) are in the PWD
# POST-CONDITIONS: Ensemble is returned to the PWD, calculated using ensemblator
#####################################################################
def ensemble_sampler(pro_list, num):
	## CHECK INPUT
	# Verify files are in the PWD
	# Verify num > 2
	# Else, exit

	## RUN ENSEMBLATOR ON PDBLIST, SUPPRESS SOME OUTPUT
	# Prepare ...
	# ...

	## RETURN ENSEMBLE
	return

#####################################################################
# NAME: 
# DESCRIPTION: 
# INPUTS: 
# OUTPUTS: 
# PRE-CONDITIONS: 
# POST-CONDITIONS: 
#####################################################################