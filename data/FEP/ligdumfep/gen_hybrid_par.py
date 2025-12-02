import os
import sys
from collections import defaultdict

def hybrid(par):
    
    with open(par) as f:
        f1 = f.readlines()

    rt = open("hybrid.par", "w")
    for i in f1:
        if i.startswith("[") or i.startswith(";") or i.startswith("\n"):
            rt.write(i)
        else:
            line = i.replace("\n", "").split()
            epsilon = float(line[6])/100
            rt.write("{:10s}{:>4s}{:>10s}{:>5s}{:>3s}{:>17s}{:>12.6f}\n".format("DUM_"+line[0], line[1], line[2], line[3], line[4], line[5], epsilon))
    rt.close()

def main():

    par = sys.argv[1]
    hybrid(par)

if __name__=="__main__":
    main() 