## 对二甲双胍周围残基进行FEP计算   
从MD的最后一帧结构出发，保留除突变残基之外的其他所有结构。    
（1）创建相应文件：   
```shell
mkdir FEP_res
cd FEP_res
mkdir H92A
cd H92A
mkdir bonded;cd bonded
cp ../../../MD/MD/top* -r .
cp ../../../MD/MD/equil/step6.6_equilibration.gro .
cp step6.6_equilibration.gro frame.gro
```
（2）从gro文件中将突变的那个链单独保存出来。添加链号，并且将非标准残基2MR删除多余原子并改名称为ARG。   
（3）对选出的链进行pmx突变准备。   
```shell
pmx mutate -f PROB.pdb -o mutant.pdb --keep_resid
source /public/software/apps/gromacs/2022.2/bin/GMXRC.bash
export LD_LIBRARY_PATH=/public/software/lib/:$LD_LIBRARY_PATH
source /public/software/compiler/intel/intel-compiler-2017.5.239/bin/compilervars.sh intel64
gmx pdb2gmx -f mutant.pdb -o conf.pdb -p topol.top -water tip3p
pmx gentop -p topol.top -o newtop.top
gmx editconf -f conf.pdb -o conf.gro
```
（4）合并文件。
```shell
cp ../mut/newtop.top .
cp ../mut/posre.itp .
mv PROB.itp PROB_1.itp
cp newtop.top PROB.itp # 修改名称，删除头尾文件
# 将conf.gro和frame.gro进行合并 
# 修改topol.top的头部forcefield文件   
```
（5）生成index.ndx。
（6）生成各个副本和窗口并提交任务。
（7）free状态的话将bond状态中gro文件和topol文件中的MF8配体去掉即可。  