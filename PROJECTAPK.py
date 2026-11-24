import math
print("========================================")
print("             HITUNG HAPEKU              ")
print("========================================")

# 1. Mengambil input data HP
nama_hp = input(" MASUKKAN NAMA HP       : ")
harga_hp = float(input("HARGA HP (Rp)              : "))
biaya_pengiriman = float(input("BIAYA PENGIRIMAN (Rp) (JIKA GAADA KETIK 0 )     : "))

# 2. OPERASI ARITMATIKA 1 - PENJUMLAHAN (+)
# Menghitung total target biaya dari nol (Harga HP + Ongkir)
total_target = harga_hp + biaya_pengiriman

print("\n--- MAU NABUNG PAKE CARA APA ---")
print("1. Menabung per Hari")
print("2. Menabung per Minggu")
print("3. Menabung per Bulan")

pilihan = input("Masukkan pilihan Anda (1/2/3): ")

# Validasi dan proses berdasarkan pilihan pengguna
if pilihan == "1":
    nominal = float(input("Masukkan nominal tabungan per hari (Rp): "))
    if nominal <= 0:
        print("\n[Error] Nominal harus lebih dari 0!")
    else:
        # OPERASI ARITMATIKA 2 - PEMBAGIAN (/)
        total_hari = math.ceil(total_target / nominal)
        
        # OPERASI ARITMATIKA 3 - PERKALIAN (*) untuk menghitung total minggu
        perkiraan_minggu = total_hari / 7
        
        # OPERASI ARITMATIKA 4 - MODULUS / SISA UANG
        total_terkumpul = total_hari * nominal
        sisa_uang = total_terkumpul - total_target

        print(f"\n      HASIL TARGET CELENGAN: {nama_hp.upper()}")
        print(f"Total Target Biaya    : Rp {total_target}")
        print(f"Tabungan per Hari     : Rp {nominal}")
        print(f"Waktu yang Dibutuhkan : {total_hari} hari")
        print(f"                      (Sekitar {perkiraan_minggu} minggu / {total_hari // 30} bulan)")
        print(f"Sisa/Kelebihan Uang   : Rp {sisa_uang}")

elif pilihan == "2":
    nominal = float(input("Masukkan nominal tabungan per minggu (Rp): "))
    if nominal <= 0:
        print("\n[Error] Nominal harus lebih dari 0!")
    else:
        # OPERASI ARITMATIKA 2 - PEMBAGIAN (/) untuk mencari total minggu
        total_minggu = math.ceil(total_target / nominal)
        
        # OPERASI ARITMATIKA 3 - PERKALIAN (*) untuk mengubah minggu ke hari
        total_hari = total_minggu * 7
        
        # OPERASI ARITMATIKA 4 - MODULUS / SISA UANG
        total_terkumpul = total_minggu * nominal
        sisa_uang = total_terkumpul - total_target

        print(f"\n      HASIL TARGET CELENGAN: {nama_hp.upper()}")
        print(f"Total Target Biaya    : Rp {total_target}")
        print(f"Tabungan per Minggu   : Rp {nominal}")
        print(f"Waktu yang Dibutuhkan : ± {total_minggu} minggu")
        print(f"                      (Sekitar {total_hari} hari / {total_minggu // 4} bulan)")
        print(f"Sisa/Kelebihan Uang   : Rp {sisa_uang}")

elif pilihan == "3":
    nominal = float(input("Masukkan nominal tabungan per bulan (Rp): "))
    if nominal <= 0:
        print("\n[Error] Nominal harus lebih dari 0!")
    else:
        # OPERASI ARITMATIKA 2 - PEMBAGIAN (/) untuk mencari total bulan
        total_bulan = math.ceil(total_target / nominal)
        
        # OPERASI ARITMATIKA 3 - PERKALIAN (*) untuk mengubah bulan ke hari
        total_hari = total_bulan * 30
        
        # OPERASI ARITMATIKA 4 - MODULUS / SISA UANG
        total_terkumpul = total_bulan * nominal
        sisa_uang = total_terkumpul - total_target

        print(f"\n      HASIL TARGET CELENGAN: {nama_hp.upper()}")
        print(f"Total Target Biaya    : Rp {total_target}")
        print(f"Tabungan per Bulan    : Rp {nominal}")
        print(f"Waktu yang Dibutuhkan : ± {total_bulan} bulan")
        print(f"                      (Sekitar {total_hari} hari)")
        print(f"Sisa/Kelebihan Uang   : Rp {sisa_uang}")

else:
    print("\n[Peringatan] Pilihan tidak valid! Silakan jalankan ulang program dan pilih angka 1, 2, atau 3.")

print("\n Semangat terus menabung demi HP impian")