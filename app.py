import streamlit as st
from pathlib import Path
from PIL import Image


# --- PATH SETTINGS ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / 'assets' / 'cv.pdf'

# --- DEFINE IMAGES --- 
jump_image = Image.open('assets/jump.png')
balance_image = Image.open('assets/balance.png')
medory_image = Image.open('assets/medory.png')
linkedin_image = Image.open('assets/linkedin_logo.png')


# --- GENERAL SETTINGS ---

PAGE_TITLE = "Personal Site | CV | George"
PAGE_ICON = 'random:'
NAME = "George"
DESCRIPTION = """
**Hello! I am George,**

**I created this Streamlit application where I will present here, as a personal portfolio, only the Streamlit applications. If you wanna see more about me below i have my links. Thank you.**

"""
EMAIL = "send@geth.gr"

SOCIAL_MEDIA = {
    "Website": "https://geth.gr",
    "LinkedIn": "www.linkedin.com/in/georgetheof",
    "GitHub": "https://github.com/gethgr",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC --- 
with open(css_file) as f:
    st.write("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


st.title('Personal Streamlit Apps Place')
st.subheader('Hello! I am George')
st.subheader('**I created this Streamlit page where I will present here, as a personal portfolio, only the Streamlit applications. If you wanna see more about me below i have my links. Thank you.**')

# --- SOCIAL LINKS ---
st.write("#")

social1,social2,social3 = st.columns(3)
with social1:
    st.write("[Website](http://geth.gr)")
with social2:
    st.write("[Linkedin](www.linkedin.com/in/georgetheof)")
with social3:
    st.write("[GitHub](https://github.com/Altemode)")

st.write("---")


#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([1,4], gap='small')
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,5])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.7,3,5])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)




##### 1o APP #####
st.title("Jump Metrcis")
st.image(jump_image, caption='Sunrise by the mountains')
#####################

st.write("**Jumps Metrics :** is a Python data analysis web app using Streamlit as a frontend for collectng raw data of a person using a force platform with sensors to measure Jumps and extra various indicators.")
# txt('**Jumps Metrics** is a Python data analysis web app using Streamlit as a frontend for collectng raw data of a person using a force platform with sensors to measure Jumps and extra various indicators.',
# '[App](https://jumpmetric.streamlit.app)')
st.markdown('**Feutures :**')
st.markdown('''
- Prepare File : The user is able to prepare the file with raw data.
- Inert New Entry : The user is able to insert new entry trial into database.
- Calculate Results : In this page the user can run any of the trials and calculate all the results.
- Statistics : Various statistics will be displayed from this page.
''')
with st.expander("More description"):
    st.write("""
        Jump Metrics for the purpose of research of School of Physical Education and Sports Science of Athens. For this purpose a force platform by PLUX Biosignals has been used to test various jumps trials and collects the raw data of athletes.

The main scope of this research is to collect raw data, transform and processing them into usable data, calculate and measure various indicators and export final results to create useful conclusions depending of the needs.

For this reason i choose to use Streamlit App Framework to create a nice and clean web app let the users to navigate very easy into the functionalities. At this point, we should mention that we check various jumps, specifically: Counter Jump, Drop Jump, Isometric, Squad Jump.
    """)
st.write("#")


txt3('**Packages used :**', '`altair`, `biosignalsnotebooks`, `numpy`, `pandas`, `plotly`, `streamlit`, `supabase`, `sympy`, `bokeh`')

txt('[Streamlit](https://medory.streamlit.app)','[GitHub](https://medory.streamlit.app)')




##### 2o APP #####
st.write("#")
st.write("---")
st.title("Balance")
st.image(jump_image, caption='Sunrise by the mountains')
#####################

st.write("**Balance :** is a Python data analysis web app using Streamlit as a frontend for collectng raw data of a person using a force platform with sensors to measure Jumps and extra various indicators.")
# txt('**Jumps Metrics** is a Python data analysis web app using Streamlit as a frontend for collectng raw data of a person using a force platform with sensors to measure Jumps and extra various indicators.',
# '[App](https://jumpmetric.streamlit.app)')
st.markdown('**Feutures :**')
st.markdown('''
- Prepare File : The user is able to prepare the file with raw data.
- Inert New Entry : The user is able to insert new entry trial into database.
- Calculate Results : In this page the user can run any of the trials and calculate all the results.
- Statistics : Various statistics will be displayed from this page.
''')
with st.expander("More description"):
    st.write("""
        Balance App developed for the purpose of research of School of Physical Education and Sports Science of Athens. For this purpose a force platform by PLUX Biosignals has been used to test various jumps trials and collects the raw data of athletes.

The main scope of this app is to be calculate the ballance of athletes by collecing raw data from the force platform, proccesing these and calculating the center of pressure in the x and y axis (ML & AP).

For these reason the streamlit app framework was a great choice to transform the python code into a nice wep app.
    """)
st.write("#")


txt3('**Packages used :**', '`altair`, `biosignalsnotebooks`, `numpy`, `pandas`, `plotly`, `streamlit`, `supabase`, `sympy`, `bokeh`')

txt('[Streamlit](https://balance.streamlit.app)','[GitHub](https://github.com/Altemode/balance-metrics-streamlit-prod)')



##### 3o APP #####
st.write("#")
st.write("---")
st.title("Medory")
st.image(medory_image, caption='Sunrise by the mountains')
#####################

st.write("**Medory :** is a Python data analysis web app using Streamlit as a frontend for collectng raw data of a person using a force platform with sensors to measure Jumps and extra various indicators.")
# txt('**Jumps Metrics** is a Python data analysis web app using Streamlit as a frontend for collectng raw data of a person using a force platform with sensors to measure Jumps and extra various indicators.',
# '[App](https://jumpmetric.streamlit.app)')
st.markdown('**Feutures :**')
st.markdown('''
- Entering a new user into the database by declaring personal information, such as name, age, weight, etc.
- Input of medical test results by type of test.
- Delete data, this section is under developing.
- Display medical test results for each user on each type of medical test.
- Display graphs per user for each type of medical examination, by specific medical indicator and selecting the chronological date.
''')
with st.expander("More description"):
    st.write("""
        This application is written in Python code and built using the Streamlit App Framework and uses a PostgreSQL database. It is a multilingual and multi-page application with the purpose of storing for each user medical data for each type of examination, making calculations, presenting the results in graphs, tables and much more.

It is a multi-page application using PostgreSQL database through the open source Supabase platform.

It is a multilingual app using gettext python package to create .mo files and strings ready for translation.
    """)
st.write("#")

txt3('**Packages used :**', '`numpy`, `pandas`, `numpy`, `Pillow`, `plotly`, `streamlit`, `streamlit_option_menu`')

txt('[Streamlit](https://medory.streamlit.app)','[GitHub](https://github.com/Altemode/medory-analysis-streamlit)')

