# Program     : belajarTenang.py
# Deskripsi   : Fungsi Menghitung jarak agar bisa belajar tenang dari suara boombox
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : (24/09/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================

# BelajarTenang: real >= 1 real  ≤ 1000000 --> string
# {BelajarTenang(dB, m) menghitung jarak minimum yang dibutuhkan agar suara sound system yang berjarak 15m 
# tidak lebih 40dB dan memeriksa apakah bahan bakar yang dimiliki cukup untuk mencapai jarak tersebut}

# ===========================================================================
# REALISASI

def BelajarTenang(dB, m):
    if 15 * 10 ** ((dB - 40) / 20) <= m :
        return str(round(15 * 10 ** ((dB - 40) / 20), 3)) + ' meter'
    else:
        return 'Isi bensin dulu, bang'

    # return f'{15 * 10 ** ((dB - 40) / 20):.3f} meter' if 15 * 10 ** ((dB - 40) / 20) <= m else 'Isi bensin dulu, bang'

# ===========================================================================
# APLIKASI
print(BelajarTenang(102, 20000)) #Output: 18883.881 meter
print(BelajarTenang(100, 1300)) #Output: Isi bensin dulu, bang
