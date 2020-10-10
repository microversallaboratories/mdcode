#!/bin/sh

 grep -n 'MODEL\|ENDMDL' $1.pdb | cut -d: -f 1 | \
 awk '{if(NR%2) printf "sed -n %d,",$1+1; else printf "%dp models.pdb > model_%03d.pdb\n", $1-1,NR/2;}' |  bash -sf
