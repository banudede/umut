import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="Umut'a Özel", page_icon="✨")

# Oturum durumlarını takip edelim
if 'adımlar' not in st.session_state:
    st.session_state.adımlar = {"1": False, "2": False, "3": False}
if 'final_goster' not in st.session_state:
    st.session_state.final_goster = False

# Giriş ekranı (final gösterilmiyorsa)
if not st.session_state.final_goster:
    container = st.container()
    with container:
        st.title("Umut'a özel küçük bir güzellik ✨")
        st.write("Bugün kendini nasıl hissediyorsun?")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Çok iyi hissediyorum"):
                st.success("Yihuuuuu!💃🏻 İşte bu!😍 Yaşasın Umut neşesiiiiiiiiiii🕺🏻😂")
                st.session_state.adımlar["1"] = True
        with col2:
            if st.button("Biraz yorgunum"):
                st.info("Hemen kendine bir kahve yap☕️, en sevdiğin dizi/film aç ve dinlenmenin tadını çıkar😴🌙")
                st.session_state.adımlar["2"] = True
        with col3:
            if st.button("Modum düşük"):
                st.warning("Ne demek modum düşük ? Hemen enerji yüklemesi yapıyoruz...")
                bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    bar.progress(i + 1)
                st.success("Enerji yüklendi ⚡️ ☀️!")
                st.session_state.adımlar["3"] = True

    # Tüm butonlara basıldı mı kontrolü
    if all(st.session_state.adımlar.values()):
        st.divider()
        if st.button("Finali Görmek İçin Tıkla 🎁"):
            st.session_state.final_goster = True
            st.rerun()

# Final ekranı
else:
    # Sayfadaki her şeyi temizle
    st.empty() 
    
    # Yazıyı göstermek için bir alan oluştur
    yazi_alani = st.empty()
    
    yazi = [
        "Seninle vakit geçirmek her zaman modumu yükseltiyor,",
        "dünyadaki en kafa dengi insanlardan birisin.",
        "Hayatın akışında senin gibi pozitif birinin olması büyük şans.",
        "Her şey gönlünce olsun, keyfin hep böyle yerinde kalsın!"
    ]
    
    # Cümleleri sırayla ekranda biriktirerek yazdır
    gorunen_yazi = ""
    for cumle in yazi:
        gorunen_yazi += f"### {cumle}\n\n"
        yazi_alani.markdown(gorunen_yazi)
        time.sleep(2.5)
    
    # Yazı bitince ekranı temizle
    yazi_alani.empty()
    
    # Balonları patlat ve final mesajını göster
    st.balloons()
    st.title("BANU'DAN SANA KÜÇÜK BİR ANI :)")