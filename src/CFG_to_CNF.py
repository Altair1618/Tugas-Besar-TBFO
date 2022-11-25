import os
from BacaFile import getCurrentDirectory


def displayGrammar(CFG):
    for lhs, rule in CFG.items():
        print(lhs, end=" -> ")
        print(rule)


def writeCNF(CNF):
    text = ""

    for lhs, rules in CNF.items():
        text += f"{lhs} -> "

        for i in range(len(rules)):
            for j in range(len(rules[i])):
                text += rules[i][j] + " "
            if i != len(rules) - 1:
                text += "| "

        text += "\n"

    # print(text[:-1])

    currentDir = getCurrentDirectory()
    f = open(os.path.join(currentDir, "../txt/CNF.txt"), 'w')
    f.write(text[:-1])
    f.close()


def CFGtoCNF(CFG):
    # Menghilangkan Unit Production
    for lhs, rule in CFG.items():
        arr = []
        for product in rule:
            arr.append(False)
            if str.isupper(product[0]) and len(product) == 1:
                for i in range(len(CFG[product[0]])):
                    rule.append(CFG[product[0]][i])
                arr[-1] = True
        for i in range(len(arr) - 1, -1, -1):
            if arr[i]:
                rule.remove(rule[i])

    # Mengubah Produksi yang Menghasilkan 3 Variabel
    i = 1
    newGrammar = {}

    for lhs, rule in CFG.items():
        arr = []
        for product in rule:
            arr.append(False)
            if len(product) > 2:
                newGrammarRule = [product[0], product[1]]

                index = "NULL"
                for left, right in newGrammar.items():
                    if newGrammarRule in right:
                        index = left
                        break

                if index == "NULL":
                    newVar = f"T{i}"
                    i += 1
                    newGrammar[newVar] = [newGrammarRule]
                    newRule = [newVar]
                else:
                    newRule = [index]

                for j in range(2, len(product)):
                    newRule += [product[j]]

                rule.append(newRule)
                arr[-1] = True
        for j in range(len(arr) - 1, -1, -1):
            if arr[j]:
                rule.remove(rule[j])

    for lhs, rule in newGrammar.items():
        CFG[lhs] = rule

    # Mencari Variabel Penghasil Terminal
    dictVarTerm = {}
    for lhs, rule in CFG.items():
        if len(rule) == 1 and len(rule[0]) == 1:
            dictVarTerm[rule[0][0]] = lhs

    # Mensubstitusi Terminal dengan Variabel jika Productnya mengandung Variabel
    for lhs, rule in CFG.items():
        for product in rule:
            if len(product) > 1:
                for i in range(len(product)):
                    if not str.isupper(product[i][0]):
                        product[i] = dictVarTerm[product[i]]

    return CFG


if __name__ == "__main__":
    terminal = ["a", "b"]
    variable = ["A", "B", "S"]

    CFG = {
        "S": [['A', 'S', 'B'], ['A', 'B']],
        "A": [['a', 'A', 'S'], ['a', 'A'], ['a']],
        "B": [['S', 'b', 'S'], ['S', 'b'], ['b', 'S'], ['b'], ['A'], ['b', 'b']],
        "C": [['a']],
        "D": [['b']]
    }

    CNF = CFGtoCNF(CFG)
    # displayGrammar(CNF)
    writeCNF(CNF)
