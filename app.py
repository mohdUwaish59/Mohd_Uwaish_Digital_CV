from pathlib import Path

import streamlit as st
from PIL import Image, ImageDraw



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume_Mohd-Uwaish.pdf"
profile_pic = current_dir / "assets" / "mohd.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Mohd Uwaish"
PAGE_ICON = ":wave:"
NAME = "Mohd Uwaish"
DESCRIPTION = """ Masters' Student |  Former Software Engineer | Data Science Enthusiast"""
EMAIL = "mohd.uwaish@stud.uni-goettingen.de"

PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# GitHub, LinkedIn, Kaggle, and Xing links
github_link = "https://github.com/mohdUwaish59"
linkedin_link = "https://www.linkedin.com/in/mohd-uwaish-72b779282/"
kaggle_link = "https://www.kaggle.com/mohduwaish"
xing_link = "https://www.xing.com/profile/Mohd_Uwaish/cv"

# Use columns to align icons horizontally
col1, col2 = st.columns(2)

with col1:
    st.markdown(f'[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github)]({github_link})')

with col2:
    st.markdown(f'[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({linkedin_link})')

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'[![Kaggle](https://img.shields.io/badge/Kaggle-Profile-blue?style=for-the-badge&logo=kaggle)]({kaggle_link})')

with col2:
    st.markdown(f'[![Xing](https://img.shields.io/badge/Xing-Profile-blue?style=for-the-badge&logo=xing)]({xing_link})')

# Define a function to display software development skills
def software_dev_skills():
    st.header("Software Development Skills")
    st.write("---")
    st.write("Programming Languages: JavaScript, Python, Java")
    st.write("Front-End Development: HTML, CSS, React.js")
    st.write("Back-End Development: Node.js, Django, Flask")
    st.write("Databases: SQL, NoSQL (MongoDB)")
    st.write("Version Control: Git")
    st.write("DevOps: Docker, Kubernetes, CI/CD")
    st.write("Web Services: RESTful API, GraphQL")
    st.write("Cloud Computing: AWS, Azure, Google Cloud")
    st.write("Testing: Unit Testing, Integration Testing, Test Automation")
    st.write("Soft Skills: Communication, Problem-Solving, Teamwork, Time Management, Adaptability")

# Define a function to display data science skills
def data_science_skills():
    st.header("Data Science Skills")
    st.write("---")
    st.write("1. Programming Languages:")
    st.write("   - Python, PLSQL")
    st.write("---")

    st.write("2.  Databases:")
    st.write("   - Relational DB: MySQL, Oracle SQL")
    st.write("   - NO SQL DB: MongoDB")
    st.write("---")
    
    st.write("2. Statistics and Mathematics:")
    st.write("   - Linear Algebra,Calculus, probability distributions, hypothesis testing, and statistical modeling.")
    st.write("---")
    
    st.write("3. Data Manipulation and Analysis:")
    st.write("   - Pandas, SQL")
    st.write("---")
    
    st.write("4. Data Visualization:")
    st.write("   - Matplotlib and Seaborn,Tableau, Power BI")
    st.write("---")
    st.write("5. Machine Learning Libraries:")
    st.write("   - Scikit-Learn, TensorFlow, XGBoost, LightGBM")
    st.write("---")
    st.write("6. Deep Learning:")
    st.write("   - Basics of Neural Networks and Convolutional Neural Networks ")
    st.write("---")
    st.write("7. Model Evaluation and Validation and Metrics such as accuracy, precision, recall, F1-score, etc.")
    st.write("---")
    st.write("8. Feature Engineering:")
    st.write("   - Feature selection, Feature extraction, Scaling and Normalization, Binning and Discretization,")
    st.write("---")
    st.write("9. Machine Learning Workflow:")
    st.write("   - Data preprocessing, Model selection, Hyperparameter tuning")
    st.write("---")
    st.write("10. Cloud Computing:")
    st.write("   - AWS, Azure, Google Cloud: Familiarity with cloud platforms for scalable computing and data storage.")
    st.write("---")
    st.write("12. Version Control:")
    st.write("   - Git: Proficiency in version control for collaboration and code management.")
    st.write("---")
    st.write("13. Deployment and Productionization:")
    st.write("   - Docker and Kubernetes, Streamlit, Flask, Django, Continuous Integration/Continuous Deployment (CI/CD)")
    st.write("---")
    st.write("14. Natural Language Processing (NLP):")
    st.write("   - NLTK and spaCy, Word2Vec, GloVe, and BERT.")
    st.write("---")
    st.write("15. Time Series Analysis:")
    st.write("   - ARIMA and Prophet")
    st.write("---")
    st.write("17. Soft Skills:")
    st.write("   - Communication: Ability to explain complex findings to non-technical stakeholders.")
    st.write("   - Problem-Solving: Critical thinking and creativity in approaching data-related challenges.")
    st.write("   - Teamwork: Collaboration with cross-functional teams.")
    st.write("---")
    st.write("18. Ethical and Legal Considerations:")
    st.write("   - Understanding of data privacy, bias, and responsible AI practices.")






# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
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


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write("---")
# Add buttons to switch between software development and data science sections
if st.button("Software Development Skills"):
    software_dev_skills()
if st.button("Data Science Skills"):
    data_science_skills()


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Engineer | Tata Consultancy Services Private Limited**")
st.write("08/09/2021 – 10/04/2023")
st.write(
    """
- • Worked on the development of the Income Tax Business Application (ITBA) for the Indian Government’s Income Tax Department, acritical project serving, Income Tax officers and millions of taxpayers.
- • Developed full‑stack solutions for the PENALTY module of the ITBA using HTML, CSS, JavaScript, Java, PL/SQL and Oracel Database to build a robust and scalable web‑based tax processing system.
- • Engineered a highly efficient web‑based tax filing system, resulting in a 20% increase in user engagement and a 15% reduction in processing time for tax filings.
- • Implemented complex business logic and dynamic functionalities in the back‑end by writing optimized Java code integrated with Oracle database.
- • Designed and executed database queries, PL/SQL procedures, triggers, and functions, optimizing data models and achieving a 18% reduction in database response time to enhance UI responsiveness.
- • Regularly identified and resolved over 100 bugs and technical issues reported by quality assurance and support teams, ensuring a smooth and uninterrupted user interface performance.
- • Collaborated with cross‑functional teams, including architects, business analysts, and software testers, achieving an on‑time delivery rate of 96% for project milestones.
- • Written well‑documented code compliant with software development standards and guidelines.
- • Leveraged Agile methodologies to iteratively develop and deploy functionalities, resulting in 9 successful change requested and 3 new functionalities release in a fast‑paced environment, consistently aligned with evolving user requirements.

"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
