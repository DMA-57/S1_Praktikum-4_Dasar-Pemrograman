# Program     : laluLintasLangit.py
# Deskripsi   : Fungsi menentukan status pesawat berdasarkan kondisi pesawat
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : (24/09/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================

# monitor_pesawat: 2 real > 0, real[0..100] --> string["Kecepatan Berbahaya" "Terlalu Tinggi" "Bahan Bakar Rendah" "Aman untuk Mendarat" "Berjalan Normal"]
# {monitor_pesawat(tinggi,kecepatan,bahanBakar) mengembalikan status pesawat berdasarkan kondisi pesawat (tinggi, kecepatan, dan bahanBakar)}

# ===========================================================================
# REALISASI
def monitor_pesawat(tinggi,kecepatan,bahanBakar):
    if kecepatan > 900 or kecepatan < 200: return "Kecepatan Berbahaya" 
    elif tinggi > 12000: return 'Terlalu Tinggi'
    elif bahanBakar < 20: return 'Bahan Bakar Rendah'
    elif tinggi < 5000 and kecepatan > 200 and kecepatan < 900 and bahanBakar > 50: return "Aman untuk Mendarat"
    else: return "Berjalan Normal"


# ===========================================================================
# APLIKASI
print(monitor_pesawat(4000,850,55)) #Output --> "Aman untuk Mendarat"
print(monitor_pesawat(5000,950,70)) #Output --> "Kecepatan Berbahaya"