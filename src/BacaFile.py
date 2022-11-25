import os
import re


def getCurrentDirectory():
    # Mengembalikan directory saat ini
    return os.path.dirname(os.path.realpath(__file__))


def bacaFile(NamaFile):
    # Mengembalikan Array of Char Syntax dari file NamaFile

    # Membaca File
    currentDir = getCurrentDirectory()
    f = open(os.path.join(currentDir, f"../test/{NamaFile}"), 'r')
    arr = f.readlines()
    f.close()

    # Menghilangkan Komentar Baris (Yang menggunakan //)
    output = ""
    idxLine = 0
    while idxLine < len(arr):
        if '//' not in arr[idxLine]:
            output += arr[idxLine]
        idxLine += 1

    # Menghilangkan Komentar MultiLine (Yang menggunakan /* */)
    idxLine = 0
    while idxLine < len(output) - 1:
        # print(output[idxLine:idxLine + 2])
        if (output[idxLine:idxLine + 2] == '/*'):
            # print(idxLine)
            idxSearch = idxLine + 1
            while idxSearch < len(output):
                if output[idxSearch:idxSearch + 2] == '*/':
                    # print(idxSearch)
                    break
                idxSearch += 1
            output = output[:idxLine] + output[idxSearch + 2:]
        idxLine += 1

        if output[idxLine] == '\\' and (output[idxLine + 1] == '\'' or output[idxLine + 1] == '\"' or output[idxLine + 1] == '\\'):
            output = output[:idxLine] + "escChar" + output[idxLine + 2:]
    
    # print(output)
    
    return output


def bacaFileTXT(namafile):
    # Prosedur pembacaan namafile
    # Fungsi pembacaan namafile
    # Hasil menjadi array of string

    # KAMUS
    global arraytextfile
    # f : file

    # ALGORITMA
    currentDir = getCurrentDirectory()
    f = open(os.path.join(currentDir, f"../txt/{namafile}"), 'r')
    #arraytextfile = f.readlines()
    arr = f.readlines()
    f.close()

    return arr

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

        # Untuk Escape Char
        'escChar',

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
        r'\\',
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
        r'\.',
        r'\"',
        r'\''
    ]

    for separator in listOfSeparators:
        tempSyntax = []

        for s in processedSyntax:
            tempSyntax += re.split(rf'({separator})', s)

        processedSyntax = tempSyntax

    while '' in processedSyntax:
        processedSyntax.remove('')
    
    while '\n' in processedSyntax:
        processedSyntax.remove('\n')
    
    idxFind = 0
    while idxFind < len(processedSyntax):
        idxSearch = idxFind + 1

        if processedSyntax[idxFind] == "\"":
            while idxSearch < len(processedSyntax):
                if processedSyntax[idxSearch] == "\"":
                    processedSyntax = processedSyntax[:idxFind] + ["validString"] + processedSyntax[idxSearch + 1:]
                idxSearch += 1
        
        if processedSyntax[idxFind] == "\'":
            while idxSearch < len(processedSyntax):
                if processedSyntax[idxSearch] == "\'":
                    processedSyntax = processedSyntax[:idxFind] + ["validString"] + processedSyntax[idxSearch + 1:]
                idxSearch += 1
        
        idxFind += 1

    return processedSyntax


if __name__ == "__main__":
    raw = bacaFile("inputAcc.js")
    processed = splitSyntax(raw)

    for s in processed:
        if s != '\n':
            print(s)
