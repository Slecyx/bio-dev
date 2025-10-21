import streamlit as st
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="🌱 Sanal Fotosentez Deneyi", page_icon="🌿", layout="centered")

# Başlık ve açıklama
st.title("🌿 Sanal Fotosentez Deneyi")
st.markdown(
    "Fotosentezin gerçekleşmesi için gerekli koşulları ayarla ve bitkinin tepkisini gözlemle! 🌞💧🌬️"
)

# --- Kullanıcı girdileri ---
st.header("Deney Koşullarını Ayarla")
isik_seviyesi = st.slider("Işık şiddeti (%)", 0, 100, 50)
su_miktari = st.slider("Su miktarı (%)", 0, 100, 50)
co2_miktari = st.slider("CO2 miktarı (%)", 0, 100, 50)

# --- Fonksiyonlar ---
def fotosentez_miktari(isik, su, co2):
    """Koşullara göre fotosentez miktarını hesaplar."""
    toplam = (isik * 0.4) + (su * 0.3) + (co2 * 0.3)
    return toplam

def urun_oranlari(toplam):
    """Oksijen ve glikoz oranlarını hesaplar."""
    oksijen = toplam * 0.7
    glikoz = toplam * 0.3
    return oksijen, glikoz

def eksik_ipucu(isik, su, co2):
    """Eksik koşullar için ipuçları verir."""
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

# --- Deneyi başlat ---
if st.button("🌱 Deneyi Başlat"):
    toplam_uretimi = fotosentez_miktari(isik_seviyesi, su_miktari, co2_miktari)
    
    if toplam_uretimi > 0:
        st.success(f"✅ Fotosentez gerçekleşti! Toplam üretim: {int(toplam_uretimi)}%")
        oksijen, glikoz = urun_oranlari(toplam_uretimi)
        
        # Metric ile hızlı gösterim
        col1, col2 = st.columns(2)
        col1.metric("Oksijen Üretimi", f"{int(oksijen)}%")
        col2.metric("Glikoz Üretimi", f"{int(glikoz)}%")
        
        # Animasyon
        st.write("Fotosentez süreci gözlemleniyor...")
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.01)  # Daha hızlı ve akıcı
            progress_bar.progress(i)
        
        # Pie chart
        labels = ['Oksijen', 'Glikoz']
        values = [oksijen, glikoz]
        colors = ['#7CFC00', '#32CD32']
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
        ax.set_title("Fotosentez Ürün Dağılımı")
        st.pyplot(fig)
        
    else:
        st.error("❌ Fotosentez gerçekleşmedi.")
        eksikler = eksik_ipucu(isik_seviyesi, su_miktari, co2_miktari)
        for e in eksikler:
            st.info(e)
        # Daha açıklayıcı GIF
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/3d/Photosynthesis.gif",
            caption="Fotosentez süreci",
            use_column_width=True
        )
