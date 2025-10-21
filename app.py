import streamlit as st
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="🌱 Sanal Fotosentez Deneyi", page_icon="🌿", layout="centered")

# Başlık
st.title("🌿 Sanal Fotosentez Deneyi")
st.write("Fotosentezin gerçekleşmesi için gerekli koşulları ayarla ve bitkinin tepkisini gözlemle! 🌞💧🌬️")

# Kullanıcı girdileri: slider ile miktar seçimi
isik_seviyesi = st.slider("Işık şiddeti (%)", 0, 100, 50)
su_miktari = st.slider("Su miktarı (%)", 0, 100, 50)
co2_miktari = st.slider("CO2 miktarı (%)", 0, 100, 50)

# Deney sonuç fonksiyonu
def fotosentez_miktari(isik, su, co2):
    # Her koşul toplam üretimi etkiler (0-100)
    toplam = (isik * 0.4) + (su * 0.3) + (co2 * 0.3)
    return toplam

def urun_oranlari(toplam):
    oksijen = toplam * 0.7
    glikoz = toplam * 0.3
    return oksijen, glikoz

# Eksik koşullar için ipuçları
def eksik_ipucu(isik, su, co2):
    eksikler = []
    ipucu = {
        "Işık yok": "Bitkinin güneş ışığına ihtiyacı var ☀️",
        "Su yok": "Su olmadan fotosentez yapamaz 💧",
        "Karbondioksit yok": "Hava olmadan fotosentez gerçekleşmez 🌬️"
    }
    if isik == 0:
        eksikler.append(ipucu["Işık yok"])
    if su == 0:
        eksikler.append(ipucu["Su yok"])
    if co2 == 0:
        eksikler.append(ipucu["Karbondioksit yok"])
    return eksikler

# Buton
if st.button("Deneyi Başlat"):
    toplam_uretimi = fotosentez_miktari(isik_seviyesi, su_miktari, co2_miktari)
    
    if toplam_uretimi > 0:
        st.success(f"✅ Fotosentez gerçekleşti! Toplam üretim: {int(toplam_uretimi)}%")
        
        # Ürün oranları
        oksijen, glikoz = urun_oranlari(toplam_uretimi)
        st.write(f"**Oksijen üretimi:** {int(oksijen)}%")
        st.write(f"**Glikoz üretimi:** {int(glikoz)}%")
        
        # Üretim animasyonu
        st.write("Fotosentez süreci gözlemleniyor...")
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.02)
            progress_bar.progress(i)
        
        # Pie chart ile ürün dağılımı
        labels = ['Oksijen', 'Glikoz']
        values = [oksijen, glikoz]
        colors = ['lightgreen', 'green']
        
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.set_title("Fotosentez Ürün Dağılımı")
        st.pyplot(fig)
        
    else:
        st.error("❌ Fotosentez gerçekleşmedi.")
        eksikler = eksik_ipucu(isik_seviyesi, su_miktari, co2_miktari)
        for e in eksikler:
            st.info(e)
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3d/Photosynthesis.gif", caption="Fotosentez süreci")
