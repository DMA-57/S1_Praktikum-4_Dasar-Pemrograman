# Program     : denumeratorSeq.py
# Deskripsi   : Mencari apakah suatu pecahan berulang merupakan hasil 1/x
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : (24/09/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================

# denumeratorSeq: string --> string
# {denumeratorSeq(x) menerima string x berupa angka yang merupakan desimal berulang dari suatu pembagian pecahan, kemudian memeriksa apakah angka tersebut dapat membagi bilangan yang
# terdiri dari digit "9" sebanyak panjang dari x, dan mengembalikan string yang sesuai dengan hasil pemeriksaan. Jika suatu bilangan tersebut
# bernilai true ketika diperiksa, bilangan tersebut merupakan pecahan dari 1/x, jika tidak berarti bukan}

# ===========================================================================
# REALISASI

def denumeratorSeq(x):
    # Mengecek apakah bilangan 10^len(x) - 1 bisa dibagi dengan x
    if (10 ** len(x) - 1) % int(x) == 0:
        return f'Ada: {(10 ** len(x) - 1) // int(x)}'
    else:
        return 'Tidak ada'

# ===========================================================================
# APLIKASI
print(denumeratorSeq('3')) #Output -->  Ada: 3
print(denumeratorSeq('166')) #Output -->  Tidak ada
