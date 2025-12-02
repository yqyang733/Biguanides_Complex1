for i in `seq 1 5`;do cd dup${i};python ../../mk_submit_fep_wins_Gromacs.py 30 1;cd ..;done
for i in `seq 1 5`;do cd dup${i};for j in `seq 0 29`;do sbatch job_${j}.sh;done;cd ..;done