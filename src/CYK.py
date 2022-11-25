import CFG_to_CNF
import os


def displayCYK(cyk_arr):
    for row in cyk_arr:
        print(row)

        
def writeCYK(cyk_arr):
    text = ""

    for row in cyk_arr:
        text += f"{row}\n"

    # print(text[:-1])

    currentDir = CFG_to_CNF.getCurrentDirectory()
    f = open(os.path.join(currentDir, "../txt/CYK_ARR.txt"), 'w')
    f.write(text)
    f.close()


def cyk(cnf, string):
    # print(string)
    a = []

    for i in range(len(string)):
        a += [[]]

        # Membuat Tabel Baris Pertama dengan Mencari Pembentuk Variabel
        if i == 0:
            for j in range(len(string)):
                a[i] += [[]]
                for lhs, rule in cnf.items():
                    for product in rule:
                        if string[j] in product:
                            a[i][j] += [lhs]

        # Membuat Tabel Baris Selanjutnya dengan Konsep Table Filling Algorithm pada CYK
        else:
            for j in range(len(string) - i):
                a[i] += [[]]
                for k in range(i):
                    for lhs, rule in cnf.items():
                        for product in rule:
                            if len(product) != 2:
                                continue
                            if product[0] in a[k][j] and product[1] in a[i - k - 1][j + k + 1]:
                                if lhs not in a[i][j]:
                                    a[i][j] += [lhs]

    # Untuk Testing
    writeCYK(a)

    return 'S' in a[-1][0]


if __name__ == "__main__":
    # Driver CYK

    # ALGORITMA
    terminal = ["a", "b"]
    variable = ["A", "B", "C", "S"]

    # Rules = {
    #     "S": [['A', 'B'], ['B', 'C']],
    #     "A": [['B', 'A'], ['a']],
    #     "B": [['C', 'C'], ['b']],
    #     "C": [['A', 'B'], ['a']]
    # }

    Rules = {
        "S": [['Var 1', 'Var 2'], ['Var 2', 'Var 3']],
        "Var 1": [['Var 2', 'Var 1'], ['term1']],
        "Var 2": [['Var 3', 'Var 3'], ['term2']],
        "Var 3": [['Var 1', 'Var 2'], ['term1']]
    }

    # string = "b a a b a"
    string = "term2 term1 term1 term2 term1"

    s = string.split(" ")

    if cyk(Rules, s):
        print("Bisa diturunkan")
    else:
        print("Tidak bisa diturunkan")
