# E-Commerce Public Data Analysis Dashboard ![image](https://github.com/user-attachments/assets/2c2c55a7-5f44-4d7c-ba75-60fa519b4dd1)

Repository ini merupakan proyek akhir dari kelas Dicoding "Belajar Analisis Data dengan Python". Proyek ini mencoba menganalisis data E-Commerce Public Dataset yang disediakan oleh Dicoding atau melalui sumber Kaggle dengan judul Brazilian E-Commerce Public Dataset oleh Olist. Tujuan dari analisis ini adalah untuk mengeksplorasi dan mengenal dataset tersebut, serta menemukan beberapa wawasan menarik dari dataset guna menjawab pertanyaan-pertanyaan bisnis.

# Pertanyaan Bisnis 
1. Berapa jumlah pesanan yang disetujui setiap bulan dalam rentang waktu tertentu, dan bagaimana perubahannya dari bulan ke bulan?
2. Produk apa yang memiliki penjualan tertinggi nomor 1 dan terendah nomor 1?
3. Bagaimana tingkat kepuasan pelanggan pada tahun 2018 berdasarkan data survei dan metrik terkait?
4. Dimana letak geografis yang memiliki customer terbanyak?

![Dashboard Streamlit - Komang Ryan](https://github.com/user-attachments/assets/07890ec2-d787-4b76-a51d-6dcad273569a)

# Main Project Structure
- ``` Dashboard with Streamlit ``` :  Folder yang menyimpan seluruh kode dan file yang diperlukan untuk membuat dashboard analisis data menggunakan Streamlit.
- ``` E-Commerce Public Dataset ``` :  Folder ini berisi semua dataset dalam format .csv yang digunakan.
- ``` Dashboard Streamlit - Komang Ryan.png ``` : File ini adalah gambar yang menunjukkan tampilan dasbor yang telah dibuat menggunakan Streamlit.
- ``` Proyek_akhir_analisis_data_Komang_Ryandhi.ipynb ``` : Notebook yang berisi seluruh proses analisis data mulai dari mendefinisikan pertanyaan hingga membuat kesimpulan dari hasil analisis.
- ``` requirements.txt ``` : File ini berisi daftar semua dependensi yang diperlukan untuk menjalankan proyek, beserta versi spesifik dari setiap paket yang digunakan.
  
## Setup environment

1. Clone repository ke komputer lokal anda menggunakan perintah berikut:
- ``` git clone https://github.com/kryandhi/e-commerce-public-data-analysis-2024.git ```
2. Instalasi Library
- ``` pip install streamlit numpy seaborn pandas matplotlib zipfile unidecode ```
3. - ``` pip install -r requirements.txt ```

## Run steamlit app (Local)
```
cd streamlit
streamlit run main.pystreamlit run ./streamlit/main.py
```

## Open Dashboard in Streamlit
![image](https://github.com/user-attachments/assets/f61f9bac-716a-4233-ace4-cdd44306a98b)



## Dataset (E-commerce public dataset)
[https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view?usp=sharing)

## Analysis Data Process
1. Data Wrangling
   - Data gathering
   - Data assessing
   - Data cleaning
2. Exploratory Data Analysis
3. Data visualization & Explanatory Analysis
4. Advanced data analysis using RFM
5. Geospatial Analysis
6. Clustering

## Conclusion
1. Berapa jumlah pesanan yang disetujui setiap bulan dalam rentang waktu tertentu, dan bagaimana perubahannya dari bulan ke bulan?

- Pembelian pelanggan menunjukkan variasi yang signifikan, dengan fluktuasi nilai yang mencerminkan kenaikan dan penurunan setiap bulannya. Analisis data mengungkapkan bahwa bulan November mencatat puncak maksimum pembelian, sedangkan bulan September mengalami puncak minimum.

2. Produk apa yang memiliki penjualan tertinggi nomor 1 dan terendah nomor 1?
- Produk yang paling populer di kalangan pelanggan adalah kategori "bed_bath_table," dengan penjualan mendekati 14.000 unit. Di sisi lain, kategori produk "security and services" mencatatkan penjualan terendah, hanya sebanyak 2 unit.

3. Bagaimana tingkat kepuasan pelanggan pada tahun 2018 berdasarkan data survei dan metrik terkait?
- Tingkat kepuasan pelanggan terhadap layanan yang diberikan sangat tinggi, seperti yang terlihat dalam visualisasi data. Sebagian besar pelanggan memberikan rating 5, sementara rating 4 menduduki posisi kedua terbanyak. Rata-rata nilai review yang diterima pada tahun 2018 adalah 4,05.

4. Dimana letak geografis yang memiliki customer terbanyak?
- Berdasarkan grafik yang telah dibuat, mayoritas pelanggan terkonsentrasi di wilayah tenggara dan selatan. Selain itu, terdapat jumlah pelanggan yang lebih tinggi di kota-kota besar yang berperan sebagai ibu kota, seperti São Paulo, Rio de Janeiro, dan Porto Alegre.
