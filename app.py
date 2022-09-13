from pathlib import Path
import streamlit as st

# used to import image
from PIL import Image

# ---path settings-----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# cwd-current working directory
css_file = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "CV.pdf"
# profile_pic = current_dir / "assests" / "profile.png"


# -----General Settings----
PAGE_TITLE = "Digital CV | Ashutosh Raj Gupta"
PAGE_ICON = ":wave:"
NAME = "Ashutosh Raj Gupta"
DESCRIPTION = """
Front end Developer, Flutter Developer, Exploring Streamlit.
"""
EMAIL = "ag2364443@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/profile.php?id=100022615870474",
    "LinkedIn": "https://www.linkedin.com/in/ashutosh-raj-gupta-18230820b/",
    "GitHub": "https://github.com/AshutoshRajGupta/AshutoshRajGupta",
    "Portfolio": "https://portfolio-ashutosh.netlify.app/",
}
PROJECTS = {
    "🏆 Portfolio website- including all my projects ": "https://portfolio-ashutosh.netlify.app/",
    "🏆 Hiyo - Expense Tracker App - Android application made with flutter": "https://github.com/AshutoshRajGupta/Hiyo-1",
    "🏆 Xphouse - Web Application": "https://github.com/AshutoshRajGupta/Xp-House",
    "🏆 Connect us page - made using Streamlit and python": "https://github.com/AshutoshRajGupta/connect-us-page-streamlit",
    "🏆 To-Do App- A website made with react": "https://todo-app-delta-beryl.vercel.app/",
    "🏆 Keep-Notes App- A website made with react": "https://keep-notes-app-alpha.vercel.app/",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# ---load css,pdf and profile pic---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
#profile_pic = Image.open(profile_pic)


# -----HERO SECTION-----
#col1, col2 = st.columns(2, gap="small")
#with col1:
    #st.image(profile_pic, width=230)
    #st.write("Hello ")
#col2=st.columns(1)
with st.container():
    st.header("Hey !!! Myself ")
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
    """
- ✔️ 1 Years expereince in Front end Development
- ✔️ 1 Years expereince in ACES DYPCOE as Publicity Team Member
- ✔️ Strong hands on experience and knowledge in Python and Html,CSs And Javascript
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Numpy,Pandas,), SQL, MySQL,C++,
- 📊 Data Visulization: MS Excel
- 📚 Frameworks: React Js,Flutter,Streamlit
- 🗄️ Databases: MongoDB, MySQL,SQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Publicity Team Member | ACES DYPCOE**")
st.write("02/10/2021 - 02/09/2022")
st.write(
    """
- ► ACES stands for Association of Computer Engineering Student.
- ► Design various posters and design for the event organised by ACES under Publicity team.
- ► Learn many skills from community which enhance my personality.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# ---certifications----
with st.container():
    st.header("CERTIFICATIONS")
    st.write("---")
    st.write("[BASICS OF PYTHON - link](https://udemy-certificate.s3.amazonaws.com/image/UC-e442c3b5-b993-4f05-9ca5-18b0881c2cce.jpg)")
    st.write("[SQL CERTIFICATION - link](https://udemy-certificate.s3.amazonaws.com/image/UC-c11bc08e-b0f0-445a-a042-ef8917a08237.jpg)")
    st.write("[HTML CERTIFICATION - link](https://www.sololearn.com/Certificate/CT-CMYLLQGB/jpg)")
    st.write("[PYTHON FOR DATA ANALYSIS - link](https://udemy-certificate.s3.amazonaws.com/image/UC-06476e45-241e-4d52-a89f-d2c29c067f41.jpg)")

