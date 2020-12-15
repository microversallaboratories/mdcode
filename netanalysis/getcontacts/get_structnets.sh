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
    # all
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_all.tsv --itypes all --sele2 'not (protein or nucleic or solv or lipid)'

    #   --solv HOH 
    #   --sele "chain A"
    #   --sele2 "chain B"
    #   --itypes sb hb
done
