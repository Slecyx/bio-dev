import streamlit as st
import matplotlib.pyplot as plt

# Başlık
st.title("🌿 Sanal Fotosentez Deneyi")
st.write("Fotosentezin gerçekleşmesi için gerekli koşulları seç ve sonucu gözlemle:")

# Girdi: Kullanıcı seçimleri
isik = st.checkbox("Işık var")
su = st.checkbox("Su var")
co2 = st.checkbox("Karbondioksit var")

# Deney sonuç fonksiyonu
def fotosentez(isik, su, co2):
    if isik and su and co2:
        return True
    else:
        return False

# Buton
if st.button("Deneyi Başlat"):
    sonuc = fotosentez(isik, su, co2)

    if sonuc:
        st.success("✅ Fotosentez gerçekleşti! Bitki oksijen ve glikoz üretti.")
        st.write("**Kullanılan maddeler:** Işık, Su, Karbondioksit")
        st.write("**Üretilen maddeler:** Oksijen, Glikoz")

        # Grafikte üretim oranlarını göster
        labels = ['Oksijen', 'Glikoz']
        values = [70, 30]
        colors = ['lightgreen', 'green']

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.set_title("Fotosentez Ürün Dağılımı")
        st.pyplot(fig)

    else:
        st.error("❌ Fotosentez gerçekleşmedi.")
        eksikler = []
        if not isik:
            eksikler.append("Işık yok")
        if not su:
            eksikler.append("Su yok")
        if not co2:
            eksikler.append("Karbondioksit yok")
        st.warning("Eksik koşullar: " + ", ".join(eksikler))
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3d/Photosynthesis.gif", caption="Fotosentez süreci")
