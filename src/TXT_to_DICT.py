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
        if rawproduction[i][0] != "" and rawproduction[i][0][:2] != "//":
            valRaw = rawproduction[i][1].split(' | ')

            val = []
            for j in range(len(valRaw)):
                if valRaw[j] != ' ':
                    toadd = valRaw[j].split(' ')
                else:
                    toadd = [valRaw[j]]
                val.append(toadd)

            production.update({rawproduction[i][0]: val})

    production["B_OR"] = [['|']]
    production["OR"] = [['|', '|']]

    return production


if __name__ == "__main__":
    arrayOfFile = bacaFileTXT("formatgrammar.txt")
    production = separate(arrayOfFile)

    CFG_to_CNF.displayGrammar(production)
