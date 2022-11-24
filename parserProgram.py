from argparse import ArgumentParser
import sys
import BacaFile
import TXT_to_DICT
import FA
from CFG_to_CNF import CFGtoCNF
from CYK import cyk 

parser = ArgumentParser()
if (len(sys.argv)>1) :
    fileName = str(sys.argv[1])
else :
    fileName = "inputAcc.js"


Term,Var,cfg = TXT_to_DICT.separate("grammar.txt")
cnf = CFGtoCNF(cfg)

if (fileName):
    arr = BacaFile.bacaFile(fileName)
    arr = BacaFile.splitSyntax(arr)
    arr = FA.validateNonVar(arr)
    string = " ".join(arr)
    if (cyk):
        print("Accepted")
    else :
        print("Syntax Error")
    print(string)



