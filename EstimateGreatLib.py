# Program     : EstimateGreatLib.py
# Deskripsi   : Mencari Pengunjung Rata-rata Perpustakaan berdasarkan data
# NIM/Nama    : 24060124130055/Daffa Maulana Alfianto
# Tanggal     : (24/09/2024)
# ===========================================================================
# DEFINISI DAN SPESIFIKASI
# ===========================================================================
# EstimateGreatLib: string 8 int --> real
#{EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R) menghitung estimasi berdasarkan kondisi tertentu pada nilai X dan Y 
# terhadap batas SR (sunrise) dan SS (sunset) dan jika waktu dinilai malam hari, estimasi akan dikalikan
# dengan rasio R. Fungsi ini mengkalkulasi semua kemungkinan waktu perpustakaan 
# dan membagi estimasi dengan masing-masing partisinya }

# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
# ===========================================================================
# last3Week: string --> real
# {last3Week(hari) menerima string yang mewakili hari dalam seminggu (misalnya "senin", "selasa") dan mengembalikan rata-rata 
# pengunjung dalam tiga minggu terakhir untuk hari yang diberikan.}

# max3: 3 real --> real
# {max3(x, y, z) mencari nilai terbesar dari x, y, dan z dengan kondisional}

# min3: 3 real --> real
# {min(x, y, z) mencari nilai terkecil dari x, y, dan z dengan kondisional}

# estimation: str, 5 int -> real
# {estimation(D, X, Y, AS, AM, AIP) menghitung estimasi berdasarkan perbedaan nilai antara X dan Y 
# serta selisih antara nilai maksimum dan minimum dari tiga input angka tertentu. 
# Nilai ini dibagi dengan rata-rata tiga minggu terakhir berdasarkan hari yang diberikan. }

# ===========================================================================
# REALISASI


def last3Week(hari):
    if hari == 'senin': return (5000 + 6000 + 4000) / 3
    elif hari == 'selasa': return (7000 + 5000 + 2000) / 3
    elif hari == 'rabu': return (4500 + 3500 + 3000) / 3
    elif hari == 'kamis': return (2900 + 2100 + 2000) / 3
    elif hari == 'jumat': return (3000 + 3000 + 3000) / 3
    elif hari == 'sabtu': return (2000 + 2500 + 2300) / 3
    elif hari == 'minggu': return (1100 + 900 + 1000) / 3

def max3(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else: return z
    
def min3(x, y, z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    else: return z

def estimation(D, X, Y, AS, AM, AIP):
    return abs(Y - X) * (max3(AS, AM, AIP) - min3(AS, AM, AIP)) / last3Week(D)

def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
    if X < SR and Y > SS:
           return round((estimation(D, X, SR, AS, AM, AIP) * (R / 100)  
                      + estimation(D, SS, SR, AS, AM, AIP) + estimation(D, SS, Y, AS, AM, AIP) * (R/ 100)) / 3 , 5)
    elif X < SR and Y > SR:  
        return round((estimation(D, X, SR, AS, AM, AIP) * (R / 100)  
                      + estimation(D, SR, Y, AS, AM, AIP)) / 2 , 5)
    elif  Y > SS and X < SS: 
        return round((estimation(D, X, SS, AS, AM, AIP)  
                      + estimation(D, SS, Y, AS, AM, AIP) * (R / 100)) /2 , 5)
    elif (X < SR) or ((X > SS) and (Y < SR)) or (Y > SS):
        return round(estimation(D, X, Y, AS, AM, AIP)* (R / 100)  , 5)
    else:
        return round(estimation(D, X, Y, AS, AM, AIP) , 5)
# ===========================================================================
#Aplikasi
print(EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50)) #1.5
print(EstimateGreatLib("jumat", 23, 18, 17, 7, 2500, 6000, 5000, 60)) #3.5
print(EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75)) #3.75
print(EstimateGreatLib("rabu", 8, 20, 16, 6, 7500, 8000, 4000, 45)) #5.345454545454546
print(EstimateGreatLib("kamis", 4, 20, 18, 8, 3250, 2500, 1500, 30)) #2.9499999999999993
