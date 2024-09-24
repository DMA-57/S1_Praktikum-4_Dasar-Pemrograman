# Program     : gradienMagis.py
# Deskripsi   : Fungsi menghitung gradien dari suatu fungsi 3x^2 + 2x - 5
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : (24/09/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================

#gradien: 2 real, real1 != real2 --> real 
#{gradien(a, b) menghitung gradien garis dari dua garis, garis pertama memiliki absis a dan ordinat yang didapatkan dari fungsi 3x^2 + 2x - 5 
# dan garis kedua memiliki nilai absis b dan ordinat yang didapatkan dari fungsi 3x^2 + 2x - 5 }

# ===========================================================================
# REALISASI

def gradien(a, b):
    return ((3 * (a ** 2)  +  2 * a - 5) - (3 * (b ** 2) + 2 * b - 5)) / (a  - b)


# ===========================================================================
# APLIKASI
print(gradien(3,1)) #Output --> 14.0
print(gradien(2,4)) #Output --> 20.0