import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

st.set_page_config(page_title="🌱 Sanal Fotosentez Deneyi", page_icon="🌿", layout="centered")

# Başlık
st.title("🌿 Sanal Fotosentez Deneyi")
st.write("Fotosentezin gerçekleşmesi için koşulları ayarla ve bitkinin tepkisini gözlemle! 🌞💧🌬️")

# Girdi: kullanıcı deney ayarları
st.subheader("🔬 Deney Koşullarını Ayarla")
isik = st.slider("Işık Şiddeti (0-100)", 0, 100, 50)
su = st.slider("Su Miktarı (0-100)", 0, 100, 50)
co2 = st.slider("Karbondioksit Seviyesi (0-100)", 0, 100, 50)

st.write("---")

# Hesaplama fonksiyonu
def fotosentez_verim(isik, su, co2):
    return round((isik * 0.4 + su * 0.3 + co2 * 0.3) / 3, 2)

# Buton
if st.button("🚀 Deneyi Başlat"):
    with st.spinner("Fotosentez reaksiyonu başlatılıyor..."):
        sleep(2)

    verim = fotosentez_verim(isik, su, co2)

    if verim > 40:
        st.success(f"✅ Fotosentez başarıyla gerçekleşti! Verim: %{verim}")
        st.balloons()

        # Ürün oranlarını hesapla
        oksijen = verim * 0.6
        glikoz = verim * 0.4

        # Grafik oluştur
        labels = ['Oksijen', 'Glikoz']
        values = [oksijen, glikoz]
        colors = ['lightgreen', 'mediumseagreen']

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.set_title("Fotosentez Ürün Dağılımı")
        st.pyplot(fig)

        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3d/Photosynthesis.gif",
                 caption="Fotosentez Süreci (Temsili Görsel)", use_container_width=True)

        st.write("### 🌿 Deney Raporu")
        st.markdown(f"""
        - **Işık Şiddeti:** {isik}  
        - **Su Miktarı:** {su}  
        - **Karbondioksit Seviyesi:** {co2}  
        - **Üretilen Oksijen:** {oksijen:.1f} birim  
        - **Üretilen Glikoz:** {glikoz:.1f} birim  
        """)

    else:
        st.error(f"❌ Fotosentez gerçekleşmedi! Verim çok düşük (%{verim}).")
        st.warning("Koşulları iyileştirmen gerekiyor. 🌥️ Daha fazla ışık, su veya CO₂ ver!")

        st.image("https://cdn.pixabay.com/photo/2016/10/25/12/28/sad-1768947_1280.png",
                 caption="Bitki yeterince enerji alamadı 😢", use_container_width=True)

else:
    st.info("Deneyi başlatmak için yukarıdaki koşulları ayarla ve 🚀 butonuna tıkla!")

