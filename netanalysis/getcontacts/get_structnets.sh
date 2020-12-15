# setup conda environment
eval "$(command conda 'shell.bash' 'hook' 2> /dev/null)"

conda activate getcontacts

# set variables
expt_name="mdsim_07_10_10_13_49_07"    # experiment name
filepath="data/JLN_1_21_1A/"    # filepath
suffix=".tsv"
filename=${filepath}${expt_name}${suffix}
cores=2

# run getcontacts.py scripts

################################################### <get_stat> ##############################################

for fn in data/JLN_1_21_1B/*/*.pdb
do
    # salt bridges
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_sb.tsv --itypes sb --sele2 'not (protein or nucleic or solv or lipid)'

    # pi-cation
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_pc.tsv --itypes pc --sele2 'not (protein or nucleic or solv or lipid)'

    # pi stacking
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_ps.tsv --itypes ps --sele2 'not (protein or nucleic or solv or lipid)'

    # t-stacking
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_ts.tsv --itypes ts --sele2 'not (protein or nucleic or solv or lipid)'

    # hydrophobic
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_hp.tsv --itypes hp --sele2 'not (protein or nucleic or solv or lipid)'

    # van der Waals
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_hp.tsv --itypes hp --sele2 'not (protein or nucleic or solv or lipid)'

    #   --solv HOH 
    #   --sele "chain A"
    #   --sele2 "chain B"
    #   --itypes sb hb
done