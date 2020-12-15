#!/bin/sh

# Give the job a name
#$ -N get_structnets

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

module load python/anaconda3-latest

############################################</LOAD MODULES>###########################################

############################################<RUN COMMANDS>############################################

bash get_structnets.sh	# Call emin

############################################</RUN COMMANDS>###########################################

############################################<UNLOAD MODULES>##########################################

module unload python/anaconda3-latest

############################################</UNLOAD MODULES>#########################################