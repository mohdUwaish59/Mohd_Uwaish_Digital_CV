from pathlib import Path

import streamlit as st
from PIL import Image, ImageDraw

from streamlit_card import card

st.set_page_config(layout="wide")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume_Mohd-Uwaish.pdf"
profile_pic = current_dir / "assets" / "photo.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Mohd Uwaish"
PAGE_ICON = ":wave:"
NAME = "Mohd Uwaish"
DESCRIPTION = """ Masters' Student |  Former Software Engineer | Data Science Enthusiast"""
EMAIL = "mohd.uwaish@stud.uni-goettingen.de"
ADDRESS = "520, Robert-Koch-Strasse 38, Göttingen 37075, Germany"
STUDY = "Georg‑August‑Universität, Göttingen"
PROJECTS = {
    "🏆 Digital Danke Schön - Full Stack Consulation and Blog portal": "https://github.com/mohdUwaish59/Digital_Danke_Schoen",
    "🏆 WebScout - Text and Image Scrapper": "https://github.com/mohdUwaish59/Web-Scout",
    "🏆 WhatsAppWordsmith - Whatsapp and Telegram Chat Analysis": "https://github.com/mohdUwaish59/WhatsAppWordsmith",
    "🏆 Dialing Hope -  Examining and Visualizing the 988 Suicide Helpline in the United States": "https://github.com/mohdUwaish59/988_Helpline_Data_Analysis_Visualization",
}





# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
container = st.container()
with container:
    col1, col2 = st.columns(2,gap="small")
    with col2:
        st.image(profile_pic, width=230)
    with col1:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
        dds = "https://www.digitaldankeschoen.com/"
        st.markdown(f"Developing - [👉Digital Danke Schön👈]({dds})")
        st.write("📫", EMAIL)
        st.write("🏠", ADDRESS)
        st.write("📚📖🏫", STUDY)


# GitHub, LinkedIn, Kaggle, and Xing links
github_link = "https://github.com/mohdUwaish59"
linkedin_link = "https://www.linkedin.com/in/mohd-uwaish-72b779282/"
kaggle_link = "https://www.kaggle.com/mohduwaish"
xing_link = "https://www.xing.com/profile/Mohd_Uwaish/cv"

# Use columns to align icons horizontally
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f'[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github)]({github_link})')

with col2:
    st.markdown(f'[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({linkedin_link})')

with col3:
    st.markdown(f'[![Kaggle](https://img.shields.io/badge/Kaggle-Profile-blue?style=for-the-badge&logo=kaggle)]({kaggle_link})')

with col4:
    st.markdown(f'[![Xing](https://img.shields.io/badge/Xing-Profile-blue?style=for-the-badge&logo=xing)]({xing_link})')

# Define a function to display software development skills
def software_dev_skills():
    st.header("Software Development Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        card(title="Programming Languages",
              text="JavaScript, Python, Java"
              )
    with col2:
        card(title="Front-End Development", text="HTML, CSS, React.js")
    with col3:
        card(title="Back-End Development", text="Node.js, Django, Flask")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        card(title="Databases", text="SQL, NoSQL (MongoDB)")
    
    with col2:
        card(title="DevOps", text="Git, Docker, Kubernetes, CI/CD")
    with col3:
        card(title="Web Services", text="RESTful API, GraphQL")

    col1, col2,col3 = st.columns(3)
    with col1:
        card(title="Testing", text="Unit Testing, Integration Testing, Test Automation")
    with col2:
        card(title="Soft Skills", text="Communication, Problem-Solving, Teamwork, Time Management, Adaptability")
    with col3:
        card(title="Cloud Computing", text="AWS, Azure, Google Cloud")
        


