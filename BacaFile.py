def bacafile(namafile):
    # Fungsi pembacaan namafile
    # Hasil menjadi array of string

    # KAMUS
    # f : file

    # ALGORITMA
    f = open(namafile, 'r')
    arr = f.readlines()
    f.close()

    return arr


def ignoreindentation(arr):
    # Menghapus indentasi pada array

    # KAMUS

    # ALGORITMA
    for i in range(len(arr)):
        while len(arr[i]) > 0 and arr[i][0] == ' ':
            arr[i] = arr[i][1:]
            print(arr[i])

    return arr


if __name__ == "__main__":
    # Driver Bacafile

    # KAMUS
    # arraytextfile : array of string

    # ALGORITMA
    arraytextfile = bacafile("inputAcc.js")
    ignoreindentation(arraytextfile)

    print(arraytextfile)
