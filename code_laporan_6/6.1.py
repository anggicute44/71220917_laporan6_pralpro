def perkalian(a, b):# UNTUK MENDEFINISIKAN FUNGSI
    hasil = 0# menampung hasil
    for _ in range(a): #membuat nilai perulangan sebanyak a
        hasil += b #menambahkan b kedalam hasi
    
    print(f"{a} x {b} =", " + ".join([str(b)] * a), "=", hasil) #untuk menampilkan format perkalian dan hasilnya
    #" + ".join([str(b)] * a) Mengubah angka b menjadi string, lalu mengulangnya a kali dengan pemisah " + "
    return hasil


# pemanggilan
perkalian(6, 5)
perkalian(7, 10)
perkalian(3, 8)
perkalian(4, 12)
