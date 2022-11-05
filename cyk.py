def createInverseRules(R):
    # Fungsi membuat dictionary berisi balikan dari rules R

    # ALGORITMA
    inverseRules = {}

    for lhs, rule in R.items():
        for rhs in rule:
            for product in rhs:
                if product in inverseRules:
                    inverseRules[product] += [lhs]
                else:
                    inverseRules[product] = [lhs]

    return inverseRules


def cyk_tablefilling(IR, string):
    # Membuat Matriks yang berisi hasil penggunaan table filling algorithm
    # dengan masukan inverse rules dan string

    # ALGORITMA
    cyk_arr = []
    for i in range(len(string)):
        cyk_arr += [[]]
        if i == 0:
            # print(cyk_arr)
            for j in range(len(string)):
                cyk_arr[i] += [IR[string[j]]]
        else:
            # print(cyk_arr)
            for j in range(len(string) - i):
                cyk_arr[i] += [[]]
                # print(cyk_arr)
                for k in range(i):
                    # print(k, j)
                    for c1 in cyk_arr[k][j]:
                        for c2 in cyk_arr[i - k - 1][j + k + 1]:
                            if c1 + c2 in IR:
                                for val in IR[c1 + c2]:
                                    if val not in cyk_arr[i][j]:
                                        cyk_arr[i][j] += val

    return cyk_arr


def isDerivable(rules, string):
    # Mengembalikan apakah string bisa diderive dari rules

    # ALGORITMA
    inverseRules = createInverseRules(rules)
    arr = cyk_tablefilling(inverseRules, string)

    if 'S' in arr[-1][0]:
        return True
    else:
        return False


if __name__ == "__main__":
    # Driver CYK

    # ALGORITMA
    terminal = ["a", "b"]
    variable = ["A", "B", "C", "S"]

    Rules = {
        "S": [["AB", "BC"]],
        "A": [["BA", "a"]],
        "B": [["CC", "b"]],
        "C": [["AB", "a"]]
    }

    s = "baaba"
    if isDerivable(Rules, s):
        print("Bisa diturunkan")
    else:
        print("Tidak bisa diturunkan")
