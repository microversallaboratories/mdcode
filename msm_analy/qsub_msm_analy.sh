#!/bin/sh

# Give the job a name
#$ -N get_msm

# set the shell
#$ -S /bin/sh

# set working directory on all host to
# directory where the job was started
#$ -cwd

# send all process STDOUT (fd 2) to this file
#$ -o job_output.txt

# send all process STDERR (fd 3) to this file
#$ -e job_output.err

# email information
#$ -m e
 
# Just change the email address. You will be emailed when the job has finished.
#$ -M northj@oregonstate.edu

# generic parallel environment with 2 cores requested
#$ -pe orte 2

############################################<LOAD MODULES>############################################

module load python/anaconda3-5.0.0.1    # load anaconda

############################################</LOAD MODULES>###########################################

############################################<RUN COMMANDS>############################################

eval "$(command conda 'shell.bash' 'hook' 2> /dev/null)"

conda activate pyemma

#wget https://files.rcsb.org/view/6VXX.pdb

python msm_test.py

############################################</RUN COMMANDS>###########################################

############################################<UNLOAD MODULES>##########################################

module unload python/anaconda3-5.0.0.1    # load anaconda

############################################</UNLOAD MODULES>#########################################