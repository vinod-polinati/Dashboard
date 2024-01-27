import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lodu_coder = load_lottieurl('https://lottie.host/b832b791-3519-4874-8773-9f9c507ca77a/SUGUSvgL35.json')
lodu_contact = load_lottieurl("https://lottie.host/32340245-31b0-4a2b-891d-f535bb022a52/3axH3jpeXW.json")

image = Image.open("Images/face.webp")
image1 = Image.open("Images/lolniga.png")

# Define your skills here
skills_list = [
    "Python",
    "Machine Learning",
    "HTML, CSS , JavaScript",
    "C",
    "C++",
    "R",
    "MySQL",
]

skills_list = [
    "Python",
    "Machine Learning",
    "HTML, CSS , JavaScript",
    "C",
    "C++",
    "R",
    "MySQL",
    "Tableau",
]
skills_list = [
    "Python",
    "Machine Learning",
    "HTML, CSS , JavaScript",
    "C",
    "C++",
    "R",
    "MySQL",
]

def display_skills():
    st.header("Skills")
    st.write("##")
    
    # Display skills in two columns
    col1, col2 = st.columns(2)

    # Check the current theme and apply styles accordingly
    theme_style = """
        <style>
            .st-eq {
                padding: 1rem;
                border-radius: 10px;
                margin-bottom: 1rem;
                transition: background-color 0.3s;
            }
            .st-hv:hover {
                background-color: #ff4b4b;
                color: white !important;
            }
        </style>
    """
    dark_mode_style = """
        <style>
            .st-eq {
                background-color: #262730;
                box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
            }
        </style>
    """

    st.markdown(theme_style, unsafe_allow_html=True)

    # Check if the current theme is dark, then apply dark mode styles
    if st.get_option("theme.secondaryBackgroundColor") == "#262730":
        st.markdown(dark_mode_style, unsafe_allow_html=True)

    # Display skills in the first column
    with col1:
        st.subheader("Technical Skills")
        for skill in skills_list[:len(skills_list)//2]:
            st.markdown(f"<div class='st-eq st-hv'>- {skill}</div>", unsafe_allow_html=True)
    
    # Display skills in the second column
    with col2:
        st.subheader("Additional Skills")
        for skill in skills_list[len(skills_list)//2:]:
            st.markdown(f"<div class='st-eq st-hv'>- {skill}</div>", unsafe_allow_html=True)


# Main content
st.write("##")
st.subheader("Hey Guys :wave:")
st.title("Vinod Polinati")
st.write("""
A Junior Year Undergrad at Vignan's IIT. I'm interested in working as a Machine Learning, Deep Learning, Data Science Intern currently cooking a few Machine Learning Projects
""")

st.write("----")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Skills', 'Contact'],
        icons=['person', 'code-slash', 'graph-up', 'chat-left-text-fill'],
        orientation="horizontal"
    )

if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education 
            - Vignan's IIT
                - B.Tech in AI & Data Science
                - Grade: 8.4 
            
            - Narayana Junior College
                - Senior Secondary Education 
                - Grade: 80
            """)
        with col4:
            st.subheader("""
            Experience
            - Skill Vertex
                - Python Developer Intern
                - Developed a Machine Learning Model which recognizes handwritten digits from an image
                - Developed a Machine Learning Model which predicts whether a person gets affected by diabetes or not 
                - May 2023 ~ Jun 2023
            - SarvePriye Foundation
                - Content Writer 
                - Wrote several articles on women empowerment which got published on their website
                - March 2023 ~ May 2023
            """)
elif selected == "Projects":
    with st.container():
        st.header('My Projects')
        st.write("##")
        col5, col6 = st.columns((1, 2))
        col7, col8 = st.columns((1, 2))
        with col5:
            st.image(image)
        with col6:
            st.subheader("FacialiZe")
            st.write("""
            This is a Python-based Face Recognition Attendance System that uses machine learning to identify students' faces and records their attendance automatically.
            """)
            st.markdown("[Visit Git Repo](https://github.com/vinod-polinati/FacialiZe)")
        with col7:
            st.image(image1)
        with col8:
            st.subheader("VerifEye")
            st.write("""
            This is a machine learning model for detecting fake news by submitting either an article text or by pasting the URL of any news article.
            The UI is exclusively made using streamlit framework
            """)
            st.markdown('[Visit Git Repo](https://github.com/vinod-polinati/VerifEye)')
elif selected == 'Skills':
    display_skills()
elif selected == 'Contact':
    st.header("Get in Touch")
    st.write('##')
    st.write('##')
    contact_form = """
    <form action="https://formsubmit.co/86ad5b91559924c3b8a71d29d53bb2ad" method="POST">
        <input type='hidden' name='captcha' value='false'>
         <input type="text" name="name" required >
         <input type="email" name="email" required>
         <text area='message' placeholder="Message Required" </textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_col, right_col = st.columns((2, 1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(lodu_contact, height=300)
