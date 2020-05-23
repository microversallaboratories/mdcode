## PREAMBLE

TITLE: fxr_feature_discovery_usl.md
PURPOSE: To plan the creation of software and sequence of analyses to determine key structural features of drugs binding to the farnesoid X receptor (FXR)
PROJECT: Applying unsupervised deep learning to molecular dynamics trajectories to determine key features of ligands activating the Farnesoid X receptor (FXR)
AUTHOR: Jacob Lloyd North
INSTITUTION: Oregon State University

## 1. PROBLEM STATEMENT

- ASSUMPTIONS

## 2. PSEUDOCODE DESIGN

## 3. IMPLEMENTATION DETAILS
- Bioinformatics
    - CATH database: http://www.cathdb.info/
- Python Libraries (pip3)
    - MDAnalysis: https://www.mdanalysis.org/MDAnalysisTutorial/index.html
    - 
- Molecular dynamics algorithm
    - GROMACS
    - AutoDock
    - OpenMM
    - Online servers to determine normal modes
        - NMSim - Normal mode detection: http://cpclab.uni-duesseldorf.de/nmsim/
    - MoDEL - Library of MD sims: http://mmb.pcb.ub.es/MoDEL/index.jsf
- Machine learning algorithms
    - Python Jupyter notebooks
    - Fast.ai / PyTorch will be used for the unsupervised learning algorithm
- Analysis
    - Will be implemented using Python Jupyter notebooks

## 4. PROGRAM TEST CASES
