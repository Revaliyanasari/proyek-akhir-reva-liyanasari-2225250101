def periksa_jawaban(jawaban_pengguna, jawaban_benar):
    """Memeriksa apakah jawaban pengguna benar."""
    return jawaban_pengguna == jawaban_benar


def hitung_nilai(jumlah_benar, jumlah_soal):
    """Menghitung nilai akhir berdasarkan jawaban benar."""
    if jumlah_soal == 0:
        return 0

    nilai = (jumlah_benar / jumlah_soal) * 100
    return nilai