import streamlit as st
import matplotlib.pyplot as plt
from time import sleep

st.set_page_config(page_title="🌱 Sanal Fotosentez Deneyi", page_icon="🌿", layout="centered")

# Başlık
st.title("🌿 Sanal Fotosentez Deneyi")
st.write("Bitkinin fotosentez yapabilmesi için koşulları ayarla ve tepkisini izle! 🌞💧🌬️")

# Deney ayarları
st.subheader("🔧 Koşulları Ayarla")
isik = st.slider("Işık Şiddeti", 0, 100, 50)
su = st.slider("Su Miktarı", 0, 100, 50)
co2 = st.slider("CO₂ Seviyesi", 0, 100, 50)

st.write("---")

# Fotosentez verimi hesaplama
def fotosentez_verim(isik, su, co2):
    return round((isik*0.4 + su*0.3 + co2*0.3) / 3, 2)

# Deneyi başlat butonu
if st.button("🚀 Deneyi Başlat"):
    with st.spinner("Fotosentez gerçekleşiyor..."):
        sleep(2)
    
    verim = fotosentez_verim(isik, su, co2)

    if verim > 40:
        st.success(f"✅ Fotosentez gerçekleşti! Verim: %{verim}")
        st.balloons()

        oksijen = verim * 0.6
        glikoz = verim * 0.4

        # Basit renkli çubuk grafik
        fig, ax = plt.subplots()
        ax.bar(['Oksijen', 'Glikoz'], [oksijen, glikoz], color=['#76c893', '#52b69a'])
        ax.set_ylabel("Ürün Miktarı")
        ax.set_title("Fotosentez Ürünleri")
        st.pyplot(fig)

        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/3d/Photosynthesis.gif",
            caption="Fotosentez Süreci (Temsili)", use_container_width=True
        )

        st.markdown(f"""
        ### Deney Raporu
        - **Işık:** {isik}  
        - **Su:** {su}  
        - **CO₂:** {co2}  
        - **Oksijen:** {oksijen:.1f}  
        - **Glikoz:** {glikoz:.1f}  
        """)

    else:
        st.error(f"❌ Fotosentez gerçekleşmedi! Verim çok düşük (%{verim}).")
        st.warning("Daha fazla ışık, su veya CO₂ eklemelisin! 🌥️")
        st.image(
            "https://cdn.pixabay.com/photo/2016/10/25/12/28/sad-1768947_1280.png",
            caption="Bitki yeterince enerji alamadı 😢", use_container_width=True
        )

else:
    st.info("Koşulları ayarladıktan sonra 🚀 butonuna tıkla ve sonucu izle!")