# Define a function to display data science skills
def data_science_skills():
    st.header("Data Science Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        card(title = "Programming Languages", text = "Python, PLSQL")
    with col2:
        card(title = "Databases", text = "Relational DB: MySQL, Oracle SQL\n- NO SQL DB: MongoDB")
    with col3:
        card(title = "Statistics and Mathematics", text = "Linear Algebra, Calculus, probability distributions, hypothesis testing, and statistical modeling.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        card(title = "Data Manipulation and Analysis", text = "Pandas, SQL")
    with col2:
        card(title = "Data Visualization", text = "Matplotlib and Seaborn, Tableau, Power BI")
    with col3:
        card("Machine Learning Libraries", "Scikit-Learn, TensorFlow, XGBoost, LightGBM")

    col1, col2, col3 = st.columns(3)
    with col1:
        card("Deep Learning", "Basics of Neural Networks and Convolutional Neural Networks")
    with col2:
        card("Model Evaluation and Validation", "Metrics such as accuracy, precision, recall, F1-score, etc.")
    with col3:
        card("Feature Engineering", "Feature selection, Feature extraction, Scaling and Normalization, Binning and Discretization")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        card("Machine Learning Workflow", "Data preprocessing, Model selection, Hyperparameter tuning")
    with col2:
        card("Cloud Computing", "AWS, Heroku")
    with col3:
        card("Version Control", " Git: Proficiency in version control for collaboration and code management")

    col1, col2, col3 = st.columns(3)
    with col1:
        card("Deployment and Productionization", "Docker, Kubernetes, Streamlit, Flask, Django, CI/CD Pipelines")
    with col2:
        card("Natural Language Processing (NLP)", "NLTK, Word2Vec, BERT")
    with col3:
        card("Time Series Analysis", "ARIMA, Prophet")

    col1, col2 = st.columns(2)
    with col1:
        card("Soft Skills", "Communication: Ability to explain complex findings to non-technical stakeholders.\n- Problem-Solving: Critical thinking and creativity in approaching data-related challenges.")
    with col2:
        card("Ethical and Legal Considerations", "Understanding of data privacy, bias, and responsible AI practices")






# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.info(
    """
- ✔️ 1.8 Years of Experience as a Software Developer.
- ✔️ Strong hands on experience and knowledge in Java, Javascript and Python.
- ✔️ Aspiring data scientist with a strong foundation in data analysis and statistics.
- ✔️ Good understanding of statistical principles and their respective applications.
- ✔️ Deep understanding of data visualization libraries and tools.
- ✔️ Basic knowledge of data mining and information extraction from unstructured data.
- ✔️ Exposure to machine learning concepts and eager to expand knowledge in this area.
- ✔️ Developing skills in using SQL for data querying and database management.
- ✔️ Proactive in staying updated with the latest trends in data science.
- ✔️ Clear communication skills for presenting findings to peers and team members.
- ✔️ Keen problem-solving abilities and a strong desire to tackle data-related challenges.
- ✔️ Committed to ethical data practices and compliance with data privacy regulations.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)



def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

#st.markdown('''
## Skills
#''')
#txt3('Programming', '`Python`, `R`, `Linux`')
#txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
#txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
##txt3('Machine Learning', '`scikit-learn`')
#txt3('Deep Learning', '`TensorFlow`')
#txt3('Web development', '`Flask`, `HTML`, `CSS`')
#txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write("---")
# Add buttons to switch between software development and data science sections
col1, col2 = st.columns(2)
with col1:
    ds = st.button("Data Science Skills")

with col2:
    sft = st.button("Software Development Skills")


if sft:
    software_dev_skills()
    
if ds:
    data_science_skills()

def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

st.markdown('''
## Education
''')
st.write("---")
txt('**Master of Science** ‑ MS in Applied Computer Science with specialization in Data Science, *Georg‑August‑Universität*, Göttingen',
'01/04/2023 ‑ PRESENT')


txt('**Bachelor of technology** ‑ BTech in Computer Science and Engineering, *Guru Gobind Singh Indraprastha University*, India',
'01/05/2017 – 30/05/2021')
minor = "https://drive.google.com/drive/folders/1NfwB24ADDKuEFIjGW2URhggdLh4M9vbM?zx=8ejbmhtpbefd"
major = "https://drive.google.com/drive/folders/1VHybcFZ63F77f2S4l3YbyE24C8zjT2hY?zx=8ejbmhtpbefd"
st.markdown(f'''
- CGPA: `8.01`/10
- Thesis: [`Eth‑Ocracy: Ethereum Blockchain based Voting System`] - [Project Report Here]({major})
            
- Minor Project: [`Video Recommendation System`] - [Project Report Here]({minor})
''')


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experience")
st.write("---")
# --- JOB 1
st.write("🚧", "**Software Engineer | Tata Consultancy Services Private Limited**")
st.write("08/09/2021 – 10/04/2023")
st.write(
    """
- • Worked on the development of the Income Tax Business Application (ITBA) for the Indian Government’s Income Tax Department, acritical project serving, Income Tax officers and millions of taxpayers.
- • Developed full‑stack solutions for the PENALTY module of the ITBA using HTML, CSS, JavaScript, Java, PL/SQL and Oracel Database to build a robust and scalable web‑based tax processing system.
- • Engineered a highly efficient web‑based tax filing system, resulting in a `20%` increase in user engagement and a `15%` reduction in processing time for tax filings.
- • Implemented complex business logic and dynamic functionalities in the back‑end by writing optimized Java code integrated with Oracle database.
- • Designed and executed database queries, PL/SQL procedures, triggers, and functions, optimizing data models and achieving a `18%`reduction in database response time to enhance UI responsiveness.
- • Regularly identified and resolved over `100` bugs and technical issues reported by quality assurance and support teams, ensuring a smooth and uninterrupted user interface performance.
- • Collaborated with cross‑functional teams, including architects, business analysts, and software testers, achieving an on‑time delivery rate of `96%` for project milestones.
- • Written well‑documented code compliant with software development standards and guidelines.
- • Leveraged Agile methodologies to iteratively develop and deploy functionalities, resulting in `9` successful change requested and 3 new functionalities release in a fast‑paced environment, consistently aligned with evolving user requirements.

"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    if project == "🏆 Digital Danke Schön - Full Stack Consulation and Blog portal":
        st.write(f"[{project}]({link})")
        if st.button("Open Portal☝"):
            js_code = "https://www.digitaldankeschoen.com/"
            st.markdown(js_code, unsafe_allow_html=True)
    elif project == "🏆 WhatsAppWordsmith - Whatsapp and Telegram Chat Analysis":
        st.write(f"[{project}]({link})")
        if st.button("Go to Website☝"):
            js_code = "https://mohduwaish59-whatsappwordsmith-app-fywxax.streamlit.app/"
            st.markdown(js_code, unsafe_allow_html=True)
    else:
        st.write(f"[{project}]({link})")
