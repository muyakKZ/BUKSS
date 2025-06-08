
import streamlit as st
import random
import pandas as pd

# Konfigurasi awal
jumlah_angka = 90
modal_per_angka = 40000
diskon = 0.29
payout = 70
jumlah_tahap_per_hari = 10
peluang_menang = 0.9

# Perhitungan
biaya_per_tahap = jumlah_angka * modal_per_angka * (1 - diskon)
keuntungan_per_tahap = payout * modal_per_angka - biaya_per_tahap
kerugian_per_tahap = biaya_per_tahap

# UI
st.title("Simulasi Togel 90 Angka Harian")
st.markdown("Strategi: 90 angka dari 100, modal Rp 40.000 per angka, diskon 29%.")

if "histori" not in st.session_state:
    st.session_state.histori = []

if st.button("Jalankan Simulasi Hari Ini"):
    hasil_harian = []
    for _ in range(jumlah_tahap_per_hari):
        if random.random() <= peluang_menang:
            hasil_harian.append(keuntungan_per_tahap)
        else:
            hasil_harian.append(-kerugian_per_tahap)

    st.session_state.histori.append({
        "Hari": len(st.session_state.histori) + 1,
        "Menang": hasil_harian.count(keuntungan_per_tahap),
        "Kalah": hasil_harian.count(-kerugian_per_tahap),
        "Profit": sum(hasil_harian)
    })

if st.session_state.histori:
    df = pd.DataFrame(st.session_state.histori)
    df["Kumulatif"] = df["Profit"].cumsum()
    st.dataframe(df)
    st.line_chart(df.set_index("Hari")["Kumulatif"])
    st.success(f"Total Profit: Rp {df['Kumulatif'].iloc[-1]:,.0f}")
else:
    st.info("Klik tombol untuk menjalankan simulasi harian.")
