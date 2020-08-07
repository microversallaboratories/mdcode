# STEPS TO RUNNING A MD SIMULATION USING AN UNPARAMETERIZED MOLECULE

Resources:
* [Lemkul's ligand bound tutorial](http://www.mdtutorials.com/gmx/complex/01_pdb2gmx.html)

1. Extract the ligand from the PDB file (if obtained from RCSB) using grep.
```
grep ${LIG_ID} ${PDB_ID}.pdb > ${LIG_ID}.pdb
```
2. Check `{LIG_ID}.pdb` for irregularities using a text editor and Avogadro.
3. Open `{LIG_ID}.pdb` in Avogadro. Select `Build > Add Hydrogens`, then `Save` the hydrogenated molecule. 
4. Calculate the charge on the molecule.
    * Webserver: [webchem ChargeCalculator](https://webchem.ncbr.muni.cz/Platform/ChargeCalculator)
5. Submit your parameterization calculation to [Queensland University's tool](https://atb.uq.edu.au/index.py). It will return:
    * A GMX `.itp` file
    * (optionally) a forcefield revision compatible with nonstandard atom types.
6. Convert the ligand to a .gro file.
```
gmx editconf -f ${LIGAND_ID}.pdb -o ${LIGAND_ID}_proc.gro
```
7. Define the unit cell and fill it with water.
```
gmx editconf -f ${LIGAND_ID}_proc.gro -o ${LIGAND_ID}_in_box.gro -bt dodecahedron -d 1.0
gmx solvate -cp ${LIGAND_ID}_in_box.gro -cs spc216.gro -p topol.top -o ${LIGAND_ID}_solv.gro
```
8. Download a .mdp file.
```
wget http://www.mdtutorials.com/gmx/complex/Files/ions.mdp
```
9. Add ions as necessary.
```
wget gmx grompp -f ions.mdp -c ${LIGAND_ID}_solv.gro 
-p topol.top -o ions.tpr
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -neutral
```

Errors:
* ["No such moleculetype"](http://www.gromacs.org/Documentation/Errors?highlight=gromacs#Fatal_error.3a_No_such_moleculetype_XXX)