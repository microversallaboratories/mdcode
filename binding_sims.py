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
# NAME: permute_prolig
# DESCRIPTION: Permutes a vector of protein structures with a vector of ligands
# INPUTS: [<pro>.pdb], [<lig>.pdb]
# OUTPUTS: [<pro>, <lig>] for 0 to len([<pro>.pdb] * [<lig>.pdb])-1
# PRE-CONDITIONS: Two vectors of proteins and ligands have been created
# POST-CONDITIONS: A matrix of protein-ligand combos to test is generated and returned
#####################################################################
def permute_prolig(pros, ligs):
    #

    return  

#####################################################################
# NAME: bindsim_gmx
# DESCRIPTION: Runs a series of binding simulations on proligs in a matrix
# INPUTS: [[<prolig>]] matrix
# OUTPUTS: Trajectories for binding simulations run, in a folder in PWD
# PRE-CONDITIONS: prolig matrix is generated and input
# POST-CONDITIONS: Trajectories are saved in a folder in the PWD
#####################################################################
def bindsim_gmx(proligs):
    ##
    ##
    ##
    ##
    return

#####################################################################
# NAME: 
# DESCRIPTION: 
# INPUTS: 
# OUTPUTS: 
# PRE-CONDITIONS: 
# POST-CONDITIONS: 
#####################################################################

#####################################################################
# NAME: 
# DESCRIPTION: 
# INPUTS: 
# OUTPUTS: 
# PRE-CONDITIONS: 
# POST-CONDITIONS: 
#####################################################################