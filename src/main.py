from argparse import ArgumentParser
import sys
import BacaFile
import TXT_to_DICT
import FA
from CFG_to_CNF import CFGtoCNF
from CYK import cyk 

if __name__ == "__main__":
    parser = ArgumentParser()
    if (len(sys.argv)>1) :
        fileName = str(sys.argv[1])
    else :
        fileName = "inputAcc.js"

    cfg_raw = BacaFile.bacaFileTXT("formatgrammar.txt")
    cfg = TXT_to_DICT.separate(cfg_raw)
    print(cfg)
    
    cnf = CFGtoCNF(cfg)

    if (fileName):
        arr = BacaFile.bacaFile(fileName)
        arr = BacaFile.splitSyntax(arr)
        arr = FA.validateNonSyntaxWord(arr)
        print(arr)
        if (cyk(cnf,arr)):
            print("Accepted")
        else :
            print("Syntax Error")
