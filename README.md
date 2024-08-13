# Laporan Proyek Machine Learning - Duta Kukuh Pribadi

## Project Overview

Perusahaan E-commerce seperti Amazon menggunakan berbagai sistem rekomendasi untuk memberikan saran kepada pelanggan. Saat ini, Amazon menggunakan penyaringan kolaboratif item-item, yang dapat menangani dataset besar dan menghasilkan sistem rekomendasi berkualitas tinggi secara real-time. dengan pertimbangan kemajuan dunia modern , kita dibanjiri dengan data, dan data ini memberikan kita informasi yang berguna. Namun, tidak mungkin bagi pengguna untuk mengekstrak informasi yang menarik bagi mereka dari data tersebut. Untuk membantu pengguna menemukan informasi tentang produk, sistem rekomendasi dikembangkan. Sistem ini adalah jenis sistem penyaringan informasi yang bertujuan untuk memprediksi "rating" atau preferensi yang diminati oleh pengguna.

**REFERENSI**

[Ups and downs: Modeling the visual evolution of fashion trends with one-class collaborative filtering](https://dl.acm.org/doi/abs/10.1145/2872427.2883037)

## Business Understanding

Dengan melihat project overview , dapat dijelaskan business understanding sebagai berikut

### Problem Statements

Problem statement projek ini akan dijabarkan sebagai berikut

- Bagaimana kita bisa model sistem rekomendasi agar bisa membantu user dalam mencari produk yang benar ?
- Bagaimana kita bisa produk yang bisa menaikan engagement berdasarkan sistem rekomendasi ?

### Goals

Tujuan dari projek ini dijabarkan sebagaimana berikut

- Untuk mengetahui pembuatan sistem rekomendasi agar bisa membantu user dalam mencari produk yang benar
- Untuk mengetahui pembuatan produk yang bisa menaikan engagement berdasarkan sistem rekomendasi

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

### Solution statements

Permasalahan dan tujuan di atas , bisa di selesaikan dengan hipotesa sebagai berikut

- Membuat Sistem rekomendasi menciptakan kesamaan antara pengguna dan item serta memanfaatkan kesamaan tersebut untuk memberikan rekomendasi berdasarkan tipe Rekomendasi sistem bernama Collaborative Filtering yang mana model Ini didasarkan pada asumsi bahwa orang menyukai hal-hal yang mirip dengan hal-hal lain yang mereka sukai, dan hal-hal yang disukai oleh orang lain dengan selera yang serupa.

## Data Understanding

Paragraf awal bagian ini menjelaskan informasi mengenai jumlah data, kondisi data, dan informasi mengenai data yang digunakan. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya, uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:

Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:

- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:

- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

## Data Preparation

Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling

Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation

Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_

- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
