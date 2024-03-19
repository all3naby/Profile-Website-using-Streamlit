import streamlit as st
import requests
import streamlit_lottie as st_lottie
from PIL import Image

st.set_page_config(page_title="My webpage", page_icon=":blue_book:", layout="wide")

#Used to get gif from Lottie website
def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Used to load css
def load_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#load assets
load_css("style/style.css")
lottie_animation_file = load_lottieurl("https://lottie.host/a810fcd3-72d6-4e5b-ac89-1f2822b4f7c6/ED4jnqKDAX.json")
project_image = Image.open("images/luffy.jpg")

# Header
with st.container():
    st.subheader("Hi, I'm Allen Aby")
    st.title("RPA Developer")
    st.markdown("[Linkedin page >](https://www.linkedin.com/in/allenaby/)")

# What I do
with st.container():
    st.write("---")
    # to split screen into 2 equal columns
    left,right = st.columns(2)
    with left:
        st.header("What I do")
        st.write("##")
        st.write("I am currently working as an RPA developer in Cooperators")
    
    with right:
        st_lottie.st_lottie(lottie_animation_file,height="300",key="coding")

# Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    # to split screen into 2 columns, column B = 2 column A
    image_column,text_column = st.columns((1,2))
    with image_column:
        # insert image
        st.image(project_image)
    
    with text_column:
        st.subheader("RPA work sort")
        st.write(
            """
            Trigger based process that logins into Guidewire and assigns work out of inputed queues to UWs
            by using a excel file to keep track of the work assigned out.
"""
        )
        st.markdown("[Link to Guidewire](https://www.guidewire.com)")

with st.container():
    st.write("---")
    st.header("Contact Form")
    st.write("##")
    # From https://formsubmit.co
    contact_form = """
            <form action="https://formsubmit.co/allen.aby.007@gmail.com" method="POST">
                <input type="text" name="name" placeholder="Your Name" required>
                <input type="email" name="email" placeholder="Your Email"  required>
                <textarea name="message" placeholder="Your message goes here" ></textarea>
                <button type="submit">Send</button>
            </form>
    """
    left, right = st.columns(2)
    with left:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right:
        st.empty()