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

Dataset ini adalah versi terbaru dari dataset ulasan Amazon yang dirilis pada tahun 2014. Seperti pada versi sebelumnya, dataset ini mencakup ulasan beberapa atribut, dengan pembaharuan sebagai berikut.

Lebih banyak ulasan:
Jumlah total ulasan adalah 233,1 juta (142,8 juta pada tahun 2014).
Ulasan yang lebih baru:
Data saat ini mencakup ulasan dalam rentang waktu Mei 1996 - Oktober 2018.

**REFERENSI DATASET**
[Amazon Product Review](http://jmcauley.ucsd.edu/data/amazon/).

Variabel-variabel pada Amazon Product Review dataset adalah sebagai berikut:

1. **userId (object)**: Kolom ini berisi data yang menunjukkan ID pengguna, disimpan sebagai tipe data `object`. Dalam Pandas, tipe `object` biasanya digunakan untuk teks atau string, meskipun juga dapat digunakan untuk tipe data campuran.

2. **productId (object)**: Kolom ini berisi data yang menunjukkan ID produk, juga disimpan sebagai tipe data `object`. Sama seperti `userId`, tipe ini digunakan untuk teks atau string.

3. **Rating (float64)**: Kolom ini berisi data yang menunjukkan penilaian atau rating yang diberikan pengguna terhadap produk, disimpan sebagai tipe data `float64`. Tipe `float64` adalah tipe data angka desimal dalam Pandas, yang memungkinkan penyimpanan nilai desimal dengan presisi tinggi.

4. **timestamp (int64)**: Kolom ini berisi data yang menunjukkan waktu (biasanya dalam format Unix timestamp) saat penilaian diberikan, disimpan sebagai tipe data `int64`. Tipe `int64` adalah tipe data bilangan bulat (integer) 64-bit dalam Pandas, yang memungkinkan penyimpanan angka yang sangat besar.

tahapan selanjutnya yaitu mencari informasi jumlah data dalam tiap attribut

| Column    | Non-Null Count   | Dtype   |
| --------- | ---------------- | ------- |
| userId    | 1048576 non-null | object  |
| productId | 1048576 non-null | object  |
| Rating    | 1048576 non-null | float64 |
| timestamp | 1048576 non-null | int64   |

Karena nilai rating adalah yang dilihat ,maka dilakukanlah observasi statistikal rating terlebih dahulu

| count | 1.048576e+06 |
| mean | 3.973380e+00 |
| std | 1.399329e+00 |
| min | 1.000000e+00 |
| 25% | 3.000000e+00 |
| 50% | 5.000000e+00 |
| 75% | 5.000000e+00 |
| max | 5.000000e+00 |

nilai rating minimal yang diberikan adalah 1 dengan nilai maksimal yang bernilai 5
terlihat bahwa sebagian besar nilai rating berniali 5

### Handling Missing Value

terlihat bahwa tidak ada data yang hilang dari semua fitur

| Feature   | Null Value |
| --------- | ---------- |
| userId    | 0          |
| productId | 0          |
| Rating    | 0          |
| timestamp | 0          |

**Unique Users and Products**

Total no of ratings : 1048576
Total No of Users : 786330
Total No of products : 61894

melihat nilai unik pada 3 fitur yang akan dibuat menjadi parameter pembuat model. dan karena fitur `TimeStamp` tidak diperlukan, makanya dilakukan penghapusan atau drop fitur tersebut

### Visualisasi Data

1. **Persebaran Feature nilai Rating**
   disini kita melihat berapa banyak persebaran distribusi nilai rating dan banyaknya nilai rating tersebut

![Distribusi_columns_rating](https://github.com/user-attachments/assets/06427ea5-d0f5-4b59-903c-6b0bc8f2a6e0)

- Rating niali 1 memiliki total lebih dari 10.000
- Rating nilai 2 memiliki total kurang dari 10.000
- Rating nilai 3 memiliki total kurang dari 10.000 tetapi lebih dari total rating nilai 2
- Rating nilai 4 memiliki total kurang dari 20.000
- Rating nilai 5 memiliki total kurang dari 50.000

2. **Analisa userId dan banyaknya rating**
   | userId | Total Rating |
   | -------------- | ------------ |
   | A5JLAU2ARJ0BO | 412 |
   | A231WM2Z2JL0U3 | 249 |
   | A25HBO5V8S8SEA | 164 |
   | A6FIAB28IS79 | 146 |
   | AT6CZDCP4TRGA | 128 |

Dengan visualisasi sebagai berikut

![Top_10_pengguna_terbanyak](https://github.com/user-attachments/assets/54f7e9b2-5fae-41e6-b878-c238ddf72370)

dari visualisasi, dilakukan observasi untuk mencari 10 `userId` dengan ulasan atau `rating` terbanyak

3. **Distribution of Quantile**

![quantile_pengguna](https://github.com/user-attachments/assets/a6653bfb-6c43-416a-9c96-602da2d9747b)

Dalam konteks pemahaman data (data understanding), nilai kuantil 1 (sering disebut juga sebagai kuartil pertama atau Q1) adalah nilai di bawah yang 25% dari data dalam suatu distribusi berada. Ini berarti bahwa 25% dari data dalam sampel atau populasi berada di bawah nilai ini, dan 75% berada di atasnya.

Grafik ini menunjukkan bahwa distribusi rating pengguna sangat tidak merata. Sebagian kecil pengguna memberikan banyak sekali rating (yang terlihat dari lompatan curam di akhir grafik), sementara sebagian besar pengguna memberikan rating dalam jumlah kecil.

dengan begitu , dilakukan observasi untuk melihat berapa banyak produk atau `userId` yang mempunyai total rating lebih dari 50

```Powershell
No of rated product more than 50 per user : 38
```

4. **DataFrame Baru new_df**

dengan melihat average rating productnya, dilakukanlah pengurutan secara ascending

| productId  | AverageRating |
| ---------- | ------------- |
| B0000DYV9H | 4.947368      |
| B000053HC5 | 4.945783      |
| B00009R96C | 4.885714      |
| B00005LE76 | 4.879310      |
| B000I1X3W8 | 4.869565      |

dengan begitu dilakukan pembuatan dataframe yang memuat user yang sudah memberi 50 rating atau lebih dengan visualisasi `rating_mean_counts`, yaitu sebuah variable baru yang mengumpulkan total rating dari mean di yang dihasilakn oleh `productId` dan `Rating`. visualisasi ditampilkan sebagai berikut

![rating_mean_count](https://github.com/user-attachments/assets/5c507197-c8db-481d-811f-0bee57a38a9d)

Berikut adalah penjelasan parameter sumbu x dan y:

- **Sumbu X (x-axis):** Menampilkan **jumlah rating** yang diterima oleh produk (yaitu `rating_counts`). Ini adalah jumlah ulasan atau penilaian yang telah diberikan untuk setiap produk.
- **Sumbu Y (y-axis):** Menampilkan **frekuensi** atau jumlah produk yang memiliki jumlah rating tertentu. Ini menunjukkan berapa banyak produk yang memiliki sejumlah ulasan tertentu.

Jadi, grafik ini menunjukkan distribusi jumlah rating yang diterima oleh produk. Misalnya, jika banyak produk memiliki sedikit ulasan, kita akan melihat lebih banyak batang di sisi kiri grafik.

![rating_per_pRODUCT](https://github.com/user-attachments/assets/43c19ae3-9bed-43da-bab5-9ed7cf1064d3)

selanjutnya dari dataframe yang baru, dilakukan observasi persebaran banyaknya nilai rating dari skala 1 sampai 5

![point_rating_distribution](https://github.com/user-attachments/assets/de2c875e-a04b-4eea-b1e7-83dcea14c742)

dengan tujuan ingin melihat persebaran lebih presisi, library `joinplot` diperlukan

![point_rating_distribution2](https://github.com/user-attachments/assets/1ff14562-aae8-4648-8bb3-34b8c63ce72a)

melihat lagi banyak rating per produk dari `new_df`

![most_popular_produk](https://github.com/user-attachments/assets/58a9dc3c-03b4-43de-9705-d1742601c2db)

## Data Preparation

untuk data preparasi, Teknik yang digunakan dalam data preparation yaitu reading dan splitting dataset

`trainset` dan `testset` dibagi menjadi dua dengan perbandingan

- **`trainset`** : 70% dari new_df
- **`testset`** : 30% dari new_df
  penggunaan `trainset` dan `testset` bertujuan agar setelah model dibuat dari trainset tersebut, model tersebut akan di evaluasi dengan cara di uji coba lewat `testset`

## Modeling

merujuk pada artikel

[Adaptive KNN-Based Extended Collaborative Filtering Recommendation Services](https://www.mdpi.com/2504-2289/7/2/106#:~:text=The%20KNN%2Dbased%20collaborative%20filtering%20algorithm%20is%20a%20type%20of,users%20to%20the%20target%20user.)

dengan referensi tersebut , dalam menggenerasi Top-N recommendations dilakukan dengan cara membuat model K-NN

K-Nearest Neighbors (KNN) adalah algoritma yang bekerja dengan mencari data poin yang paling mirip atau "tetangga terdekat" dalam suatu ruang fitur. Dalam konteks **collaborative filtering** untuk rekomendasi, KNN dapat digunakan untuk memprediksi preferensi pengguna terhadap item berdasarkan preferensi pengguna lain atau item lain yang mirip.

**Cara Kerja KNN dalam Collaborative Filtering:**

1. **Definisi Tetangga Terdekat (K-Nearest Neighbors)**:

   - Untuk merekomendasikan item kepada pengguna, KNN menghitung kemiripan antara item yang telah dinilai oleh pengguna dan semua item lain yang belum dinilai oleh pengguna.
   - Alternatifnya, jika model berbasis pengguna, KNN menghitung kemiripan antara pengguna target dengan semua pengguna lain untuk menemukan pengguna yang memiliki preferensi serupa.

2. **Menghitung Kemiripan (Similarity Calculation)**:
   - Kemiripan antara dua item atau dua pengguna sering dihitung menggunakan metrik seperti _Cosine Similarity_ atau _Pearson Correlation_.
3. **Pemilihan Tetangga (Selecting Neighbors)**:

   - Setelah kemiripan dihitung, KNN memilih k tetangga terdekat yang memiliki nilai kemiripan tertinggi.

4. **Prediksi Rating (Rating Prediction)**:

   - Untuk memprediksi rating yang akan diberikan pengguna pada suatu item, kita bisa menghitung rata-rata tertimbang dari rating yang diberikan oleh tetangga terdekat. dengan catatan
     himpunan tetangga terdekat dari item, dan rating yang diprediksi untuk item.

5. **Memberikan Rekomendasi (Making Recommendations)**:
   - Setelah memprediksi rating untuk semua item yang belum dinilai oleh pengguna, kita dapat mengurutkan item-item tersebut berdasarkan rating prediksi dan merekomendasikan top-5 item dengan rating tertinggi kepada pengguna.

Penggunaan parameter dijelaskan sebagai berikut

Kode ini mengimplementasikan algoritma **K-Nearest Neighbors with Means (KNNWithMeans)** dari library `surprise` untuk membuat model rekomendasi. Berikut penjelasan mengenai parameter yang digunakan:

1. **k=5**: Parameter ini menentukan jumlah tetangga terdekat (neighbors) yang akan dipertimbangkan oleh algoritma saat membuat prediksi. Dalam kasus ini, algoritma akan menggunakan 5 tetangga terdekat untuk menentukan rating prediksi.

2. **sim_options={'name': 'pearson_baseline', 'user_based': False}**:

   - **'name': 'pearson_baseline'**: Ini menentukan jenis metrik kesamaan (similarity metric) yang digunakan untuk mengukur seberapa mirip dua item satu sama lain. `pearson_baseline` adalah varian dari Pearson correlation yang memperhitungkan baseline rating dari pengguna dan item, sehingga bisa menghasilkan perhitungan kesamaan yang lebih akurat.
   - **'user_based': False**: Parameter ini menentukan apakah kesamaan akan dihitung berdasarkan pengguna atau item. Jika `user_based` diset `False`, maka kesamaan dihitung antar item (item-based). Sebaliknya, jika `True`, kesamaan akan dihitung antar pengguna (user-based).

3. **algo.fit(trainset)**: Metode ini digunakan untuk melatih model `algo` menggunakan dataset pelatihan (`trainset`). Model akan mempelajari pola dari data tersebut untuk digunakan dalam melakukan prediksi di kemudian hari.

## Evaluation

### Evaluasi RMSE dari `testset`

Nilai RMSE sebesar 1.343641161111319 memberi indikasi tentang seberapa baik model dalam memprediksi rating. Untuk menganalisis nilai ini, kita perlu mempertimbangkan beberapa aspek:

1. **Skala Rating**

   - Jika skala rating adalah dari 1 hingga 5 (seperti pada kebanyakan sistem rekomendasi), RMSE sekitar 1.34 menunjukkan bahwa rata-rata kesalahan prediksi model sekitar 1.34 unit dari nilai sebenarnya. Ini berarti prediksi model sering kali meleset lebih dari satu poin pada skala rating.

2. **Perbandingan dengan Baseline**

   - Bandingkan nilai RMSE ini dengan baseline model, seperti model yang memprediksi rating rata-rata untuk semua item atau pengguna. Jika RMSE jauh lebih rendah daripada baseline, ini adalah indikasi positif bahwa model menangkap pola dalam data lebih baik daripada model sederhana.

3. **Implementasi Model**

   - Dalam beberapa aplikasi, RMSE sekitar 1.34 mungkin dianggap cukup baik, terutama jika data memiliki banyak noise atau jika preferensi pengguna sangat beragam. Namun, dalam aplikasi yang memerlukan prediksi yang sangat akurat (misalnya, sistem rekomendasi kritis), mungkin ingin mencoba menurunkan RMSE lebih jauh.

4. **Interpretasi Keseluruhan**
   - Secara keseluruhan, RMSE sebesar 1.34 adalah indikasi bahwa model cukup baik, tetapi mungkin ada ruang untuk perbaikan tergantung pada tujuan dan kebutuhan aplikasi Anda. Jika dibandingkan dengan model baseline dan model lain, nilai ini dapat memberikan lebih banyak konteks apakah model memadai atau memerlukan perbaikan lebih lanjut.

### Evaluasi MAE dari `testset`

Nilai MAE (Mean Absolute Error) sebesar 1.0505 memberikan indikasi tentang rata-rata kesalahan absolut antara prediksi model dan nilai sebenarnya. Mari kita analisis lebih lanjut:

1. **Skala Rating**

   - Jika skala rating yang gunakan adalah dari 1 hingga 5, maka nilai MAE sebesar 1.05 menunjukkan bahwa, secara rata-rata, prediksi model meleset sekitar 1.05 unit dari nilai sebenarnya. Ini berarti bahwa prediksi model biasanya berada dalam jarak sekitar satu poin dari rating aktual.

2. **Perbandingan dengan RMSE**

   - MAE lebih mudah diinterpretasikan daripada RMSE karena tidak memberikan penalti lebih besar untuk kesalahan yang besar. Dengan MAE sebesar 1.05 dan RMSE sebesar 1.34, dapat dikatakan bahwa meskipun ada beberapa kesalahan besar yang memengaruhi RMSE, rata-rata kesalahan absolut tetap berada di sekitar 1.05. Ini menunjukkan bahwa kebanyakan prediksi model berada dalam jarak yang cukup konsisten dari nilai sebenarnya, namun ada beberapa outlier atau kesalahan besar yang meningkatkan RMSE.

3. **Konteks Aplikasi**

   - Dalam konteks sistem rekomendasi, MAE sebesar 1.05 pada skala 1 hingga 5 berarti prediksi masih bisa ditingkatkan. Idealnya, menginginkan MAE yang mendekati 0, yang menunjukkan prediksi yang sangat dekat dengan rating sebenarnya. Namun, nilai MAE ini tidak terlalu buruk, terutama jika data mengandung banyak noise atau jika pengguna memiliki preferensi yang sangat beragam.

4. **Interpretasi Keseluruhan**
   - MAE sebesar 1.05 menunjukkan bahwa model memiliki kesalahan prediksi yang cukup signifikan, tetapi tidak ekstrem. Ada ruang untuk perbaikan, terutama jika akurasi prediksi sangat penting dalam konteks aplikasi Anda. Bandingkan dengan baseline atau model lain yang coba untuk menentukan apakah model ini sudah cukup baik atau perlu ditingkatkan lebih lanjut.

Perbandingan grafik antara RMSE dan MAE ditunjukan sebagai berikut

![comparison rmse,rmae](https://github.com/user-attachments/assets/7830691c-dad4-4ed2-b0df-6c5523395150)

### Cross Validation

![Cross Validation](https://github.com/user-attachments/assets/441fa760-ff5a-4e46-945a-3b72b45085d1)

Analisis hasil cross-validation ini memberikan gambaran tentang performa model di berbagai lipatan (fold) dari data. Mari kita telaah setiap metrik yang diberikan:

1. **RMSE (Root Mean Square Error)**

   - **Fold Values**: Nilai RMSE pada setiap lipatan berkisar antara 1.3371 hingga 1.3453. Ini menunjukkan bahwa performa model cukup konsisten di berbagai subset data.
   - **Mean**: Rata-rata RMSE sebesar 1.3417 menunjukkan bahwa, secara keseluruhan, kesalahan kuadrat rata-rata model berada di sekitar 1.34 unit dari nilai sebenarnya. Ini konsisten dengan analisis sebelumnya, di mana RMSE sekitar 1.34 berarti model cenderung meleset sekitar 1.34 unit pada skala rating.
   - **Standard Deviation (Std)**: Nilai standar deviasi sebesar 0.0036 sangat kecil, menunjukkan bahwa performa model sangat stabil di berbagai lipatan. Model tidak terlalu sensitif terhadap perubahan data, yang merupakan pertanda baik.

2. **MAE (Mean Absolute Error)**

   - **Fold Values**: Nilai MAE pada setiap lipatan berkisar antara 1.0438 hingga 1.0504, menunjukkan bahwa kesalahan absolut rata-rata cukup konsisten di seluruh lipatan.
   - **Mean**: Rata-rata MAE sebesar 1.0470 berarti bahwa, secara rata-rata, prediksi model meleset sekitar 1.05 unit dari nilai sebenarnya. Ini sejalan dengan analisis sebelumnya bahwa MAE ini mengindikasikan kesalahan prediksi yang moderat tetapi tidak ekstrem.
   - **Standard Deviation (Std)**: Standar deviasi sebesar 0.0027 juga sangat kecil, menegaskan bahwa kesalahan absolut rata-rata stabil di seluruh subset data yang diuji.

3. **Fit Time**

   - **Fold Values**: Waktu pelatihan (fit time) berkisar antara 2.94 detik hingga 3.72 detik per lipatan. Variasi ini mungkin disebabkan oleh perbedaan beban komputasi atau kinerja sistem pada saat pelatihan.
   - **Mean**: Rata-rata waktu pelatihan sebesar 3.28 detik menunjukkan bahwa model membutuhkan waktu yang cukup singkat untuk dilatih pada setiap subset data.
   - **Standard Deviation (Std)**: Standar deviasi sebesar 0.29 detik menunjukkan adanya variasi kecil dalam waktu pelatihan, tetapi ini tidak signifikan dan masih dalam batas yang dapat diterima.

4. **Test Time**
   - **Fold Values**: Waktu pengujian (test time) berkisar antara 0.72 detik hingga 0.80 detik per lipatan, yang menunjukkan konsistensi dalam kecepatan evaluasi model.
   - **Mean**: Rata-rata waktu pengujian sebesar 0.75 detik menunjukkan bahwa model memprediksi dengan cepat pada subset data uji.
   - **Standard Deviation (Std)**: Standar deviasi sebesar 0.03 detik sangat kecil, menunjukkan waktu pengujian yang sangat stabil dan konsisten di berbagai lipatan.

**Kesimpulan Cross Validation**

- **Konsistensi**: Nilai RMSE dan MAE yang sangat konsisten di seluruh lipatan menunjukkan bahwa model cukup stabil dan tidak terlalu dipengaruhi oleh variasi data. Standar deviasi yang rendah memperkuat kepercayaan dalam hasil model.
- **Performansi**: Meskipun nilai RMSE dan MAE mengindikasikan bahwa model memiliki kesalahan prediksi yang moderat, konsistensi model di berbagai lipatan adalah pertanda positif. bisa mencoba meningkatkan performa model dengan tuning hyperparameter lebih lanjut atau dengan mencoba metode lain.
- **Efisiensi**: Waktu pelatihan dan pengujian yang singkat dan konsisten menunjukkan bahwa model ini efisien dalam hal komputasi, yang penting untuk aplikasi yang membutuhkan respons cepat.

Secara keseluruhan, model ini tampaknya stabil dan efisien, meskipun mungkin masih ada ruang untuk perbaikan dalam hal akurasi prediksi.

### Uji coba

dari model yang sudah dibuat, dilakukan pembuat dataframe baru yang melalui beberapa tahap

- fill value 0 pada `userID` yang tidak mereivew `productID`, lalu di transpose matrix
- Dekomposisi matrix agar mengurangi dimensi dari matriks besar menjadi matriks dengan dimensi lebih kecil, sambil mempertahankan informasi penting.
- mengambil sampel `productID` agar di uji coba

## Kesimpulan

Untuk menjawab apakah model yang buat telah memenuhi tujuan dalam problem statement proyek, mari kita tinjau kedua poin dari problem statement dan hubungkan dengan hasil cross-validation yang peroleh:

1. **Membantu User Mencari Produk yang Benar**

   - **Analisis RMSE dan MAE**: Hasil cross-validation menunjukkan bahwa model memiliki RMSE sekitar 1.3417 dan MAE sekitar 1.0470. Ini menunjukkan bahwa model memiliki kesalahan prediksi rata-rata sekitar 1 poin pada skala rating 1 hingga 5. Jika tujuan utama adalah membantu pengguna menemukan produk yang benar, maka akurasi ini mungkin sudah cukup baik, tetapi bergantung pada konteks spesifik:
     - Jika pengguna cenderung puas dengan prediksi yang akurat dalam selisih sekitar 1 poin, model ini mungkin sudah cukup memadai.
     - Namun, jika aplikasi memerlukan prediksi yang sangat akurat untuk meningkatkan pengalaman pengguna, mungkin perlu mengoptimalkan model lebih lanjut untuk menurunkan nilai RMSE dan MAE.

2. **Meningkatkan Engagement Berdasarkan Rekomendasi**
   - **Kaitan dengan Engagement**: Meningkatkan engagement melalui sistem rekomendasi tidak hanya bergantung pada akurasi prediksi, tetapi juga pada relevansi dan personalisasi rekomendasi. RMSE dan MAE yang rendah membantu

**Penutup**

- **Kualitas Rekomendasi**: Berdasarkan nilai RMSE dan MAE, model cukup baik dalam memberikan rekomendasi yang akurat, tetapi mungkin ada ruang untuk perbaikan.

Jika engagement dan kepuasan pengguna adalah kunci keberhasilan proyek ini, pertimbangan tambahan ini akan sangat penting untuk memastikan bahwa model memenuhi tujuan secara menyeluruh.

### Referensi

[Nguyen, Luong Vuong, Quoc-Trinh Vo, and Tri-Hai Nguyen. "Adaptive knn-based extended collaborative filtering recommendation services." Big Data and Cognitive Computing 7.2 (2023): 106.](https://www.mdpi.com/2504-2289/7/2/106#:~:text=The%20KNN%2Dbased%20collaborative%20filtering%20algorithm%20is%20a%20type%20of,users%20to%20the%20target%20user.)
