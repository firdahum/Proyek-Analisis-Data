import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import os
from pathlib import Path

# Load dataset dengan os
def load_data():
    # Pastikan path file relatif terhadap script ini
    file_path = Path(_file_).parent / "dashboard" / "main_data.csv"
    
    # Baca dataset
    df = pd.read_csv(file_path)
    df["dteday"] = pd.to_datetime(df["dteday"])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Data untuk Dampak Suhu terhadap Penyewaan ")
month = st.sidebar.selectbox("Pilih Bulan", df["mnth"].unique())
weather = st.sidebar.selectbox("Pilih Kondisi Cuaca", df["weathersit"].unique())

df_filtered = df[(df["mnth"] == month) & (df["weathersit"] == weather)]

# Dashboard title
st.title("Dashboard Bike Sharing🚴🏻🚴🏻🚴🏻")

st.write("Selamat datang di Dashboard Bike Sharing!")
st.write("Dashboard ini menyajikan analisis mendalam mengenai pola penyewaan sepeda berdasarkan berbagai faktor seperti hari libur, suhu, dan waktu dalam sehari.")

st.subheader("📊 Berikut Analisis Bike Sharing")

# 1. Dampak Hari Libur terhadap Penyewaan
st.subheader("Dampak Hari Libur terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
merge_df = df_filtered.groupby("holiday").agg({"cnt_daily": "mean"}).reset_index()
sns.barplot(x=merge_df["holiday"].map({0: "Hari Biasa", 1: "Hari Libur"}), 
            y=merge_df["cnt_daily"], hue=merge_df["holiday"].map({0: "Hari Biasa", 1: "Hari Libur"}), 
            palette="Set2", 
            legend=False, 
            ax=ax)
ax.set_xlabel("Jenis Hari")
ax.set_ylabel("Rata-rata Penyewaan")
ax.grid(True)
st.pyplot(fig)

# 2. Dampak Suhu terhadap Penyewaan
st.subheader("Dampak Suhu terhadap Penyewaan Sepeda")
merge_daily = df_filtered.groupby("dteday").agg({"temp": "mean", "cnt_daily": "mean"}).reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.regplot(x=merge_daily["temp"], y=merge_daily["cnt_daily"], scatter_kws={"alpha": 0.5}, line_kws={"color": "red"}, ax=ax)
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Penyewaan Harian")
ax.grid(True)
st.pyplot(fig)

# 3. Pola Penyewaan berdasarkan Waktu dalam Sehari
st.subheader("Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari")
fig, ax = plt.subplots(figsize=(10, 5))

# Garis utama
sns.lineplot(x=df_filtered["hr"], y=df_filtered["cnt_hourly"], marker="o", label="Total Rentals", color="darkblue", linewidth=2, ax=ax)

# Menandai jam sibuk dan jam sepi
rush_hours = [7, 8, 17, 18]
off_peak_hours = [0, 1, 2, 3, 4, 5]

rush_hour_rentals = df_filtered[df_filtered["hr"].isin(rush_hours)].groupby("hr")["cnt_hourly"].mean()
off_peak_rentals = df_filtered[df_filtered["hr"].isin(off_peak_hours)].groupby("hr")["cnt_hourly"].mean()

sns.scatterplot(x=rush_hour_rentals.index, y=rush_hour_rentals.values, color="red", s=100, edgecolor="black", label="Rush Hours", ax=ax)
sns.scatterplot(x=off_peak_rentals.index, y=off_peak_rentals.values, color="green", s=100, edgecolor="black", label="Off-Peak Hours", ax=ax)

ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xticks(range(0, 24))
ax.grid(True, linestyle="--", alpha=0.7)
ax.legend()
st.pyplot(fig)

# Show raw data
if st.checkbox("Tampilkan Data Mentah"):
    st.write(df_filtered)

st.markdown("---")
st.markdown("© Dibuat 2025")
st.markdown("by Firda Humaira")
