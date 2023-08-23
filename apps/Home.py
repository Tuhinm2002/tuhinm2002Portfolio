import streamlit as st
import json
import streamlit_lottie

def load_lottiefile(filepath):
	with open(filepath, "r") as f:
		return json.load(f)
def app():
	st.title("🙋‍♂️ Welcome to Tuhin's Portfolio (ML and AI)")
	st.markdown("### tuhinm2002@gmail.com || tuhinm151@gmail.com")
	st.markdown("[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABDUlEQVR4AWP4////gOLB44D6nTcsGIo33QHi/zTGd0B2YTiAPpYjHIHNAf/piQk6wGPW8f/rLz8HYRCbXg5AWI4GQGJ0cwDY12gAJDbcHUA4CkZAIqQUK7Ts/m/SfxBMs5RupswBaACr+P47b/5zlG/5DyzZ/r/+8hNF7vuvP//nn3r0X6JhJ+0ccPrR+/+H7735jw9cf/n5v0D1Nuo5gBxQve06zR0AjoL7b7/+//zjN4bc+ScfaOeA33///k9Yfg4mDw7u/Xdeo6uhnQP6D93FMNxlxjF0ZbRzgMXEQ9iyI90cALIMJoccDXRzAK6CZog6YNQBow6gIx54Bwx4x2RAu2bAysoEZu9o7xgAQrvkxt3WZi0AAAAASUVORK5CYII=)](www.linkedin.com/in/tuhinm2002) "
			"[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/Tuhinm2002/) "
			"Resume 👉"
			"[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAyVBMVEVHcEwYgDgYgDgwnW8imUoWfjYYgDgCfTm3px35pw80qFNXjDD+wAD7vAQ0qVAwo1Ddsg/8vAP8vgMrijuGmCg0qFP7vAQ0qFP7vAQ0qFP7vAQhqFX9vgISplr7vAT7vAT7vAQ1q0oedL4jfq4hfawzhcdAhfa1gI30bhnwcCjtWS8XY9cYZdVChfU2h/nrQTTpOjcXZtEYZ9I0eueUa7DyPRjqQzUlb9ssif/XTFUZZ9Jme9m+WX3qQzXwPyU/hvVChfRChfRBhfQoFiIiAAAAQ3RSTlMAQEkl//////4a////63v///9p//+xmdvPVz2rvQqlUPn/hP//3azf//+SSf////9A3v/////Q////qf//bt15t7a2ajpqkQAAAQZJREFUeAGsz9WawjAQBeCDQ9DB3VZxd3j/19pmmsk2X3vJfzt68F6xOIshWiKZSrNMNocoSqW5I5MvFBGhpFTZb6gQVRGmPDWvI1MvEBFCGkrTDaQ1Qx8qlkxlsgXScnC1lC9dKxBrw9FRRrJiGqiLICV6fTKKbkQxyJGowhooUQKaJJyIBjwkhk5E1oGnSiJnIxotsCIZbYkoEmBdEiM3YgOGjTrmiBMBqyB01OmH7/Pr2/r5nfnmABZLY/VvvTG28Oz27BBsOJ64foaW2GuXVdD1xg05sLtdYK0fesUcBi9wXZ9eA8R0v1+FnDYvWDvngPnzb3bICcLewcERBTg42TPQCwAAp2s7XGwIAYMAAAAASUVORK5CYII=)](https://drive.google.com/file/d/1fR9UQ8pdtybSchQ-22nVaknpG0J7NpYo/view?usp=drive_link)")
	st.write("")
	st.write("")
	st.write("")
	lottie_coding = load_lottiefile("first_comp.json")
	streamlit_lottie.st_lottie(lottie_coding,loop=True)
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
			 "of transformers "
			 "He has been doing great in the field of ml and data science "
			 "and looking forward to build a great career into this. "
			 "Hope the companies also support him in his dreams ")
	st.write("")
	st.write("")
	st.write("")
	st.title("🚀 Tuhin's Projects")
	lottie_coding = load_lottiefile("animation_project.json")
	streamlit_lottie.st_lottie(lottie_coding, loop=True)
	col1, col2 = st.columns(2)
	col3, col4 = st.columns(2)
	with col1:
		with st.expander("### Spam detector"):
			st.write("A small Natural Language Processing (NLP) project "
					 "made with python to detect spam messages over the emai and "
					 "internet.")
			st.write("#### Technologies used")
			st.write("Python (base language")
			st.write("Scikit-learn (ml module)")
			st.write("pandas (data structure for data science)")
			st.write("jupyter (Interactive python notebook editor)")
			st.write("streamlit (python module for web app)")
			st.write("render.com (for deployment)")
			st.write("")
			st.write("#### Links ")
			st.markdown(
				"[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/Tuhinm2002/spam-classifier/)")
			st.markdown(
				"[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAtFBMVEX////gsbH26em3HyTBUVS8PD//JCT/iIj/+PjbpKW6MDS9QEOvjI96LjX/pqb/AAD/mJi3Iia5m51yFiC/paf/8PD/Kyv/GRn/ERF1ISl9NTtwDxv07+//X1//s7PKtbaVY2b/w8P/MTHUxMV1ICj/HR3TPT+4QUT/kpL0MzPOP0GnP0N4NDr/6emMOj//U1ONVFjrNjfiOTurhon/39+eISjj29z/fX3gfX7/1NT/bW3/W1uaV1tlAAAA6ElEQVR4AeXORXYDQQxFUbmZqstYZGYOx7j/fUVNCnsDvuN/9AT3qVaDmyzbtuAWx3Ud+M7zAyBhFMdRCCRIGKSc1ynQiFGDIs1Wqw0dLqRKq0CMqkhba9PtAfQ9IaQ3KAOoiAyZNoaNAGCsBFKTcREoIlOjDZpNAUmRU/PFslpE2uQ0ZFZzUVpvqsl2ZxBLILPngtDkwaCWBblHT3yZuMUET7AnQPQmeY6XRUQPoUSDLxOMtKDiV2+SF1ywV6i80ZtfJ+8HIEfOlZLzuZebz6VSnJ/gq/15nK6Ol/712r8cV+n4vIe78gHQ5B8DWKNMwgAAAABJRU5ErkJggg==)](https://spam-classifier-a0li.onrender.com)")
	with col2:
		with st.expander("### ML for Drug Discovery"):
			st.write("A Complicated Data Science and Ml project for drug discovery "
					 "It aims to calculate activeness of a drug on particular disease "
					 "using various regression techniques and its accuracy is measured "
					 "using ic50 parameter ")
			st.write("#### Technologies used")
			st.write("Python (base language")
			st.write("Scikit-learn (ml module)")
			st.write("pandas (data structure for data science)")
			st.write("jupyter (Interactive python notebook editor)")
			st.write("padelpy (python module to break the molecular formula) ")
			st.write("streamlit (python module for web app)")
			st.write("render.com (for deployment)")
			st.write("")
			st.write("#### Links ")
			st.markdown(
				"[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/Tuhinm2002/ML_Drug_Discovery/)")
			st.markdown(
				"[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAtFBMVEX////gsbH26em3HyTBUVS8PD//JCT/iIj/+PjbpKW6MDS9QEOvjI96LjX/pqb/AAD/mJi3Iia5m51yFiC/paf/8PD/Kyv/GRn/ERF1ISl9NTtwDxv07+//X1//s7PKtbaVY2b/w8P/MTHUxMV1ICj/HR3TPT+4QUT/kpL0MzPOP0GnP0N4NDr/6emMOj//U1ONVFjrNjfiOTurhon/39+eISjj29z/fX3gfX7/1NT/bW3/W1uaV1tlAAAA6ElEQVR4AeXORXYDQQxFUbmZqstYZGYOx7j/fUVNCnsDvuN/9AT3qVaDmyzbtuAWx3Ud+M7zAyBhFMdRCCRIGKSc1ynQiFGDIs1Wqw0dLqRKq0CMqkhba9PtAfQ9IaQ3KAOoiAyZNoaNAGCsBFKTcREoIlOjDZpNAUmRU/PFslpE2uQ0ZFZzUVpvqsl2ZxBLILPngtDkwaCWBblHT3yZuMUET7AnQPQmeY6XRUQPoUSDLxOMtKDiV2+SF1ywV6i80ZtfJ+8HIEfOlZLzuZebz6VSnJ/gq/15nK6Ol/712r8cV+n4vIe78gHQ5B8DWKNMwgAAAABJRU5ErkJggg==)](https://ml-drug-sars.onrender.com)")

	# with col3:
	#     with st.expander("### ML for Drug Discovery"):
	#         st.write("A Complicated Data Science and Ml project for drug discovery "
	#                  "It aims to calculate activeness of a drug on particular disease "
	#                  "using various regression techniques and its accuracy is measured "
	#                  "using ic50 parameter ")
	#         st.write("#### Technologies used")
	#         st.write("Python (base language")
	#         st.write("Scikit-learn (ml module)")
	#         st.write("pandas (data structure for data science)")
	#         st.write("jupyter (Interactive python notebook editor)")
	#         st.write("padelpy (python module to break the molecular formula) ")
	#         st.write("streamlit (python module for web app)")
	#         st.write("render.com (for deployment)")
	#         st.write("")
	#         st.write("#### Links ")
	#         st.markdown("[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/Tuhinm2002/spam-classifier/)")
	#         st.markdown("[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAtFBMVEX////gsbH26em3HyTBUVS8PD//JCT/iIj/+PjbpKW6MDS9QEOvjI96LjX/pqb/AAD/mJi3Iia5m51yFiC/paf/8PD/Kyv/GRn/ERF1ISl9NTtwDxv07+//X1//s7PKtbaVY2b/w8P/MTHUxMV1ICj/HR3TPT+4QUT/kpL0MzPOP0GnP0N4NDr/6emMOj//U1ONVFjrNjfiOTurhon/39+eISjj29z/fX3gfX7/1NT/bW3/W1uaV1tlAAAA6ElEQVR4AeXORXYDQQxFUbmZqstYZGYOx7j/fUVNCnsDvuN/9AT3qVaDmyzbtuAWx3Ud+M7zAyBhFMdRCCRIGKSc1ynQiFGDIs1Wqw0dLqRKq0CMqkhba9PtAfQ9IaQ3KAOoiAyZNoaNAGCsBFKTcREoIlOjDZpNAUmRU/PFslpE2uQ0ZFZzUVpvqsl2ZxBLILPngtDkwaCWBblHT3yZuMUET7AnQPQmeY6XRUQPoUSDLxOMtKDiV2+SF1ywV6i80ZtfJ+8HIEfOlZLzuZebz6VSnJ/gq/15nK6Ol/712r8cV+n4vIe78gHQ5B8DWKNMwgAAAABJRU5ErkJggg==)](https://spam-classifier-a0li.onrender.com)")

	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.title("💻 Tuhin's Coding Accounts")
	lottie_coding = load_lottiefile("coding.json")
	streamlit_lottie.st_lottie(lottie_coding, loop=True)
	col1, col2 = st.columns(2)
	col3, col4 = st.columns(2)
	with col1:
		with st.expander("### Leetcode"):
			st.write("### My Leetcode Account")
			st.write("#### Links ")
			st.markdown(
				"[![Foo](https://leetcode.com/_next/static/images/logo-dark-c96c407d175e36c81e236fcfdd682a0b.png)](https://leetcode.com/tuhinm2002/)")

	with col2:
		with st.expander("### Codechef"):
			st.write("### My Codechef Account")
			st.write("#### Links ")
			st.markdown(
				"[![Foo](https://cdn.codechef.com/images/cc-logo.svg)](https://www.codechef.com/users/tuhinm2002)")

	with col3:
		with st.expander("### HackerRank"):
			st.write("### My HackerRank Account")
			st.write("#### Links ")
			st.markdown(
				"[![Foo](https://hrcdn.net/fcore/assets/work/header/hackerrank_logo-21e2867566.svg)](https://www.hackerrank.com/tuhinm2002)")

	with col4:
		with st.expander("### kaggle"):
			st.write("### My kaggle Account")
			st.write("#### Links ")
			st.markdown(
				"[![Foo](https://storage.googleapis.com/kaggle-avatars/images/default-thumb.png)](https://www.kaggle.com/tuhinm2002)")




