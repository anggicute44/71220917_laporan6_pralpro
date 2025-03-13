#perkalian
# def tabel_perkalian(base, jumlah):
#     for i in range(1, jumlah + 1):
#         print(f"{base} x {i} = {base * i}")


#Program Membuat Kalimat dari Inputan Use
# def buat_kalimat():
#     kata_list = ""
#     jumlah_huruf = 0

#     while True:
#         kata = input("Masukkan kata (ketik 'cukup' untuk berhenti): ")
#         if kata.lower() == "cukup":
#             break
#         if kata_list:
#             kata_list += " " + kata  # Menggunakan konkatenasi string
#         else:
#             kata_list = kata
#         jumlah_huruf += len(kata)

#     print(f"\nKalimat yang terbentuk: {kata_list}")
#     print(f"Jumlah huruf dalam kalimat: {jumlah_huruf}")

# buat_kalimat()


# #Program Membuat Kalimat dari Inputan Use
# def buat_kalimat(kata_list):
#     kalimat = kata_list[0]  # Mulai dengan kata pertama
#     jumlah_huruf = len(kata_list[0])

#     for i in range(1, len(kata_list)):  # Mulai dari indeks ke-1
#         kalimat += " " + kata_list[i]  # Menggunakan konkatenasi string
#         jumlah_huruf += len(kata_list[i])

#     print(f"\nKalimat yang terbentuk: {kalimat}")
#     print(f"Jumlah huruf dalam kalimat: {jumlah_huruf}")

# # Daftar kata yang sudah ditentukan (tanpa inputan pengguna)
# kata_list = ["Saya", "suka", "belajar", "pemrograman", "Python"]

# # Memanggil fungsi
# buat_kalimat(kata_list)





# # #list
# # buah=["Apel", "Mangga", "Jeruk", "Pisang"]
# # for i in buah:
# #     print(i)

# # #tuple
# # numbers = (10, 20, 30, 40)
# # for num in numbers:
# #     print(num)
 
# #  #queue   
# # from collections import deque
# # queue = deque(["A", "B", "C", "D"])
# # while queue:
# #     print(queue.popleft())  # Mengakses dan menghapus elemen dari depan


# # #contoh bentuk perulangan for
# # nilai = 10 # jumlah perulangan

# # for i in range(nilai):
# #     print(f"Perulangan ke-{i}")#tampilkan nilai i dalam string


# # total = 2
 
# # for i in range(1, 10):  
# #     total += i  
# # print("Jumlah:", total) # output jumlah:45
# # #penjumlahan 1+2+3+4..+9


# # awal = 1
# # akhir = 20

# # # Perulangan for untuk menampilkan bilangan ganjil
# # for bilangan in range(awal, akhir + 1):  # Perulangan dari 1 sampai 20
# #     if bilangan % 2 != 0:  # Mengecek apakah bilangan ganjil (sisa bagi dengan 2 tidak nol)
# #         print(bilangan)  # Jika ganjil, cetak bilangan tersebut



# # #Menampilkan Bilangan Genap dari 60 ke 3 (Mundur)
# # for i in range(10, 1, -2):  
# #     print(i)

# # #menampilkan teks berulang kali
# # for _ in range(5):  
# #     print("selamat anda lulus")#output: selamat anda lulus (sebanyak 5kali)

# # angka = 1  #  angka mulai dari 1
# # jumlahg = 0  # untuk menghitung jumlah angka genap

# # while angka <= 20:  # Perulangan while akan berjalan selama angka ≤ 10
# #     if angka % 2 == 0:  # Mengecek apakah angka genap (sisa bagi dengan 2 == 0)
# #         jumlahg += 1  # Jika angka genap, tambahkan 1 ke jumlah_genap
# #     angka += 1  # Menambah nilai angka agar perulangan tidak berjalan selamanya

# # print("Jumlah angka genap:", jumlahg)  # Mencetak jumlah angka genap dari 1 hingga 20

# # #perulangan while menggunakan else
# # nomor = 0  
# # while nomor < 3:  # akan berulang selama nomor < 3
# #     print("mengulang ke-", nomor)  # Mencetak nilai nomor saat ini
# #     nomor += 1  # Menambah nilai nomor agar perulangan tidak berjalan selamanya
# # else:
# #     print("perulangan selesai")  # Akan dieksekusi setelah perulangan while berakhir

# #menghitung rata rata dari sebuah list
# # angka = [1, 3, 7, 9, 11]  # angka yang mau dihitung rata-ratanya
# # total = 0  # Variabel untuk menyimpan jumlah total angka dalam list
# # i = 0  # untuk perulangan while

