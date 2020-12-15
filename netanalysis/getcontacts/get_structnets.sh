# setup conda environment
eval "$(command conda 'shell.bash' 'hook' 2> /dev/null)"

conda activate getcontacts

# set variables
expt_name="mdsim_07_10_10_13_49_07"    # experiment name
filepath="data/JLN_1_21_1A/"    # filepath
suffix=".tsv"
filename=${filepath}${expt_name}${suffix}
cores=2

# make folders to hold data

mkdir statcont_sb statcont_pc statcont_ps statcont_ts statcont_hp statcont_vdw

# run getcontacts.py scripts

################################################### <get_stat> ##############################################

for fn in data/JLN_1_21_1B/*/*.pdb
do
    # salt bridges
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_sb.tsv --itypes sb --sele2 'not (protein or nucleic or solv or lipid)'
    mv ${fn/.pdb/}_statcont_sb.tsv statcont_sb

    # pi-cation
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_pc.tsv --itypes pc --sele2 'not (protein or nucleic or solv or lipid)'
    mv ${fn/.pdb/}_statcont_pc.tsv statcont_pc

    # pi stacking
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_ps.tsv --itypes ps --sele2 'not (protein or nucleic or solv or lipid)'
    mv ${fn/.pdb/}_statcont_ps.tsv statcont_ps

    # t-stacking
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_ts.tsv --itypes ts --sele2 'not (protein or nucleic or solv or lipid)'
    mv ${fn/.pdb/}_statcont_ts.tsv statcont_ts

    # hydrophobic
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_hp.tsv --itypes hp --sele2 'not (protein or nucleic or solv or lipid)'
    mv ${fn/.pdb/}_statcont_hp.tsv statcont_hp

    # van der Waals
    get_static_contacts.py --structure ${fn} --output ${fn/.pdb/}_statcont_vdw.tsv --itypes vdw --sele2 'not (protein or nucleic or solv or lipid)'
    mv ${fn/.pdb/}_statcont_vdw.tsv statcont_vdw

    #   --solv HOH 
    #   --sele "chain A"
    #   --sele2 "chain B"
    #   --itypes sb hb
done
