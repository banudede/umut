import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title=" Umut İçin", page_icon="🥳")

# Güncellenmiş Başlıklar
st.title(" Umut İçin Küçük Bir Güzellik 🎉")
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
        st.success("Süpersiiiiin! Enerjin dünyayı aydınlatıyor! Yaşasın Umut Neşesiiiiii 😄 ✨")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqdW5kZ2JqZGdqZGdqZGdqZGdqZGdqZGdqZGdqZGdqZGdqJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTjJp82YyD8wUo/giphy.gif")
    
    elif seçim == "Biraz yorgunum...":
        st.snow()
        st.warning("Bazen durgunlaşmak normaldir. Dinlenmek iyidir. ☕")
       
    
    else:
        st.balloons()
        st.success("Hemen enerji yüklüyoruz... Yükleniyor... %100! ⚡")
        st.info("Sen harika bir insansın, Umut! Asla unutma!")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqdW5kZ2JqZGdqZGdqZGdqZGdqZGdqZGdqZGdqZGdqZGdqJmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKVUn7iM8FMEU24/giphy.gif")

st.markdown("---")
# Final dokunuşu ve efekt
st.snow() 
st.markdown("### BANU'DAN SANA KÜÇÜK BİR ANI :) 💖")