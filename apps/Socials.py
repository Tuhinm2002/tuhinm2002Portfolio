import streamlit as st
import json
import base64

def load_lottiefile(filepath):
	with open(filepath, "r") as f:
		return json.load(f)

def app():
    st.title("Tuhin's Coding Accounts")
    lottie_coding = load_lottiefile(r"apps\social.json")
    st.lottie(lottie_coding, loop=True)
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    with col1:
        with st.expander("### Linkedin"):
            st.write("### My Linkedin Account")
            st.write("#### Links ")
            st.markdown("[![Foo](https://media.licdn.com/dms/image/C560EAQG-uEBUjD3-GA/rightRail-logo-shrink_200_200/0/1663316693401?e=1693299600&v=beta&t=V12omAFXiAibmTHb-NGn-OoBOXRVebs1rfn0g4GULZI)](www.linkedin.com/in/tuhinm2002)")

    with col2:
        with st.expander("### Email"):
            st.write("### My Email Address")
            st.markdown("#### tuhinm2002@gmail.com ")



    with st.expander("### My Resume"):
        st.markdown("#### https://drive.google.com/file/d/1fR9UQ8pdtybSchQ-22nVaknpG0J7NpYo/view?usp=drive_link")



