# def hitung_ips():
#     # Bobot nilai berdasarkan soal
#     bobot_nilai = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
#     sks_per_mk = 3  # SKS tiap mata kuliah selalu 3

#     # Meminta jumlah mata kuliah
#     jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
    
#     total_bobot = 0
#     total_sks = jumlah_mk * sks_per_mk  # Total SKS
    
#     for i in range(1, jumlah_mk + 1):
#         while True:
#             nilai = input(f"Masukkan nilai untuk mata kuliah ke-{i} (A/B/C/D): ").upper()
#             if nilai in bobot_nilai:
#                 total_bobot += bobot_nilai[nilai] * sks_per_mk
#                 break
#             else:
#                 print("Nilai tidak valid! Masukkan A, B, C, atau D.")

#     # Menghitung IPS
#     ips = total_bobot / total_sks
#     print(f"\nIndeks Prestasi Semester (IPS) Anda: {ips:.2f}")

# # Pemanggilan fungsi
# hitung_ips()


# # konversi huruf ke angka
# def huruf_ke_angka(huruf):
#     if 'A' <= huruf <= 'Z':  # Cek apakah huruf kapital
#         return ord(huruf) - ord('A') + 1
#     elif 'a' <= huruf <= 'z':  # Cek apakah huruf kecil
#         return ord(huruf) - ord('a') + 1
#     else:
#         return "Bukan huruf A-Z"

# # Contoh penggunaan
# huruf_list = ["A", "C", "Z", "B", "b"]
# for huruf in huruf_list:
#     print(f"{huruf} = {huruf_ke_angka(huruf)}")

def fibonacci_hingga_batas(batas):
    fib_minus_satu = 0
    fib_minus_dua = 1
    fib_hasil = 0
    deret = []

    while fib_hasil <= batas:
        fib_minus_dua = fib_minus_satu
        fib_minus_satu = fib_hasil
        if len(deret) < 2:
            fib_hasil = 1
        else:
            fib_hasil = fib_minus_satu + fib_minus_dua
        
        if fib_hasil <= batas:
            deret += [fib_hasil]
    return deret
# Batas nilai sudah ditentukan
batas = 200
hasil_fibonacci = fibonacci_hingga_batas(batas)
# Menampilkan hasil dengan output memanjang ke bawah
print(f"Deret Fibonacci hingga {batas}:")
for angka in hasil_fibonacci:
    print(angka)
