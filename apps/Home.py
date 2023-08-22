import streamlit as st
import json
try:
	import streamlit_lottie
except:
	pass

def load_lottiefile(filepath):
	with open(filepath, "r") as f:
		return json.load(f)
def app():
	st.title("🙋‍♂️ Welcome to Tuhin's Portfolio")
	st.write("")
	st.write("")
	st.write("")
	lottie_coding = load_lottiefile("first_comp.json")
	st.lottie(lottie_coding,loop=True)
	st.write("### Hey there, whoever viewing this pleasure to meet you"
			 "😊🤓🤗")
	st.write("")
	st.write("")
	st.write("")
	st.write("### So who is Tuhin ? Let us know about him 🤔")
	st.write("")
	st.write("")
	st.write("Tuhin's Full name is Tuhin Mondal also known by the code name. "
			 "tuhinm2002 in many coding platforms like leetcode and codechef and also in github. "
			 "He is a third year student of B.tech studying in University of Engineering and Management. "
			 "He has a great passsion for machine leraning and deep learning research. "
			 "his current field of learning is llms and nlp models and pre trained models. "
			 "of transformers"
			 "He has been doing great in the field of ml and data science "
			 "and looking forward to build a great career into this. "
			 "Hope the companies also support him in his dreams ")
	st.write("")
	st.write("")
	st.write("")
	st.write("#### Want to know more about him then let's dive in and see"
			 "what is wating in the other tabs")
