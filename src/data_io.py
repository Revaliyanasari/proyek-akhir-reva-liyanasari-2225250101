def tampilkan_pesan(pesan):
    """Menampilkan pesan kepada pengguna."""
    print(pesan)


def minta_jawaban():
    """Meminta jawaban berupa bilangan bulat dari pengguna."""
    while True:
        try:
            jawaban = int(input("Masukkan jawaban Anda: "))
            return jawaban
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")