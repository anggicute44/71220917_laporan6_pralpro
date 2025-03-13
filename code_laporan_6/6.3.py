def hitung_ips():
    # Bobot nilai berdasarkan soal
    bobot_nilai = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    sks_per_mk = 3  # SKS tiap mata kuliah selalu 3

    # Meminta jumlah mata kuliah
    jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
    
    total_bobot = 0
    total_sks = jumlah_mk * sks_per_mk  # Total SKS
    
    for i in range(1, jumlah_mk + 1):
        while True:
            nilai = input(f"Masukkan nilai untuk mata kuliah ke-{i} (A/B/C/D): ").upper()
            if nilai in bobot_nilai:
                total_bobot += bobot_nilai[nilai] * sks_per_mk
                break
            else:
                print("Nilai tidak valid! Masukkan A, B, C, atau D.")

    # Menghitung IPS
    ips = total_bobot / total_sks
    print(f"\nIndeks Prestasi Semester (IPS) Anda: {ips:.2f}")

# Pemanggilan fungsi
hitung_ips()






















# def buat_kalimat(kata_list):
#     kalimat = kata_list[0]  # Mulai dengan kata pertama
#     jumlah_huruf = len(kata_list[0])

#     for i in range(1, len(kata_list)):  # Mulai dari indeks ke-1
#         kalimat += " " + kata_list[i]  # Menggunakan konkatenasi string
#         jumlah_huruf += len(kata_list[i])

#     return kalimat, jumlah_huruf  # Mengembalikan hasil

# # Daftar kata yang sudah ditentukan (tanpa inputan pengguna)
# kata_list = ["Saya", "suka", "belajar", "pemrograman", "Python"]

# # Memanggil fungsi dan menyimpan hasil
# kalimat, jumlah_huruf = buat_kalimat(kata_list)

# # Menampilkan hasil
# print(f"\nKalimat yang terbentuk: {kalimat}")
# print(f"Jumlah huruf dalam kalimat: {jumlah_huruf}")

##########################

#to do list
# def tambah_kegiatan(todo_list, kegiatan):
#     return todo_list + [kegiatan]  # Menggunakan return untuk mengembalikan daftar baru

# def lihat_kegiatan(todo_list):
#     hasil = "\nDaftar Kegiatan:\n"
#     for idx in range(len(todo_list)):  # Menggunakan indeks, bukan `enumerate`
#         hasil += f"{idx + 1}. {todo_list[idx]}\n"
#     return hasil  # Menggunakan return agar bisa dipakai di tempat lain

# def main():
#     todo_list = []  # Daftar awal kosong
    
#     # Data kegiatan yang sudah ditentukan (tanpa inputan)
#     daftar_kegiatan = ["Bangun pagi", "Sarapan", "Kuliah", "Olahraga", "Belajar Python"]
    
#     # Menambahkan kegiatan satu per satu
#     for kegiatan in daftar_kegiatan:
#         todo_list = tambah_kegiatan(todo_list, kegiatan)
    
#     # Menampilkan hasil dengan return
#     hasil = lihat_kegiatan(todo_list)
#     print(hasil)

# # Jalankan program
# main()
###########
# def kategori_nilai(nilai):
#     if 85 <= nilai <= 100:
#         return "A"
#     elif 70 <= nilai < 85:
#         return "B"
#     elif 50 <= nilai < 70:
#         return "C"
#     elif 0 <= nilai < 50:
#         return "D"
#     else:
#         return "Nilai tidak valid"

# def main():
#     daftar_nilai = [95, 78, 60, 45, 110]  # Data tetap
#     for nilai in daftar_nilai:
#         print(f"Nilai: {nilai}, Kategori: {kategori_nilai(nilai)}")

# main()
###############################################


