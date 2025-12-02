import os
import sys
from collections import defaultdict

class topol_file():

    def __init__(self, top):

        self.title = list()
        self.moleculetype = list()
        self.atoms = list()
        self.bonds = list()
        self.pairs = list()
        self.angles = list()
        self.dihedrals = list()
        self.imp = list()
        self.restraints = list()
        
        identifier = {"[ moleculetype ]":1, "[ atoms ]":2, "[ bonds ]":3, "[ pairs ]":4, "[ angles ]":5, "[ dihedrals ]":6, "#ifdef POSRES_LIGAND":7,}
        index = 0
        flag = 0
        dihe_index = 0
        with open(top) as f:
            lines = f.readlines()

        while index < len(lines):
            line = lines[index]
            
            if line.strip() in identifier.keys():
                flag = identifier[line.strip()]
                if flag == 6:
                    dihe_index += 1
            
            if flag == 0:
                self.title.append(line)
            elif flag == 1:
                self.moleculetype.append(line)
            elif flag == 2:
                self.atoms.append(line)
            elif flag == 3:
                self.bonds.append(line)
            elif flag == 4:
                self.pairs.append(line)
            elif flag == 5:
                self.angles.append(line)
            elif flag == 6:
                if dihe_index == 1:
                    self.dihedrals.append(line)
                else:
                    self.imp.append(line)
                # dihe_index += 1
            elif flag == 7:
                self.restraints.append(line)

            index += 1

def hybrid(itp):
    
    top = topol_file(itp)
    rt = open("hybrid.itp", "w")
    rt.write("".join(top.title))
    rt.write("".join(top.moleculetype))
    for i in top.atoms:
        if i.startswith("[") or i.startswith(";") or i.startswith("\n"):
            rt.write(i)
        else:
            line = i.replace("\n", "").split()
            charge_b = float(line[6])/100
            rt.write("{:>4s} {:5s}{:3s}{:4s}{:5s}{:>4s}{:>8s}{:>9s}   {:10s}{:>8.4f}{:>9s}\n".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], "DUM_"+line[1], charge_b, line[7]))
    rt.write("".join(top.bonds))
    rt.write("".join(top.pairs))
    rt.write("".join(top.angles))
    rt.write("".join(top.dihedrals))
    rt.write("".join(top.imp))
    rt.write("".join(top.restraints))

def main():

    itp = sys.argv[1]
    hybrid(itp)

if __name__=="__main__":
    main() 