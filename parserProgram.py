from argparse import ArgumentParser
import sys
import BacaFile
import TXT_to_DICT

parser = ArgumentParser()
fileName = str(sys.argv[1])


T,V,P = TXT_to_DICT.separate("grammar.txt")

if (fileName):
    raw = BacaFile.bacaFile(fileName)
    processed = BacaFile.splitSyntax(raw)

    #test
    for s in processed:
        if s != '\n':
            print(s)


