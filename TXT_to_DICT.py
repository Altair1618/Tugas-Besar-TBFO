from BacaFile import *
import CFG_to_CNF

def separate(array):
    production = {}
    rawproduction = []

    for i in range(len(array)):
        array[i] = array[i].replace("\n", "")
        toadd = array[i].split(' -> ')
        rawproduction.append(toadd)

    for i in range(len(rawproduction)):
        valRaw = rawproduction[i][1].split(' | ')

        val = []
        for j in range(len(valRaw)):
            if valRaw[j] != ' ':
                toadd = valRaw[j].split(' ')
            else:
                toadd = [valRaw[j]]
            val.append(toadd)

        production.update({rawproduction[i][0]: val})

    production["OR"] = [['|']]

    return production


if __name__ == "__main__":
    arrayOfFile = bacaFileTXT("formatgrammar2.txt")
    production = separate(arrayOfFile)

    CFG_to_CNF.displayGrammar(production)
