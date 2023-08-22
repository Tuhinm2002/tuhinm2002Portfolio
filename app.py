import streamlit as st
from Multiapp import Multipage
from apps import Home,Projects,Coding,Socials


def apps():
    app = Multipage()
    app.add_page("🏠 Home", Home.app)
    app.add_page("🚀 Projects",Projects.app)
    app.add_page("💻 Coding Accounts", Coding.app)
    app.add_page("🤵 Socials & Resume", Socials.app)
    app.run()
apps()
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")



