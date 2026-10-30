# GENERATOR SOAL ARITMETIKA BERBASIS PYTHON
*PROPOSAL PROYEK AKHIR*

## 1. Judul Proyek

Perancangan Program Generator Soal Aritmetika Berbasis Python sebagai Media Latihan Operasi Hitung.

## 2. Latar Belakang

Operasi hitung merupakan salah satu keterampilan dasar yang penting dalam pembelajaran matematika. Untuk menguasai keterampilan tersebut, siswa memerlukan latihan yang cukup agar dapat memahami dan menerapkan operasi penjumlahan, pengurangan, perkalian, dan pembagian dengan baik.

Salah satu cara untuk mendukung kegiatan latihan adalah dengan memanfaatkan program komputer sederhana yang dapat menghasilkan soal secara otomatis. Melalui program tersebut, pengguna dapat mengerjakan soal, memeriksa ketepatan jawaban, dan mengetahui hasil latihan yang telah dilakukan.

Berdasarkan hal tersebut, dirancang sebuah program Generator Soal Aritmetika menggunakan bahasa pemrograman Python. Program ini direncanakan dapat menghasilkan soal operasi hitung secara acak, menerima jawaban pengguna, memeriksa kebenaran jawaban, serta menampilkan rekap hasil latihan. Proyek ini juga menjadi penerapan konsep algoritma dan pemrograman dalam mengembangkan solusi sederhana untuk mendukung pembelajaran matematika.

## 3. Pengguna dan Tujuan Program

### 3.1 Pengguna

Pengguna yang menjadi sasaran program ini adalah siswa yang sedang mempelajari operasi hitung dasar serta membutuhkan latihan soal aritmetika.

### 3.2 Tujuan

Program ini dirancang dengan tujuan:
1. Menyediakan latihan operasi hitung dasar melalui program komputer.
2. Menghasilkan soal aritmetika secara acak.
3. Memeriksa kebenaran jawaban yang dimasukkan pengguna.
4. Menghitung dan menampilkan nilai akhir latihan.
5. Menerapkan konsep algoritma dan pemrograman Python dalam konteks pembelajaran matematika.

## 4. Batasan Ruang Lingkup

Agar proyek dapat diselesaikan sesuai dengan ruang lingkup yang ditetapkan, program dibatasi pada hal-hal berikut:
1. Program berjalan melalui terminal atau konsol.
2. Operasi hitung yang digunakan meliputi penjumlahan, pengurangan, perkalian, dan pembagian.
3. Bilangan yang digunakan merupakan bilangan bulat.
4. Soal dibuat secara acak oleh program.
5. Pengguna memasukkan jawaban untuk setiap soal.
6. Program memeriksa jawaban dan menghitung nilai akhir berdasarkan jumlah jawaban benar.
7. Program tidak menggunakan basis data atau layanan eksternal.

## 5. Kebutuhan Program

### 5.1 Kebutuhan Fungsional

Program diharapkan mampu:
1. Menampilkan menu operasi aritmetika.
2. Menerima pilihan operasi dari pengguna.
3. Menghasilkan soal berdasarkan operasi yang dipilih.
4. Menerima jawaban pengguna.
5. Membandingkan jawaban pengguna dengan jawaban yang benar.
6. Menghitung jumlah jawaban benar dan salah.
7. Menampilkan rekap hasil latihan dan nilai akhir.

### 5.2 Kebutuhan Perangkat dan Perangkat Lunak

Perangkat dan perangkat lunak yang digunakan meliputi:
- Komputer atau laptop.
- Python.
- Visual Studio Code.
- Git.
- GitHub.

## 6. Rancangan IPO (Input, Process, Output)

### 6.1 Input

Data yang dimasukkan atau digunakan oleh program:
- Pilihan operasi aritmetika.
- Jawaban yang dimasukkan pengguna.
- Jumlah soal yang akan dikerjakan.

### 6.2 Process

Proses yang dilakukan program:
1. Menampilkan pilihan operasi aritmetika.
2. Menerima pilihan operasi dari pengguna.
3. Menghasilkan soal secara acak sesuai operasi yang dipilih.
4. Meminta pengguna memasukkan jawaban.
5. Memeriksa kebenaran jawaban.
6. Menghitung jumlah jawaban benar dan salah.
7. Menghitung nilai akhir.
8. Menampilkan rekap hasil latihan.

### 6.3 Output

Keluaran yang dihasilkan program:
- Soal aritmetika yang harus dikerjakan.
- Informasi benar atau salah untuk setiap jawaban.
- Jumlah jawaban benar dan salah.
- Nilai akhir latihan.

## 7. Algoritma dan Pseudocode

Berikut rancangan algoritma program:

