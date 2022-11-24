import os
import re


def getCurrentDirectory():
    # Mengembalikan directory saat ini
    return os.path.dirname(os.path.realpath(__file__))


def bacaFile(NamaFile):
    # Mengembalikan Array of Char Syntax dari file NamaFile

    # Membaca File
    currentDir = getCurrentDirectory()
    f = open(os.path.join(currentDir, NamaFile), 'r')
    arr = f.readlines()
    f.close()

    # Menghilangkan Komentar Baris (Yang menggunakan //)
    output = ""
    idxLine = 0
    while idxLine < len(arr):
        if '//' not in arr[idxLine]:
            output += arr[idxLine]
        idxLine += 1

    return output


def splitSyntax(rawSyntax):
    # Memisahkan string yang terpisah oleh spasi
    processedSyntax = rawSyntax.split(" ")

    # Membuat List Separator (Terbuat dari Terminal)
    listOfSeparators = [
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
        r'\;',
        r'\(',
        r'\)',
        r'\{',
        r'\}',
        r'\[',
        r'\]',
        '\n',

        # Ini bagian operator
        r'\+',
        r'\-',
        r'\*',
        r'\/',
        r'\=',
        r'\!',
        r'\~',
        r'\%',
        r'\<',
        r'\>',
        r'\&',
        r'\|',
        r'\^',
        r'\,',
        r'\.'
    ]

    for separator in listOfSeparators:
        tempSyntax = []

        for s in processedSyntax:
            tempSyntax += re.split(rf'({separator})', s)

        processedSyntax = tempSyntax

    while '' in processedSyntax:
        processedSyntax.remove('')

    return processedSyntax


if __name__ == "__main__":
    raw = bacaFile("inputAcc.js")
    processed = splitSyntax(raw)

    for s in processed:
        if s != '\n':
            print(s)
