import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title=" Umut İçin", page_icon="❤️")

# Güncellenmiş Başlıklar
st.title(" Umut İçin Küçük Bir Güzellik 🥳")
st.subheader("Umut'un Motivasyon İstasyonu 😍")
st.markdown("---")

seçim = st.selectbox("Bugün ruh halin nasıl?", 
                     ("Harika hissediyorum!", "Biraz yorgunum...", "Enerjiye ihtiyacım var!"))

if st.button("Sihirli Dokunuşu Başlat"):
    # İlerleme çubuğu
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    
    st.markdown("---")
    
    if seçim == "Harika hissediyorum!":
        st.balloons() 
        st.success("Süpersin! Enerjin dünyayı aydınlatıyor! Yaşasın Umut Neşesiiiiiiii 😁 🎉 ✨")
        
    
    elif seçim == "Biraz yorgunum...":
        st.snow()
        st.warning("Bazen durgunlaşmak normaldir. Dinlenmek iyidir. Keyifli günlerin değerini artırır✨☀️ ☕")
        
    
    else:
        st.balloons()
        st.success("Hemen enerji yüklüyoruz... Yükleniyor... %100! ⚡")
        st.info("Sen harika bir insansın, Umut! Asla unutma!")
        

# FİNAL BUTONU
    if st.button("Final"):
        placeholder.empty() # Diğer her şeyi sil
        
        # Sadece finalde belirecek efektler ve metinler
        st.snow()
        
        st.markdown("### ✨ Her nefes, evrenden sana yansıyan bir mucize.")
        time.sleep(1.5)
        st.markdown("### ✨ İçindeki sessizlikte, ruhunun gerçek gücünü bul.")
        time.sleep(1.5)
        st.markdown("### ✨ Yolun ışıkla dolsun, kalbin hep huzur bulsun bebişkosuuuu. Dipnot: Bugün çok duygusalım 🥹😂 ")
        time.sleep(1.5)
        st.markdown("---")
        st.title("BANU'DAN SANA KÜÇÜK BİR ANI :) 💃🏻 ")
        st.balloons()