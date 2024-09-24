# Program     : jamPasir.py
# Deskripsi   : Mengformat waktu ke string (d:m:j)
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : (24/09/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================
#jam: tuple<int[0..24] int[0..59] int[0..59]> --> string       #Input tapi bukan tuple (soal doang ini)
#{jam(j,m, d) mengformat tuple waktu <j, m, d> ke dalam format ("Jam: j, Menit: m, Detik: s"), jika tuple memiliki waktu yang tidak valid akan dikembalikan 
# sebuah string 'Waktu tidak valid }
# ===========================================================================
# REALISASI

def jam(j, m, d):
    return f'Jam: {j}, Menit: {m}, Detik: {d}' if (j >= 0 and j <= 24) and ((m >= 0) and (m <= 59)) and ((d >= 0) and (d <= 59)) else 'Waktu tidak valid'
# ===========================================================================
# APLIKASI

print(jam(12,30,45)) # Output --> Jam: 12, Menit: 30, Detik: 45
print(jam(12,45,60)) # Output --> Waktu tidak valid