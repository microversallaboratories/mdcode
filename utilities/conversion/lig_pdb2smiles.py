# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from Bio.PDB.PDBParser import PDBParser
parser = PDBParser()
structure = parser.get_structure("test", "1osv_ligand_backup.pdb")
model = structure[0]
chain = model["A"]

# %%
for chain in model:
    print(chain)

# %%
from Bio.PDB import PDBParser, PDBIO

io = PDBIO()
pdb = PDBParser().get_structure("test", "1osv_ligand_backup.pdb")


# %%
import os

io = PDBIO()
end = "_ligand.pdb"
directory = "./ligands/"

for filename in os.listdir(directory):
    if filename.endswith(end): # IF the file ends with the generic ending,
        fileid = filename           # duplicate the fileid for a shortened title
        fileid = fileid.replace(end,'')      # remove the end
        pdb = PDBParser().get_structure(fileid, directory+filename)       # get the structure
        ress = model.get_residues()
        for chain in pdb.get_chains():
            for res in chain.get_residues():                  # for each chain in the structure,
                io.set_structure(residue)                     # set the structure to the chain
                #io.save(pdb.get_id() + "_" + chain.get_id() + ".pdb")   # save the chain to a new PDB file
                io.save(fileid + "_" + chain.get_id() + ".pdb")   # save the chain to a new PDB file


# %%
ligs = structure[:][:][:]


# %%
import os

io = PDBIO()
end = "_ligand.pdb"
directory = "./ligands/"

for filename in os.listdir(directory):
    if filename.endswith(end): # IF the file ends with the generic ending,
        fileid = filename           # duplicate the fileid for a shortened title
        fileid = fileid.replace(end,'')      # remove the end
        pdb = PDBParser().get_structure(fileid, directory+filename)       # get the structure
        ress = model.get_residues()
        for res in ress:
            io.set_structure(res)                     # set the structure to the chain
            io.save(fileid + "_" + chain.get_id() + ".pdb")   # save the chain to a new PDB file


# %%
from Bio.PDB import PDBParser
from Bio.PDB.PDBIO import PDBIO
import os


parser = PDBParser()
structure = parser.get_structure("1a8o", "ligands/1osv_ligand.pdb")
io=PDBIO()
for i in structure.get_residues():
    io.set_structure(i)
    io.save(str(i)+".pdb")
    #os.remove("bio-pdb-pdbio-out.pdb")  # tidy up


# %%
class LigSelect(PDBIO.Select):
    def ret_ligname(self, residue):
        if not is_aa(residue):
            return residue
        else:
            return

null.tpl [markdown]
# ## StackOverflow solution
# ~~~~~~~~~~~~~~
# https://stackoverflow.com/questions/61390035/how-to-save-each-ligand-from-a-pdb-file-separately-with-bio-pdb

# %%
import io

from Bio.PDB import PDBParser, PDBIO, Select

def is_het(residue):
    res = residue.id[0]
    return res != " " and res != "W"

class ResidueSelect(Select):
    def __init__(self, chain, residue):
        self.chain = chain
        self.residue = residue
        
    def accept_chain(self, chain):
        return chain.id == self.chain.id

    def accept_residue(self, residue):
        """ Recognition of heteroatoms - Remove water molecules """
        return residue == self.residue and is_het(residue)

def extract_ligands(path):
    """ Extraction of the heteroatoms of .pdb files """

    for pfb_file in os.listdir(path + 'pdbs/'):
        i = 1
        if pfb_file.endswith('.pdb') and not pfb_file.startswith("lig_"):
            pdb_code = pfb_file[:-4]
            pdb = PDBParser().get_structure(pdb_code, path + 'pdbs/' + pfb_file)
            io = PDBIO()
            io.set_structure(pdb)
            model_selected = pdb[0]
            # for model in pdb:

            for chain in model_selected:
                for residue in chain:
                    if not is_het(residue):
                        continue
                    print(f"saving {chain} {residue}")
                    io.save(f"lig_{pdb_code}_{i}.pdb", ResidueSelect(chain, residue))
                    i += 1

# Main
path = ""

extract_ligands(path)


