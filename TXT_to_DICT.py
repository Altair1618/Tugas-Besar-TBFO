from BacaFile import *

def separate(array):
    terminal = []
    variable = []
    production = {}

    raw = []

    for i in range(len(array)):
        add = [array[i]]
        raw.append(add)

    for i in range(len(raw)):
        if raw[i] == ['Terminals:\n'] :
            terminalraw = raw[i+1][0]
            terminal = terminalraw.split(' ')
            a = terminal[-1].split('\n')
            terminal.pop()
            terminal.append(a[0])

        elif raw[i] == ['Variables:\n'] :
            variableraw = raw[i+1][0]
            variable = variableraw.split(' ')
            a = variable[-1].split('\n')
            variable.pop()
            variable.append(a[0])

        elif raw[i] == ['Productions:\n'] :
            rawproduction = []

            for j in range((i+1), len(raw)):
                toaddraw = raw[j][0]
                toadd = toaddraw.split(' -> ')
                rawproduction.append(toadd)

            for j in range(len(rawproduction)) :
                valRaw = rawproduction[j][1]
                valRawRaw = valRaw.split(' | ')
                val = []
                for k in range(len(valRawRaw)):
                    if valRawRaw[k] != ' ' :
                        toadd = valRawRaw[k].split(' ')
                    else :
                        toadd = [valRawRaw[k]]
                    val.append(toadd)
                k = val[-1][0].split(';')
                val.pop()
                val.append([k[0]])
                for k in range(len(val)):
                    for y in range(len(val[k])):
                        if val[k][y] == 'or' :
                            val[k][y] = '|'
                        if val[k][y] == 'dot' :
                            val[k][y] = '.'
                        if val[k][y] == 'semicolon' :
                            val[k][y] = ';'
                        if val[k][y] == 'colon' :
                            val[k][y] = ':'
                production.update({rawproduction[j][0]:val})

    return terminal, variable, production

if __name__ == "__main__":
    arrayOfFile = bacaFileTXT("formatgrammar.txt")
    terminal, variable, production = separate(arrayOfFile)
    #print(terminal)
    #print(variable)
    print(production)
    #print(production['OTHER'])