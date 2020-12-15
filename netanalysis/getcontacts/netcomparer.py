
import pandas as pd
import os

rin_dfs = []
fileNames = []

for file in os.scandir(path):
    if (file.path.endswith("all.tsv") and file.is_file()):
        fileNames.append(file.name.split("_")[0])
        rin_dfs.append(pd.read_csv(file, sep='\t', names=["frame", "interaction_type", "atom_1", "atom_2"], skiprows=2))