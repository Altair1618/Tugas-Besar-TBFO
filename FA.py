import BacaFile


listOfSyntaxWord = [
    # Ini Terminal berupa Kata Perintah di JS
    'break',
    'continue',
    'return',
    'const',
    'var',
    'let',
    'switch',
    'case',
    'try'
    'catch',
    'finally',
    'throw',
    'default',
    'delete',
    'if',
    'else',
    'true',
    'false',
    'null',
    'for',
    'while',
    'function',

    # Ini bagian simbol-simbol di JS
    ';',
    '(',
    ')',
    '{',
    '}',
    '[',
    ']',
    '\n',

    # Ini bagian operator
    '+',
    '-',
    '*',
    '/',
    '==',
    '!',
    '~',
    '%',
    '<',
    '>',
    '&',
    '|',
    '^',
    ',',
    '.'
]


def validateNonVar(processedSyntax):
    global listOfSyntaxWord

    for index in range(len(processedSyntax)):
        if not isSyntaxWord(processedSyntax[index]):
            if '0' <= processedSyntax[index][0] <= '9':
                if numFA(processedSyntax[index]):
                    processedSyntax[index] = "validNum"
                else:
                    processedSyntax[index] = "invalidNum"
            else:
                if varAndFunFA(processedSyntax[index]):
                    processedSyntax[index] = "validName"
                else:
                    processedSyntax[index] = "invalidName"

    return processedSyntax


def varAndFunFA(string):
    # FA untuk pengecekan nama variabel dan fungsi

    # States
    # q0 : Baca Huruf Pertama
    # q1 : Final State (nama Var/Fun valid)
    # q2 : Dead State

    currentState = "q0"

    for char in string:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9' or char == '_' or char == '$'):
            currentState = "q2"
            break

        if currentState == "q0":
            currentState = "q1"

    return currentState == "q1"


def numFA(string):
    # FA untuk pengecekan angka
    # Input sudah pasti tidak kosong

    # States
    # q0 : Final State, string yang dibaca semua berisi angka
    # q1 : Dead State

    currentState = "q0"

    for char in string:
        if not '0' <= char <= '9':
            currentState = "q1"
            break

    return currentState == "q0"


def isSyntaxWord(string):
    global listOfSyntaxWord

    return string in listOfSyntaxWord


if __name__ == "__main__":
    processedSyntax = BacaFile.splitSyntax(BacaFile.bacaFile("inputAcc.js"))

    # processedSyntax = ['9---', 'An+jay', 'Woee', '$$$', '1000000', 'const']

    print(validateNonVar(processedSyntax))
