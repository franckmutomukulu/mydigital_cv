from pathlib import Path

import streamlit as st
from PIL import Image


# --- Path setting
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
# resume_file = current_dir/"assets"/"cv.pdf"
profile_pic = current_dir/"assets"/"profile-pic.png"
project_pic = current_dir/"assets"/"python.png"



# ---- General Setting

PAGE_TITLE = "MyDigital_cv | Franck N Mutomukulu"
PAGE_ICON = ":computer"
NAME = "Franck N. Mutomukulu"
DESCRIPTION = """Software Engineer, Data analyst, QA Engineer, Network Engineer, Test Engineer """


EMAIL = "franckmutomukulu@gmail.com"
SOCIAL_MEDIA = {
    "🔌 LinkedIn":"https://www.linkedin.com/in/franck-mutomukulu-5b3434193/",
    "📖 Github":"https://github.com/franckmutomukulu/",
    "⚈⚈ Medium":"https://medium.com/@franckmutomukulu",
}
PROJECTS = {
    "Summerspub":"https://summerspub.com/",
    "Survey":"https://survey.fmnlepro.com/",
    "Ecomerce":"https://nezabuy.com/",
    "Neza-Lab":"https://nezalab.com",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Load css --
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# with open(resume_file,"rb") as pdf_file:
#     PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
project_pic = Image.open(project_pic)



# --- Hero Sectio
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # st.download_button(
    #     # label=" Download Resume",
    #     # data=PDFbyte,
    #     # file_name=resume_file.name,
    #     # mime="application/octet-stream",
    # )
    st.write(":book",EMAIL)
# ---- SOCIAL Media
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# -- Experience & Qualifications --
st.write("#")
st.subheader("INTRODUCTION & QUALIFICATIONS")
st.write(
       """ Software Engineer with 4+ years of experience in translating business requirements
 and functional specifications into code modules and software solutions. 
 Deep understanding of system integration testing (SIT) and user acceptance testing(UAT).
 Engages in the software development lifecycle to support developing, configuring, modifying, and testing
 testing integrated business and enterprise application solutions. Drives the adoption of new technologies 
 by researching innovative technology trends and developments, 
 Experienced in PYTHON, PHP, C++, SQL, Ionic, HTML, CSS and JIRA
 """
)
st.write(
    """
    - Ability to work on Back-end and Front-end development 
    - Excellent team- player and displaying strong sense of initiative on tasks
    - Excellent communication skills, Research, Business analysis, Tableau
    - Leadership, Strong decision make, Ability to learn new concepts quickly
    - Able to integrate in multicultural environment
    - Strong hands on experience and knowledge in Python
    """
)

# --- Skills
st.write("#")
st.subheader("SKILLS")
st.write(
    """
    - Programming Languages: PYTHON, PHP, C++, Kotlin, Ionic
    - Data Base: MySQL, SQL, Mongodb
    - API Testing: Postman
    - Design : HTML, CSS, JavaScript
    - Text Editing: Microsoft Office
    - Agile Management Tools: JIRA, MONDAY.COM, ASANA
    - Video Editing and Picture Editing Tools: Photoshop, Premiere Pro, Pinnacles
    """
)

# --- Langage
st.write("#")
st.subheader("LANGUAGES")
st.write(
    """
    - English 
    - French
    - Chinese (Conversational)
    - Swahili
    - Lingala
    """
)


# --- Work History --
st.write("#")
st.subheader("PROFESSIONAL WORK EXPERIENCES")
st.write("---")

# -----JOB 1
st.write("", "**SOFTWARE ENGINEER | SWISSPORT**")
st.write("07/2022 - Present")
st.write(
    """
    - Build and deploy web applications and mobile application on server.
    - Work with developers to design algorithms.
    - Produce clean, efficient code based on specifications.
    - Modified html, JavaScript and Css to optimize web applications.
    - Test and maintenance of project.
    """
)

# -----JOB 2
st.write("", "**SOFTWARE ENGINEER | NEZA-LAB**")
st.write("01/2019 - 03/2022 ")
st.write(
    """
    - Code and script applications, Maintenance of website.
    - Build website, Provide continued support for one or more web properties.
    - Maintain communication with team members and supervisors concerning the direction of the website.
    - Troubleshoot, debug and upgrade existing software.
    - Verify and deploy programs and systems.
    """
)

# -----JOB 3
st.write("", "**ELECTRONICS ENGINEER | VISIBILITY360**")
st.write("01/2015 - 03/2017 ")
st.write(
    """
    - Design electronic systems, products, software and components for scientific, military, medical, industrial and commercial applications.
    - Create testing procedures and maintenance for electronic equipment and components.
    - Recommend design modifications and equipment repair.
    - Inspect electronic systems, instruments and equipment to ensure they meet applicable regulations and safety standards.

    """
)




# ---- Eduction --
st.write("#")
st.subheader("EDUCATION")
st.write("---")
st.write("""
    - 2020: Master Degree In Software Engineering\n
            Zhejiang Normal University | China
    - 2017: Bachelor Degree In Appy Electronics\n
            Ista | Dr. Congo
    - 2013: High School Diploma\n
            Institut Professionnel dela Gombe | Dr.Congo
""")

# ---- Project & Accomplishments --
st.write("#")
st.subheader("PROJECTS & ACCOMPLISHMENTS")
st.write("---")
col1,col2 = st.columns(2,gap="small")
with col1:
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")
with col2:
    st.image(project_pic, width=190)








