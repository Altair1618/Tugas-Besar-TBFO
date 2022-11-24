from argparse import ArgumentParser
import sys
import BacaFile
import TXT_to_DICT

parser = ArgumentParser()
if len(sys.argv)>1:
    fileName = str(sys.argv[1])
else:
    fileName = 'grammar.txt'

T,V,P = TXT_to_DICT.separate(fileName)

inputFile = input("Input path file javascript : ")
if (inputFile):
    raw = BacaFile.bacaFile("inputAcc.js")
    processed = BacaFile.splitSyntax(raw)

    for s in processed:
        if s != '\n':
            print(s)


