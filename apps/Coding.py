import streamlit as st
import json
import streamlit_lottie
def load_lottiefile(filepath):
	with open(filepath, "r") as f:
		return json.load(f)
def app():
    st.title("Tuhin's Coding Accounts")
    lottie_coding = load_lottiefile(r"apps\coding.json")
    st.lottie(lottie_coding, loop=True)
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    with col1:
        with st.expander("### Leetcode"):
            st.write("### My Leetcode Account")
            st.write("#### Links ")
            st.markdown("[![Foo](https://leetcode.com/_next/static/images/logo-dark-c96c407d175e36c81e236fcfdd682a0b.png)](https://leetcode.com/tuhinm2002/)")

    with col2:
        with st.expander("### Codechef"):
            st.write("### My Codechef Account")
            st.write("#### Links ")
            st.markdown("[![Foo](https://cdn.codechef.com/images/cc-logo.svg)](https://www.codechef.com/users/tuhinm2002)")

    with col3:
        with st.expander("### HackerRank"):
            st.write("### My HackerRank Account")
            st.write("#### Links ")
            st.markdown("[![Foo](https://hrcdn.net/fcore/assets/work/header/hackerrank_logo-21e2867566.svg)](https://www.hackerrank.com/tuhinm2002)")

    with col4:
        with st.expander("### kaggle"):
            st.write("### My kaggle Account")
            st.write("#### Links ")
            st.markdown("[![Foo](https://storage.googleapis.com/kaggle-avatars/images/default-thumb.png)](https://www.kaggle.com/tuhinm2002)")

