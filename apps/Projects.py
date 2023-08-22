import json
from PIL import Image
import streamlit as st
import streamlit_lottie
def load_lottiefile(filepath):
	with open(filepath, "r") as f:
		return json.load(f)
def app():
    # st.write("https://ml-drug-sars.onrender.com")
    st.title("Tuhin's Projects")
    lottie_coding = load_lottiefile("animation_project.json")
    streamlit_lottie.st_lottie(lottie_coding, loop=True)
    col1,col2 = st.columns(2)
    col3,col4 = st.columns(2)
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
            st.markdown("[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/Tuhinm2002/spam-classifier/)")
            st.markdown("[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAtFBMVEX////gsbH26em3HyTBUVS8PD//JCT/iIj/+PjbpKW6MDS9QEOvjI96LjX/pqb/AAD/mJi3Iia5m51yFiC/paf/8PD/Kyv/GRn/ERF1ISl9NTtwDxv07+//X1//s7PKtbaVY2b/w8P/MTHUxMV1ICj/HR3TPT+4QUT/kpL0MzPOP0GnP0N4NDr/6emMOj//U1ONVFjrNjfiOTurhon/39+eISjj29z/fX3gfX7/1NT/bW3/W1uaV1tlAAAA6ElEQVR4AeXORXYDQQxFUbmZqstYZGYOx7j/fUVNCnsDvuN/9AT3qVaDmyzbtuAWx3Ud+M7zAyBhFMdRCCRIGKSc1ynQiFGDIs1Wqw0dLqRKq0CMqkhba9PtAfQ9IaQ3KAOoiAyZNoaNAGCsBFKTcREoIlOjDZpNAUmRU/PFslpE2uQ0ZFZzUVpvqsl2ZxBLILPngtDkwaCWBblHT3yZuMUET7AnQPQmeY6XRUQPoUSDLxOMtKDiV2+SF1ywV6i80ZtfJ+8HIEfOlZLzuZebz6VSnJ/gq/15nK6Ol/712r8cV+n4vIe78gHQ5B8DWKNMwgAAAABJRU5ErkJggg==)](https://spam-classifier-a0li.onrender.com)")
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
            st.markdown("[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/Tuhinm2002/ML_Drug_Discovery/)")
            st.markdown("[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAtFBMVEX////gsbH26em3HyTBUVS8PD//JCT/iIj/+PjbpKW6MDS9QEOvjI96LjX/pqb/AAD/mJi3Iia5m51yFiC/paf/8PD/Kyv/GRn/ERF1ISl9NTtwDxv07+//X1//s7PKtbaVY2b/w8P/MTHUxMV1ICj/HR3TPT+4QUT/kpL0MzPOP0GnP0N4NDr/6emMOj//U1ONVFjrNjfiOTurhon/39+eISjj29z/fX3gfX7/1NT/bW3/W1uaV1tlAAAA6ElEQVR4AeXORXYDQQxFUbmZqstYZGYOx7j/fUVNCnsDvuN/9AT3qVaDmyzbtuAWx3Ud+M7zAyBhFMdRCCRIGKSc1ynQiFGDIs1Wqw0dLqRKq0CMqkhba9PtAfQ9IaQ3KAOoiAyZNoaNAGCsBFKTcREoIlOjDZpNAUmRU/PFslpE2uQ0ZFZzUVpvqsl2ZxBLILPngtDkwaCWBblHT3yZuMUET7AnQPQmeY6XRUQPoUSDLxOMtKDiV2+SF1ywV6i80ZtfJ+8HIEfOlZLzuZebz6VSnJ/gq/15nK6Ol/712r8cV+n4vIe78gHQ5B8DWKNMwgAAAABJRU5ErkJggg==)](https://ml-drug-sars.onrender.com)")


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

    with st.expander("### My Github"):
        st.markdown(
            "[![Foo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/Tuhinm2002/)")
