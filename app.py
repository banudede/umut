import streamlit as st

st.title("🕺🏻 Umut'un Özel Neşe Makinesi 🤖")

mod = st.radio("Selam Umut! Bugün kendini nasıl hissediyorsun?", 
               ("İyi hissediyorum", "Kötü hissediyorum"))

if st.button("Analiz Et"):
    if mod == "İyi hissediyorum":
        st.balloons()
        st.success("Yihuuu, YAŞASIN UMUT NEŞESİİİİİİ! 🥳 🎉")
        st.write("Enerjin harika, hep böyle kal! 😍🕺🏻🎈")
    else:
        st.error("HEEY! Sen enerji çocuksun kendine gel, hemen toparlan ve neşene geri dön.")
        st.write("Lütfen şimdi iyi hissediyorumu seç, sonra tekrar analiz et!")