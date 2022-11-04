def bacafile(namafile):
    # Prosedur pembacaan namafile

    # KAMUS
    global arraytextfile

    # ALGORITMA
    f = open(namafile, 'r')
    arraytextfile = f.readlines()
    f.close()


def ignoreindentation():
    # Menghapus indentasi pada array txt file

    # KAMUS
    global arraytextfile

    # ALGORITMA
    for i in range(len(arraytextfile)):
        while len(arraytextfile[i]) > 0 and arraytextfile[i][0] == ' ':
            arraytextfile[i] = arraytextfile[i][1:]
            print(arraytextfile[i])


if __name__ == "__main__":
    # Driver Bacafile

    # KAMUS
    # arraytextfile : array of string

    # ALGORITMA
    arraytextfile = []
    bacafile("inputAcc.js")
    ignoreindentation()

    print(arraytextfile)