```text
MULAI

Tampilkan menu operasi aritmetika
Minta pengguna memilih operasi
Minta pengguna menentukan jumlah soal

Inisialisasi jumlah benar = 0
Inisialisasi jumlah salah = 0

ULANGI sebanyak jumlah soal:
    Buat soal secara acak sesuai operasi
    Tampilkan soal
    Minta jawaban pengguna

    JIKA jawaban pengguna sama dengan jawaban benar:
        Tampilkan "Jawaban benar"
        Tambahkan jumlah benar
    JIKA TIDAK:
        Tampilkan "Jawaban salah"
        Tambahkan jumlah salah
    AKHIR JIKA
AKHIRI PENGULANGAN

Hitung nilai akhir
Tampilkan jumlah benar
Tampilkan jumlah salah
Tampilkan nilai akhir

SELESAI
```

## 8. Rancangan Struktur Program

Program direncanakan menggunakan beberapa file Python agar setiap bagian memiliki tanggung jawab yang jelas.

| Nama File | Fungsi |
|---|---|
| `main.py` | Mengatur alur utama program dan menghubungkan fungsi-fungsi lainnya. |
| `data_io.py` | Menangani masukan pengguna dan tampilan informasi. |
| `analisis.py` | Memeriksa jawaban dan menghitung nilai akhir. |
| `utilitas.py` | Menyediakan fungsi untuk menghasilkan soal aritmetika secara acak. |

## 9. Rancangan Struktur Data

Struktur data yang direncanakan meliputi:
1. **Integer:** menyimpan bilangan yang digunakan dalam operasi aritmetika, jumlah soal, jumlah jawaban benar, dan jumlah jawaban salah.
2. **String:** menyimpan pilihan operasi dan jawaban yang dimasukkan pengguna sebelum diproses.
3. **Boolean:** menunjukkan apakah jawaban pengguna benar atau salah.
4. **Tuple:** menyimpan pasangan soal dan jawaban benar yang dikembalikan oleh fungsi pembuat soal.

Struktur data tersebut dipilih karena sesuai dengan kebutuhan program yang sederhana dan berfokus pada latihan operasi hitung dasar.

## 10. Rencana Kasus Pengujian

| No. | Kasus Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | Penjumlahan | 12 + 8 | Jawaban benar adalah 20. |
| 2 | Pengurangan | 25 - 9 | Jawaban benar adalah 16. |
| 3 | Perkalian | 6 × 7 | Jawaban benar adalah 42. |
| 4 | Pembagian | 36 ÷ 6 | Jawaban benar adalah 6. |
| 5 | Perhitungan nilai | 4 jawaban benar dari 5 soal | Nilai akhir adalah 80. |

Kasus pengujian tersebut merupakan rancangan awal untuk memeriksa kebenaran operasi aritmetika dan perhitungan nilai. Pengujian aktual akan dilakukan setelah implementasi program selesai.

## 11. Rencana Pengerjaan Individu

Karena proyek dikerjakan secara individu, seluruh kegiatan perancangan, implementasi, pengujian, dokumentasi, dan penyempurnaan program menjadi tanggung jawab pengembang.

Rencana pekerjaan meliputi:
1. Menentukan permasalahan dan tujuan program.
2. Menyusun rancangan IPO dan pseudocode.
3. Menyiapkan struktur folder dan dokumentasi proyek.
4. Mengimplementasikan fungsi pembuat soal aritmetika.
5. Mengimplementasikan pemeriksaan jawaban dan perhitungan nilai.
6. Mengintegrasikan fungsi-fungsi ke dalam program utama.
7. Melakukan pengujian dan memperbaiki kesalahan.
8. Menyelesaikan dokumentasi dan repositori GitHub.

## 12. Jadwal Pengerjaan

| Tahap | Kegiatan | Target |
|---|---|---|
| 1 | Perancangan proyek dan struktur folder | Rancangan proyek tersedia. |
| 2 | Implementasi fungsi-fungsi Python | Fungsi dasar selesai dibuat. |
| 3 | Integrasi program utama | Program dapat menjalankan alur latihan. |
| 4 | Pengujian program | Hasil program dibandingkan dengan hasil yang diharapkan. |
| 5 | Dokumentasi dan penyempurnaan | Dokumentasi dan repositori proyek selesai. |

Jadwal pelaksanaan akan disesuaikan dengan batas waktu pengumpulan tugas yang ditetapkan dosen.

## 13. Repositori Proyek

URL repositori GitHub:

[Isi dengan URL repositori GitHub setelah repositori dibuat.]

## Penutup

Proyek Generator Soal Aritmetika Berbasis Python dirancang sebagai program sederhana untuk mendukung latihan operasi hitung dasar. Melalui proyek ini, konsep algoritma, fungsi, struktur data, pengulangan, percabangan, dan pengujian program akan diterapkan dalam konteks pembelajaran matematika.

Rancangan ini menjadi dasar untuk tahap implementasi, pengujian, dan penyempurnaan program berikutnya.
