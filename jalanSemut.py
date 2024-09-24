# Program     : jalanSemut.py
# Deskripsi   : Mencari jalan tercepat untuk semut mencapai gula di sisi balok
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : (24/09/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================
# jalanSemut: 3 real[1..10000] --> real
# {jalanSemut(x, y, z) mencari jalan terpendek semut dari titik (0, 0, 0) ke gula di sebuah titik (x, y, z) yang merupakan 
# titik sudut berlawanan menggunakan pergerakan diagonal dua sisi (sisi lebar & tinggi dan sisi lebar & panjang)}
# ===========================================================================
# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
# ===========================================================================
# min3: 3 real --> real
# {min(x, y, z) mencari nilai terkecil dari x, y, dan z dengan kondisional}
# ===========================================================================
# REALISASI
def min3(x, y, z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    else: return z
    
def jalanSemut(x, y, z):
    return round( min((x ** 2 + (z + y) ** 2) ** 0.5, (y ** 2 + (x + z) ** 2) ** 0.5, (z ** 2 + (x + y) ** 2 ) ** 0.5), 3)

# ===========================================================================
# APLIKASI

print(jalanSemut(3,4,5)) #Output --> 8.602
print(jalanSemut(1,2,7)) #Output --> 7.616