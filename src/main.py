from data_io import tampilkan_pesan, minta_jawaban
from analisis import periksa_jawaban, hitung_nilai
from utilitas import buat_soal


def main():
    tampilkan_pesan("===================================")
    tampilkan_pesan("   GENERATOR SOAL ARITMETIKA")
    tampilkan_pesan("===================================")

    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    pilihan = input("Masukkan pilihan (1-4): ")

    daftar_operasi = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/"
    }

    if pilihan not in daftar_operasi:
        tampilkan_pesan("Pilihan tidak valid.")
        return

    operasi = daftar_operasi[pilihan]

    try:
        jumlah_soal = int(input("Berapa soal yang ingin dikerjakan? "))

        if jumlah_soal <= 0:
            tampilkan_pesan("Jumlah soal harus lebih dari 0.")
            return

    except ValueError:
        tampilkan_pesan("Masukkan jumlah soal berupa bilangan bulat.")
        return

    jumlah_benar = 0
    jumlah_salah = 0

    for nomor in range(1, jumlah_soal + 1):
        soal, jawaban_benar = buat_soal(operasi)

        print(f"\nSoal nomor {nomor}: {soal}")

        jawaban_pengguna = minta_jawaban()

        if periksa_jawaban(jawaban_pengguna, jawaban_benar):
            tampilkan_pesan("Benar!")
            jumlah_benar += 1
        else:
            tampilkan_pesan(
                f"Jawaban salah. Jawaban yang benar adalah {jawaban_benar}."
            )
            jumlah_salah += 1

    nilai_akhir = hitung_nilai(jumlah_benar, jumlah_soal)

    print("\n========== HASIL LATIHAN ==========")
    print(f"Jumlah soal       : {jumlah_soal}")
    print(f"Jawaban benar     : {jumlah_benar}")
    print(f"Jawaban salah     : {jumlah_salah}")
    print(f"Nilai akhir       : {nilai_akhir:.2f}")
    print("===================================")


if __name__ == "__main__":
    main()