import streamlit as st
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="🌱 Sanal Fotosentez Deneyi", page_icon="🌿", layout="centered")

# Başlık
st.title("🌿 Sanal Fotosentez Deneyi")
st.markdown(
    "Bitkilerin nasıl fotosentez yaptığını gözlemle! 🌞💧🌬️\n\n"
    "Aşağıdaki koşulları ayarlayarak, bitkinin oksijen ve glikoz üretimini inceleyebilirsin."
)

# --- Kullanıcı girdileri ---
st.header("🔧 Deney Koşullarını Belirle")
isik_seviyesi = st.slider("Işık şiddeti (%)", 0, 100, 70)
su_miktari = st.slider("Su miktarı (%)", 0, 100, 60)
co2_miktari = st.slider("CO₂ miktarı (%)", 0, 100, 80)

# --- Fonksiyonlar ---
def fotosentez_miktari(isik, su, co2):
    """Fotosentez miktarını hesaplar."""
    return (isik * 0.4) + (su * 0.3) + (co2 * 0.3)

def urun_oranlari(toplam):
    """Oksijen ve glikoz oranlarını hesaplar."""
    oksijen = toplam * 0.7
    glikoz = toplam * 0.3
    return oksijen, glikoz

def eksik_ipucu(isik, su, co2):
    """Eksik koşullar için açıklama verir."""
    eksikler = []
    if isik == 0:
        eksikler.append("☀️ **Işık eksik!** Bitki enerji üretemez.")
    if su == 0:
        eksikler.append("💧 **Su eksik!** Köklerden besin taşınamaz.")
    if co2 == 0:
        eksikler.append("🌬️ **CO₂ eksik!** Bitki karbon alamaz.")
    return eksikler

# --- Deneyi başlat ---
if st.button("🌱 Deneyi Başlat"):
    st.subheader("🔬 Fotosentez Süreci Başlatılıyor...")

    toplam_uretimi = fotosentez_miktari(isik_seviyesi, su_miktari, co2_miktari)

    if toplam_uretimi > 0:
        oksijen, glikoz = urun_oranlari(toplam_uretimi)

        # Denklemi göster
        st.markdown("---")
        st.latex(r"6CO_2 + 6H_2O + Işık \longrightarrow C_6H_{12}O_6 + 6O_2")
        st.caption("Fotosentez Denklemi: Karbondioksit + Su + Işık → Glikoz + Oksijen")

        # Girdiler - Çıktılar tablosu
        st.markdown("### ⚙️ Girdiler ve Çıktılar")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 🔹 Giren Maddeler")
            st.write(f"☀️ Işık: **{isik_seviyesi}%**")
            st.write(f"💧 Su (H₂O): **{su_miktari}%**")
            st.write(f"🌬️ Karbondioksit (CO₂): **{co2_miktari}%**")

        with col2:
            st.markdown("#### 🔸 Çıkan Maddeler")
            st.write(f"🌿 Glikoz (C₆H₁₂O₆): **{int(glikoz)}%**")
            st.write(f"🍃 Oksijen (O₂): **{int(oksijen)}%**")

        # Animasyon (ilerleme çubuğu)
        st.markdown("---")
        st.write("🌞 Bitki fotosentez yapıyor...")
        progress_bar = st.progress(0)
        for i in range(101):
            time.sleep(0.015)
            progress_bar.progress(i)

        # Sonuç
        st.success(f"✅ Fotosentez tamamlandı! Toplam üretim: **{int(toplam_uretimi)}%**")

        # Grafik - ürün oranları
        labels = ['Oksijen (O₂)', 'Glikoz (C₆H₁₂O₆)']
        values = [oksijen, glikoz]
        colors = ['#7CFC00', '#2E8B57']

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
        ax.set_title("🌿 Fotosentez Ürün Dağılımı")
        st.pyplot(fig)

        # Bilgilendirici not
        st.info("🔍 Bitkiler, ürettikleri glikozu enerji olarak kullanır ve oksijeni atmosfere salar.")

    else:
        st.error("❌ Fotosentez gerçekleşmedi!")
        for e in eksik_ipucu(isik_seviyesi, su_miktari, co2_miktari):
            st.warning(e)

        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/3d/Photosynthesis.gif",
            caption="Fotosentez gerçekleşmesi için tüm koşullar gerekli 🌱",
            use_column_width=True
        )
