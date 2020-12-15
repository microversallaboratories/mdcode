# setup conda environment
conda activate getcontacts

# set variables
expt_name="mdsim_07_10_10_13_49_07"    # experiment name
filepath="data/JLN_1_21_1A/"    # filepath
suffix=".tsv"
filename=${filepath}${expt_name}${suffix}
cores=2

# run getcontacts.py scripts

################################################### <get_dyn> ##############################################

for fn in */*.pdb
do
    # salt bridges
    get_static_contacts.py --structure ${fn}.pdb --output statcont_sb_${fn}.tsv --solv HOH --itypes sb

    # pi-cation
    get_static_contacts.py --structure ${fn}.pdb --output statcont_pc_${fn}.tsv --solv HOH --itypes pc

    # pi stacking
    get_static_contacts.py --structure ${fn}.pdb --output statcont_ps_${fn}.tsv --solv HOH --itypes ps

    # t-stacking
    get_static_contacts.py --structure ${fn}.pdb --output statcont_ts_${fn}.tsv --solv HOH --itypes ts

    # hydrophobic
    get_static_contacts.py --structure ${fn}.pdb --output statcont_hp_${fn}.tsv --solv HOH --itypes hp

    # van der Waals
    get_static_contacts.py --structure ${fn}.pdb --output statcont_hp_${fn}.tsv --solv HOH --itypes hp

    #   --solv HOH 
    #   --sele "chain A"
    #   --sele2 "chain B"
    #   --itypes sb hb
done
