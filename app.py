import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="Umut İçin", page_icon="🕺🏻")

# Session state kontrolü
if 'final_basildi' not in st.session_state:
    st.session_state.final_basildi = False
if 'sihirli_dokunus_tamamlandi' not in st.session_state:
    st.session_state.sihirli_dokunus_tamamlandi = False

# 1. FİNAL EKRANI (Butona basılınca tetiklenir)
if st.session_state.final_basildi:
    st.markdown("### ✨ Her nefes, evrenden sana yansıyan bir mucizedir.")
    time.sleep(1.5)
    st.markdown("### ✨ İçindeki sessizlikte, ruhunun gerçek gücünü bul.")
    time.sleep(1.5)
    st.markdown("### ✨ Yolun ışıkla dolsun, kalbin hep huzur bulsun bebişkosuuu :) ")
    time.sleep(1.5)
    st.markdown("### Dipnot: Bugün çok duygusalım 🥹 😂 ")
    time.sleep(1.5)
    st.markdown("---")
    
    st.title("BANU'DAN SANA KÜÇÜK BİR ANI :) 💃🏻 ")
    st.balloons() # Balonlar en sonda, final mesajıyla birlikte!

# 2. ANA EKRAN
else:
    st.title("Umut İçin Küçük Bir Güzellik ✨ ")
    st.subheader("Umut'un Motivasyon İstasyonu 😍")
    st.markdown("---")

    seçim = st.selectbox("Bugün ruh halin nasıl?", 
                         ("Harika hissediyorum!", "Biraz yorgunum...", "Enerjiye ihtiyacım var!"))

    # Sihirli Dokunuş Butonu
    if st.button("Sihirli Dokunuşu Başlat"):
        # İlerleme çubuğu
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        # Sonuç mesajları
        if seçim == "Harika hissediyorum!":
            st.success("Süpersin! Enerjin dünyayı aydınlatıyor! Yaşasın Umut Neşesiiiiiiii 😁 🎉 ✨")
        elif seçim == "Biraz yorgunum...":
            st.warning("Bazen durgunlaşmak normaldir. Dinlenmek iyidir. Keyifli günlerin değerini artırır✨☀️ ☕")
        else:
            st.success("Hemen enerji yüklüyoruz... Yükleniyor... %100! ⚡")
            st.info("Sen harika bir insansın, Umut! Asla unutma!")
        
        # Sihirli dokunuş artık tamamlandı
        st.session_state.sihirli_dokunus_tamamlandi = True
        st.rerun()

    # Final butonu SADECE işlem bitince görünür
    if st.session_state.sihirli_dokunus_tamamlandi:
        st.markdown("---")
        st.write("Her şey hazır! ✨")
        if st.button("Final"):
            st.session_state.final_basildi = True
            st.rerun()