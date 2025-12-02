## 将二甲双胍以及氯胍进行消除FEP计算  
输入[MF8.itp](MF8.itp)，运行脚本[gen_hybrid_itp.py](gen_hybrid_itp.py)，产生hybrid.itp。    
输入[MF8_atoms.par](MF8_atoms.par)，运行脚本[gen_hybrid_par.py](gen_hybrid_par.py)，产生hybrid.par。  
bonded状态[mdp](./mdp-mem/)文件，free状态[mdp](./mdp-lig/)文件。   
free状态[topol.top](topol.top)  
产生job.sh的脚本[mk_submit_fep_wins_Gromacs.py](mk_submit_fep_wins_Gromacs.py)     
提交任务相关脚本[do.sh](do_202309191628.sh)   