# # while i < len(angka):  # berulang selama i kurang dari panjang list angka
# #     total += angka[i]  # Menambahkan angka pada indeks ke-i ke total
# #     i += 1  # Menambah nilai i agar bisa berhenti

# # rata_rata = total / len(angka)  # Menghitung rata-rata dengan membagi total dengan jumlah dalam ist
# # print('Rata-rata data adalah:', rata_rata)  # output:6.2

# #contoh penggunaan continue 
# # namaku = "anggrayni layuk"
# # for huruf in namaku:
# #     if huruf in "anggi":  # Jika huruf termasuk dalam string "anggi"
# #         continue  # Lewati iterasi ini (tidak mencetak huruf tersebut)
# #     print(huruf, end=" ")

# #contoh break pada perulangan for
# # for i in range(1,20):
# #   print(i,' x ',i ,' = ',i*i)
# #   if i == 5:
# #     break


# # #contoh break pada while
# # i=0
# # while i < 10:
# # 	print(i)
# # 	if i == 6:
# # 		break
# # 	i += 1


# # #perulangan for
# # for i in range(10, 0, -1):  # Dari 10 sampai 1 (mundur)
# #     print(i)
    
# # #perulangan while
# # i = 10  # Nilai awal
# # while i > 0:  # Kondisi akhir
# #     print(i)  # Cetak nilai i
# #     i = i - 1  # Step: turunkan i sebesar 1


# def perkalian(a, b):
#     hasil = 0
#     for _ in range(a):  # Menjumlahkan b sebanyak a kali
#         hasil += b
#     return hasil

# # Contoh penggunaan
# x, y = 6, 5
# print(f"{x} x {y} =", " + ".join([str(y)] * x), "=", perkalian(x, y))

# x, y = 7, 10
# print(f"{x} x {y} =", " + ".join([str(y)] * x), "=", perkalian(x, y))

# print(perkalian(6, 5))  # Seharusnya output: 30
# print(perkalian(7, 10)) # Seharusnya output: 70

# #1
# def is_prime(num):
#     """
#     Fungsi untuk mengecek apakah suatu bilangan prima atau bukan.
#     """
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# def find_closest_prime(num):
#     # """
#     # Fungsi untuk mencari bilangan prima terdekat dari suatu bilangan yang diinputkan oleh pengguna.
#     # """
#     if num <= 2:
#         return None
    
#     # Mencari bilangan prima terdekat yang lebih kecil dari n.
#     i = num - 1
#     while i > 1:
#         if is_prime(i):
#             return i
#         i -= 1

# n = int(input("Masukkan bilangan: "))
# closest_prime = find_closest_prime(n)
# if closest_prime is None:
#     print("Tidak ada bilangan prima yang lebih kecil dari", n)
# else:
#     print("Bilangan prima terdekat dari", n, "adalah", closest_prime)
# #1

#membuat segitiga kekiri
# def cetak_pola(n):
#     for i in range(n):
#         hasil = 1
#         for j in range(n - i):
#             hasil *= (j + 1)
#         print(hasil, end=' ')
#         for k in range(n - i, 0, -1):
#             print(k, end=' ')
#         print()

# # Input dari pengguna
# n = int(input("Masukkan nilai n: "))
# cetak_pola(n)

#2

# #membuat persegi
# def persegi(tinggi, lebar):

#     n = tinggi*lebar
#     for i in range(n):
#         print(i+1, end=" ")
#         if (i+1) % lebar == 0:
#             print()
# persegi(5, 4)

##soal fibonaci
#Menampilkan Deret Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def main():
    n = 10  # Jumlah bilangan Fibonacci yang tetap
    print(f"Deret Fibonacci {n} bilangan pertama:")
    fibonacci(n)

main()

## menentukan
def fibonacci(bil):
    fibo_minus_satu = 0
    fibo_minus_dua = 0
    fibo_hasil = 0
    for x in range(1, bil + 1):
        fibo_minus_dua = fibo_minus_satu
        fibo_minus_satu = fibo_hasil
        if x <= 2:
            fibo_hasil = 1
        else:
            fibo_hasil = fibo_minus_satu + fibo_minus_dua
    return fibo_hasil

# Nilai n sudah ditentukan tanpa input pengguna
angka = 6  # Ubah sesuai kebutuhan
fibonacci_bil = fibonacci(angka)
print(f'Bilangan Fibonacci ke-{angka} adalah {fibonacci_bil}')

