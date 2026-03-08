import time

# Sayfa ayarları
st.set_page_config(page_title="Umut İçin", page_icon="❤️")

# Sayfayı temizleyebilmek için ana konteyner
placeholder = st.empty()

# Adımları takip etmek için (3 keşif alanı için 3 bayrak)
if 'adim1' not in st.session_state: st.session_state.adim1 = False
if 'adim2' not in st.session_state: st.session_state.adim2 = False
if 'adim3' not in st.session_state: st.session_state.adim3 = False

with placeholder.container():
    st.title("Umut İçin Küçük Bir Güzellik 🥳")
    st.subheader("Umut'un Motivasyon İstasyonu 😍")
    st.markdown("---")

    # 1. Keşif: Neşe Makinesi
    seçim = st.selectbox("Bugün ruh halin nasıl?", 
                         ("Harika hissediyorum!", "Biraz yorgunum...", "Enerjiye ihtiyacım var!"))
    
    if st.button("Sihirli Dokunuşu Başlat"):
        st.session_state.adim1 = True
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        if seçim == "Harika hissediyorum!":
            st.balloons() 
            st.success("Süpersin! Enerjin dünyayı aydınlatıyor! Yaşasın Umut Neşesiiiiiiii 😁 🎉 ✨")
        elif seçim == "Biraz yorgunum...":
            st.snow()
            st.warning("Bazen durgunlaşmak normaldir. Dinlenmek iyidir. Keyifli günlerin değerini artırır✨☀️ ☕")
        else:
            st.balloons()
            st.success("Hemen enerji yüklüyoruz... %100! ⚡")
            st.info("Sen harika bir insansın, Umut! Asla unutma!")

    st.markdown("---")

    # 2. Keşif: Özel Not
    with st.expander("💌 Buraya bir tıkla, sürprizim var!"):
        st.write("Hayat bazen yorucu olabilir ama senin içindeki o güzel enerji her şeyi güzelleştirmeye yeter. İyi ki varsın Umut! 💖")
        if st.button("Notu okudum"):
            st.session_state.adim2 = True
            st.success("Notum kaydedildi! ✅")

    # 3. Keşif: Motivasyon Sözü
    if st.button("Bana bir ilham ver!"):
        st.session_state.adim3 = True
        st.success("Bugün her şey senin için çok güzel olacak! 🚀")

    st.markdown("---")
    
    # FİNAL BUTONU (Sadece 3 adım da tamamlandıysa görünür)
    if st.session_state.adim1 and st.session_state.adim2 and st.session_state.adim3:
        st.warning("Tüm keşifler bitti! Artık Final'e basabilirsin. ✨")
        if st.button("Final"):
            placeholder.empty() # Her şeyi sil
            
            # Final sahnesi
            st.snow()
            st.markdown("### ✨ Her nefes, evrenden sana yansıyan bir mucize.")
            time.sleep(1.5)
            st.markdown("### ✨ İçindeki sessizlikte, ruhunun gerçek gücünü bul.")
            time.sleep(1.5)
            st.markdown("### ✨ Yolun ışıkla dolsun, kalbin hep huzur bulsun bebişkosuuuu.")
            time.sleep(1.5)
            st.markdown("###  Dipnot: Bugün çok duygusalım 🥹😂 ")
            time.sleep(1.5)
            st.markdown("---")
            st.title("BANU'DAN SANA KÜÇÜK BİR ANI :) 💃🏻 ")
            st.balloons()