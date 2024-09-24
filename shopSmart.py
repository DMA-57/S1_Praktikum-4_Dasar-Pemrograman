# Program     : shopSmart.py
# Deskripsi   : Fungsi menghitung harga setelah diskon di sebuah toko
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : (24/09/2024)
# ===========================================================================

# DEFINISI DAN SPESIFIKASI
# ===========================================================================

# hargaAkhir: integer > 0, string["elektronik", "pakaian", "makanan"], boolean, string["luar negeri", "dalam negeri"], 
# string["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]  --> integer > 0
# {hargaAkhir(harga, kategori, VIP, lokasi, hari) menghitung harga setelah melalui banyak 
# perhitungan diskon dan pajak berdasarkan kategori, keanggotaan, hari, dan lokasi}

# ===========================================================================

# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
# ===========================================================================

# potonganHarga: integer > 0, integer [0..100] --> integer > 0 
# {potonganHarga(harga, diskon) menghitung harga setelah terkena diskon}

# pajakHarga: integer > 0, integer [0..100] --> integer > 0 
# {pajakHarga(harga, pajak) menghitung harga setelah terkena pajak}

# diskonKategori: integer > 0, string["elektronik", "pakaian", "makanan"], boolean --> integer > 0
# {diskonKategori(harga, kategori, VIP) menghitung potongan harga berdasarkan kategori dan keanggotaan}

#penangananHari: integer > 0, string["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"], 
# boolean, string["elektronik", "pakaian", "makanan"] --> integer > 0
#{penangananHari(harga, kategori, VIP) menghitung potongan harga atau pajak harga berdasarkan hari, kategori, dan keanggotaan}

#pajakLokasi: integer > 0, string["luar negeri", "dalam negeri"] --> integer > 0
# {pajakLokasi(harga, lokasi) menghitung harga setelah dikenakan pajak lokasi pembelian}
# ===========================================================================
#REALISASI
def potonganHarga(harga, diskon):
    """Menghitung harga setelah terkena diskon."""
    return (1 - (diskon / 100)) * harga
    
def pajakHarga(harga, pajak):
    """Menghitung harga setelah terkena pajak."""
    return (1 + (pajak / 100)) * harga

def diskonKategori(harga, kategori, VIP):
    """Menghitung potongan harga berdasarkan kategori dan status VIP."""
    if kategori == 'elektronik':
        if VIP: 
            return potonganHarga(harga, 30)  #a Diskon 30% untuk VIP
        else: 
            return potonganHarga(harga, 10)  # Diskon 10% untuk non-VIP
    elif kategori == 'pakaian':
        if VIP: 
            return potonganHarga(harga, 20)  # Diskon 20% untuk VIP
        else: 
            return potonganHarga(harga, 5)   # Diskon 5% untuk non-VIP
    elif kategori == 'makanan':
        if VIP: 
            return potonganHarga(harga, 15)  # Diskon 15% untuk VIP
        else: 
            return potonganHarga(harga, 2)   # Diskon 2% untuk non-VIP
    return harga

def penangananHari(harga, hari, VIP, kategori):
    """Menghitung potongan atau pajak berdasarkan hari pembelian."""
    if hari == 'Jumat' or (hari == 'Sabtu' and VIP):
        return potonganHarga(harga, 5)  # Potongan 5% untuk VIP pada Jumat dan Sabtu
    elif hari == 'Minggu':
        return pajakHarga(harga, 5)      # Pajak 5% pada hari Minggu
    elif hari == 'Rabu' and kategori == 'pakaian':
        return potonganHarga(harga, 5)    # Potongan 5% untuk pakaian pada Rabu
    
    return harga  # Kembalikan harga jika tidak ada potongan atau pajak

def pajakLokasi(harga, lokasi):
    """Menghitung pajak berdasarkan lokasi pembelian."""
    if lokasi == 'luar negeri':
        return pajakHarga(harga, 20)  # Pajak 20% untuk luar negeri
    else:
        return pajakHarga(harga, 10)   # Pajak 10% untuk dalam negeri

def hargaAkhir(harga, kategori, VIP, lokasi, hari):
    """Menghitung harga akhir setelah diskon dan pajak."""
    # Hitung harga setelah potongan kategori, hari, dan pajak lokasi
    return int(pajakLokasi(penangananHari(diskonKategori(harga, kategori, VIP), hari, VIP, kategori), lokasi))

# ===========================================================================

# APLIKASI
print(hargaAkhir(1000000, "elektronik", True, "dalam negeri", "Senin"))  # Output --> 770000
print(hargaAkhir(500000, "pakaian", False, "luar negeri", "Rabu"))      # Output --> 541500
