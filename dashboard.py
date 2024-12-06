import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data
day = pd.read_csv("day-cleaned.csv")  # Pastikan file ini ada di direktori Streamlit
hour = pd.read_csv("hour-cleaned.csv")  # Pastikan file ini ada di direktori Streamlit

# Halaman utama
st.title("🚲 Bike Sharing Analysis by Vit 🚲")

# Tambahkan informasi
st.info("Analisis data bike sharing untuk memahami pengaruh cuaca dan waktu terhadap total penyewaan sepeda.")

# Data Expander
with st.expander('Data yang sudah bersih'):
    st.write('**day.csv**')
    day = pd.read_csv('day-cleaned.csv')
    st.dataframe(day, height=150)
    st.write('**hour.csv**')
    hour = pd.read_csv('hour-cleaned.csv')
    st.dataframe(hour, height=150)

# Pilih pertanyaan untuk analisis
question = st.selectbox("Pilih Analisis", [
    "Pengaruh variabel cuaca terhadap total penyewaan sepeda",
    "Perbandingan pola penyewaan sepeda pada hari kerja dan akhir pekan"
])

# Bar 1: Pengaruh variabel cuaca terhadap total penyewaan sepeda
if question == "Pengaruh variabel cuaca terhadap total penyewaan sepeda":
    st.header("Pengaruh Variabel Cuaca terhadap Total Penyewaan Sepeda")

    # Heatmap korelasi
    corr_features = ['suhu', 'suhu_terasa', 'kelembapan', 'kecepatan_angin', 'total_penyewa']
    corr_matrix_day = day[corr_features].corr()

    st.subheader("Heatmap Korelasi")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix_day, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Korelasi antara variabel cuaca dan total penyewaan sepeda')
    st.pyplot(fig)

    # Kesimpulan
    st.subheader("Kesimpulan")
    st.write("""
    - **Suhu**: Terdapat hubungan positif antara suhu dan jumlah penyewaan. Semakin tinggi suhu, semakin banyak sepeda yang disewa.
    - **Kelembapan**: Tidak ada hubungan yang jelas antara kelembapan dan jumlah penyewaan sepeda. Kelembapan tampaknya bukan faktor signifikan.
    - **Kecepatan Angin**: Sama halnya dengan kelembapan, kecepatan angin juga tidak menunjukkan hubungan yang kuat dengan jumlah penyewaan sepeda.
    """)

# Bar 2: Perbandingan pola penyewaan sepeda pada hari kerja dan akhir pekan
elif question == "Perbandingan pola penyewaan sepeda pada hari kerja dan akhir pekan":
    st.header("Perbandingan Pola Penyewaan Sepeda pada Hari Kerja dan Akhir Pekan")

    # Grupkan data berdasarkan waktu dan tipe hari
    holiday_rental_counts = hour.groupby('holiday')['total_penyewa'].mean()
    colors = ['#000059', '#DBA514']  # Warna untuk Tidak Libur dan Libur
    # Plot data
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(holiday_rental_counts.index, holiday_rental_counts.values, color=colors)
    ax.set_xlabel('Holiday')
    ax.set_ylabel('Rata-rata Jumlah Penyewa')
    ax.set_title('Perubahan Jumlah Penyewa di Hari Libur')
    ax.set_xticks(holiday_rental_counts.index, ['Tidak Libur', 'Libur'])  # Label X-axis
    st.pyplot(fig)

    # Kesimpulan
    st.subheader("Kesimpulan")
    st.write("""
    - Pada hari kerja, terdapat dua puncak penyewaan signifikan: pagi sekitar pukul 8 dan sore pukul 5-6, kemungkinan terkait aktivitas kerja.
    - Pada akhir pekan, pola penyewaan lebih merata dengan puncak sekitar pukul 2 siang, mencerminkan aktivitas rekreasi masyarakat.
    """)
