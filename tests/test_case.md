# Dokumentasi Pengujian Generator Soal Aritmetika

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat menghasilkan soal aritmetika, memeriksa jawaban pengguna, menghitung nilai akhir, dan menangani input yang tidak valid.

## 2. Daftar Kasus Pengujian

### Test Case 1: Penjumlahan

- **Input:** Pilih operasi penjumlahan.
- **Contoh soal:** 12 + 8.
- **Hasil yang diharapkan:** Jawaban benar adalah 20.
- **Status:** Menunggu pengujian.

### Test Case 2: Pengurangan

- **Input:** Pilih operasi pengurangan.
- **Contoh soal:** 25 - 9.
- **Hasil yang diharapkan:** Jawaban benar adalah 16.
- **Status:** Menunggu pengujian.

### Test Case 3: Perkalian

- **Input:** Pilih operasi perkalian.
- **Contoh soal:** 6 * 7.
- **Hasil yang diharapkan:** Jawaban benar adalah 42.
- **Status:** Menunggu pengujian.

### Test Case 4: Pembagian

- **Input:** Pilih operasi pembagian.
- **Contoh soal:** 36 / 6.
- **Hasil yang diharapkan:** Jawaban benar adalah 6.
- **Status:** Menunggu pengujian.

### Test Case 5: Perhitungan Nilai

- **Input:** 4 jawaban benar dari 5 soal.
- **Hasil yang diharapkan:** Nilai akhir adalah 80.
- **Status:** Menunggu pengujian.

### Test Case 6: Jumlah Soal Tidak Valid

- **Input:** Masukkan jumlah soal 0 atau bilangan negatif.
- **Hasil yang diharapkan:** Program menampilkan pesan bahwa jumlah soal harus lebih dari 0 dan tidak melanjutkan latihan.
- **Status:** Menunggu pengujian.

### Test Case 7: Pilihan Operasi Tidak Valid

- **Input:** Masukkan pilihan operasi selain 1, 2, 3, atau 4.
- **Hasil yang diharapkan:** Program menampilkan pesan "Pilihan tidak valid." dan menghentikan proses latihan.
- **Status:** Menunggu pengujian.

### Test Case 8: Jawaban Bukan Bilangan Bulat

- **Input:** Masukkan teks, misalnya `abc`, ketika program meminta jawaban.
- **Hasil yang diharapkan:** Program menampilkan pesan bahwa input tidak valid dan meminta pengguna memasukkan jawaban kembali.
- **Status:** Menunggu pengujian.

## 3. Kesimpulan

Pengujian dirancang untuk memeriksa fungsi utama program dan responsnya terhadap input yang tidak valid. Status pengujian akan diperbarui berdasarkan hasil percobaan program yang sebenarnya.