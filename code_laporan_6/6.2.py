def ganjil(bawah, atas):
    if bawah < atas:  # Jika batas bawah lebih kecil, iterasi dari bawah ke atas
        angka = range(bawah, atas + 1)
    else:  # Jika batas bawah lebih besar, iterasi dari atas ke bawah
        angka = range(bawah, atas - 1, -1)

    # untuk melihat bilangan ganjil
    hasil = [i for i in angka if i % 2 != 0]

    # Cetak hasil
    print(f"hasilnya adalah: {bawah} ke {atas}: {', '.join(map(str, hasil))}")

# memanggil output
ganjil(10, 30)
ganjil(97, 82)

