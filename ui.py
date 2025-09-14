import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Career Assessment", "CEI Score", "Resume Builder"])

# Home Page

if page == "Home":
    st.title("🎯 Personalized Career & Skills Advisor")
    st.write("""
    Welcome to our prototype for the **Hackathon Submission**.  
    This platform is designed to help users bridge the gap between **skills and employability**.
    
    🔹 Key Features:
    - AI-powered Career Assessment  
    - Continuous Employability Index (CEI Score)  
    - AI Resume Builder with ATS Optimization  

    Use the sidebar to explore each feature of the prototype.
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=200)

    st.success("👉 Navigate using the sidebar to test our prototype features.")

# Page 1: Career Assessment

elif page == "Career Assessment":
    st.title("Career Assessment")
    st.write("Get personalized career suggestions based on your skills and interests.")

    skills = st.text_input("Enter your current skills (comma separated):")
    interests = st.text_input("Enter your career interests:")

    if st.button("Analyze Profile"):
        st.success(f"Based on your skills: {skills} and interests: {interests}, "
                   f"we suggest roles in **Data Analysis** and **AI Engineering**.")
        st.write("👉 Suggested Next Step: Learn Python, SQL, and Machine Learning basics.")

# Page 2: CEI Score

elif page == "CEI Score":
    st.title("Continuous Employability Index (CEI)")
    st.write("Track how employable you are with a dynamic score.")

    cei = 72  # Example static value for prototype
    st.progress(cei/100)
    st.metric("Your CEI Score", f"{cei}/100")

    st.write("🎯 To improve your CEI Score:")
    st.write("- Complete at least 2 certifications")
    st.write("- Work on a real-world project")
    st.write("- Improve communication & problem-solving skills")

# Page 3: Resume Builder

elif page == "Resume Builder":
    st.title("AI Resume Builder & Optimizer")
    st.write("Upload your resume to check ATS readiness and improvement suggestions.")

    uploaded = st.file_uploader("Upload your resume (PDF/DOCX)", type=["pdf", "docx"])
    if uploaded:
        st.info("✅ Resume scanned successfully.")
        st.write("Your resume currently matches **65%** with top job market trends.")
        st.write("💡 Suggestions to improve:")
        st.write("- Add technical keywords such as 'Python', 'SQL', 'Data Visualization'")
        st.write("- Highlight measurable achievements instead of generic statements")
        st.write("- Include project links (GitHub/Portfolio)")
