# ml_md_analysis.py

#####################################################################
# TITLE: ml_md_analysis.py
# PURPOSE: Header file for molecular dynamics ml analysis with PyTorch
# PRE-CONDITIONS: One or more trajectories has been generated
# POST-CONDITIONS: Trajectory analyses are completed
#####################################################################

###############
###FUNCTIONS###
###############

#####################################################################
# NAME: is_bound
# DESCRIPTION: Returns 1 if ligand is bound, returns 0 if not.
# INPUTS: <prolig_frame>.pdb, <prolig_ref>.pdb
# OUTPUTS: 1 if ligand is bound (by RMSD), 0 if ligand is not bound (by RMSD)
# PRE-CONDITIONS: Prolig is generated, and is being tested (generally during a simulation)
# POST-CONDITIONS: 1 or 0 is returned
#####################################################################
def is_bound(prolig_frame, prolig_ref):
	## CHECK INPUTS
	# If prolig_frame exists and prolig_ref exists, continue
	# else return
	
	## CHECK RMSD
	# Calculate RMSD between prolig_frame and prolig_ref
	# If < ???
	# return 1
	# Else, 
	return  # return 0

#####################################################################
# NAME: surf_bind_traj
# DESCRIPTION: Produces a 3D map where proximity of the molecule to the atoms within 5A become highlighted during the binding event. Starts "movie" at RMSD = max, ends at RMSD = min
# INPUTS: <prolig_traj>.trj, <RMSD_min>, <RMSD_max>
# OUTPUTS: Prints a 3D video of the binding event to PWD
# PRE-CONDITIONS: Protein ligand binding trajectory has been generated
# POST-CONDITIONS: <prolig_bind_traj>.??? is output to the PWD
#####################################################################
def surf_bind_traj(traj, r_min, r_max):
	## CHECK INPUTS
	# If traj exists, continue
	# If r_min < 1 or r_max < r_min, exit with error

	## CHECK

	return

#####################################################################
# NAME: learn_features
# DESCRIPTION: Uses a machine learning algorithm to generate feature importance
# INPUTS: 
# OUTPUTS: 
# PRE-CONDITIONS: 
# POST-CONDITIONS: 
#####################################################################
