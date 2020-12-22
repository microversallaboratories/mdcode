# elemSpecificPH.py

'''
elemSpecificPH : A package for element-specific persistent homology in Python.

Uses algebraic topology tools to create persistence diagrams for protein structures (PDB files).
'''

'''
IMPORT PACKAGES
'''

import Bio.PDB

import sktda as skt
import ripser
from persim import plot_diagrams
import numpy as np

'''
FUNCTIONS
'''

# create an atom position array from a Bio.PDB.Structure.Structure object
def getPositionArray(struc: Bio.PDB.Structure.Structure) -> np.ndarray:
    '''
    Obtains a position array for the 3D-coordinates of each atom in the provided structure.
    '''
    coords = []   # construct a (3 x natoms) array
    # take the structure object
    # faster to do it this way, see: 
    # https://stackoverflow.com/questions/3881453/numpy-add-row-to-array

    for model in struc: # for each model,
        for chain in model:    # for each chain,
            for res in chain:   # for each residue,
                for atom in res:    # for each atom,
                    coords.append(atom.get_coord()) # get the coordinates, append to a new array
    
    return np.array(coords)    # convert to np.ndarray

# create an atom position array from a Bio.PDB.Structure.Structure object
def struc2elemPosArrays(struc: Bio.PDB.Structure.Structure) -> np.ndarray:
    '''
    Obtains a list of position arrays separated by atom type for the 3D-coordinates of each atom in the provided structure. Glommed together into one function because I was frustrated at how to get Bio.PDB to work properly.
    '''

    elist = [{"H"}, {"C", "CA", "CB", "CG", "CD", "CE"}, {"O"}, {"N"}, {"S"}, {"P"}, {"Cl"}]

    elemarray = []

    for set in elist:
        coords = []   # construct a (3 x natoms) array
        # take the structure object
        # faster to do it this way, see: 
        # https://stackoverflow.com/questions/3881453/numpy-add-row-to-array

        for model in struc: # for each model,
            for chain in model:    # for each chain,
                for res in chain:   # for each residue,
                    for atom in res:    # for each atom,
                        if atom.get_id() in set:   # if it's the proper atomtype,
                            coords.append(atom.get_coord()) # get the coordinates, append to a new array
        elemarray.append(np.array(coords))

    return elemarray   # convert to np.ndarray

# return 1 if the element ID contains the string of interest
def elemContainsQuery(atom: Bio.PDB.Atom.Atom, query: set) -> bool:
    return 1 if (atom.get_id() in query) else 0

'''
class IsAtomType(Select, query):
    def accept_atom(self, atom, query):
        return elemContainsQuery(atom, query)
'''

# separate a single PDB structure into a list of element-specific Bio.PDB.Structure.Structure objects
def sepPDBbyElement(struc: Bio.PDB.Structure.Structure) -> list:
    '''
    elist = [{"H"}, {"C", "CA", "CB", "CG", "CD", "CE"}, {"O"}, {"N"}, {"S"}, {"P"}, {"Cl"}]  # will **likely** not use H...
    struc_list = []
    #for e in elist:                         # for each element query in elist,
        #def subsetStruc(struc: Bio.PDB.Structure.Structure, queryset: set) -> Bio.PDB.Structure.Structure:
            
            #Subsets a structure according to if the atoms match an ID query, and returns the resulting structure.
            
            s = struc.copy()    # make a copy of the starting structure
            #s = Bio.PDB.Structure.Structure(id="subset")   # create a new structure object with a name similar to the element
            #for atom in s.get_atoms():      # for each atom in the original structure,
            #    if elemContainsQuery(atom, e):  # if the current atom is the same type as element,
            #        s.detach_child(atom)
            #        print("Added!")
            #return s
        #struc_list.append(subsetStruc(struc, e))    # append the new structure object to the struc_list


    '''
    return struc_list

# combine single-element PDB structure files into new files to determine certain information
def combineElementTypes(struc1:Bio.PDB.Structure.Structure, struc2:Bio.PDB.Structure.Structure) -> Bio.PDB.Structure.Structure:

    return

# compute distance matrix between all atoms in a structure
def calcDistanceMatrix(struc1: Bio.PDB.Structure.Structure) -> Bio.PDB.Structure.Structure:

    return

