import streamlit as st
from streamlit_option_menu import option_menu
from deta import Deta

selected2 = option_menu(None, ["Course Outcome Survey Form", "Alumini survey form","Guest lecture Feedback"], 
    icons=['house', "bi-app-indicator","book-fill"], 
    menu_icon="cast", default_index=0, orientation="horizontal")
st.image("images.jpeg",width = 150)
deta = Deta("c0s6px57_jRsaNEKUSabNNDVzppaTy4BUHVAvxXpZ")
db = deta.Base("form")
if(selected2=="Course Outcome Survey Form"):
    st.title("Course Outcome Survey Form")
    a=st.text_input("Course code")
    b=st.text_input("Course Name")
    c=st.text_input("Year/Sem")
    genre = st.radio(
        "Faculty Has Made The Subject Interesting",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre2 = st.radio(
        "Faculty is enthusisatic about what is taught",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre3 = st.radio(
        "Faculty is good at explaining things",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre15 = st.radio(
        "The course is well organized",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre4 = st.radio(
        "The course is intellectually stimulating",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))


    genre5 = st.radio(
        "Any changes in the course or teaching have been communicated effectively",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))


    genre6 = st.radio(
        "The criteria used in assessment have been clearly stated in advance",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))


    genre7 = st.radio(
        "Assessment and marking have been fair",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))


    genre8 = st.radio(
        "I have been able to contact faculty when I needed to",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre9 = st.radio(
        "I have received detailed comments on my work",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre10 = st.radio(
        "I have received sufficient advice and support from the faculty for my studies",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre11 = st.radio(
        "I have been able to access general IT resources when I needed to",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre12 = st.radio(
        "My communication skills have improved",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))


    genre13 = st.radio(
        "Feedback on my work has been prompt",
        ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    
    genre14 = st.radio(
    "Feedback on my work has helped me clarify things I did not understand",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre15 = st.radio(
    "As a result of the course, I feel confident in tackling problems related to this course",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genre16 = st.radio(
    "Overall I am satisfied with the quality of the course",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    sug=st.text_area("Suggestions (if any)")

    if(st.button("Submit")):
        st.balloons()
        db.put({"Course code": a,"Course Name":b,"Year/Sem":c,"Faculty Has Made The Subject Interesting":genre,"Faculty is enthusisatic about what is taught":genre2,"Faculty is good at explaining things":genre3,"The course is well organized":genre15})
        st.success("Thank you, Your response has been recorded")

if(selected2=="Alumini survey form"):
    st.title("Alumini survey form")
    st.subheader("(Assessment of Outcomes)")
    #st.image("images.jpeg",width = 150)
    nm=st.text_input("Name")
    da=st.date_input("Date")
    org=st.text_input("Organization")
    add=st.text_input("Address")
    gra=st.text_input("Year of Graduation")
    ph=st.text_input("Mobile number")
    mailid=st.text_input("Enter your mail id")
    genrea = st.radio(
    "Demonstrate basic knowledge in mathematics,science, engineering, and humanities",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genreb = st.radio(
    "Define the problems and provide solutions by designing and conducting experiments, interpreting and analysing data, and reporting the results",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genrec = st.radio(
    "Demonstrate the ability to design Computer Science and Engineering systemss",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genred = st.radio(
    "Ability to participate as members of multidisciplinary design teams along with mechanical, electrical, and other engineers",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genree = st.radio(
    "Understand quantitative modelling and analysis of a broad array of systems-level techniques to identify, formulate and solve CSE problems",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genref = st.radio(
    "Broadly educated and will have an understanding of ethical responsibilities",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genreg = st.radio(
    "Proficient in English language in both communicative and technical forms",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genreh = st.radio(
    "Awareness to apply engineering solutions in Global, National, and Societal contexts",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genrei = st.radio(
    "Capable of self-education and clearly understand the value of updating their professional knowledge to engage in lifelong learning",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genrej = st.radio("Demonstrate the ability to apply advanced technologies to solve contemporary and new problems.Capable of self-education and clearly understand the value of updating their professional knowledge to engage in lifelong learning",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    genrek = st.radio(
    "Demonstrate the ability to choose and apply appropriate resource management techniques",
    ('Very satisfied', 'Generally satisfied', 'Generally dissatisfied','very dissatisfied','Not applicable'))

    if(st.button("Submit")):
        st.balloons()
        st.success("Thank you, Your response has been recorded")

if(selected2=="Guest lecture Feedback"):
    st.title("Guest lecture Feedback")
    st.subheader("((By student))")
    a= st.text_input("Topic :")
    b= st.text_input("Name of the Expert :")
    c= st.text_input("Semester :")
    d= st.text_input("Date : ")
    e= st.text_input("Register No. :")
    f= st.text_input("Academic Year")
    st.text("Overall, Your satisfaction on the following statements")

    g= st.radio("Topic relevance to my course/syllabus",('Definitely agree','Agree','Uncertain','Disagree',' Definietly disagree'))
    g1= st.radio("Topic relevance to my area of interest",('Definietly agree','Agree','Uncertain','Diasgree','Definietly Disagree'))
    g2= st.radio("Lecture challenged me intellectually ",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g3= st.radio("Lecture content was well organized",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g4= st.radio("Speaker was able to explain the topic clearly & used relevant examples",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g5= st.radio("Speaker was able to make the lecture interactive & made me feel engaged",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g6= st.radio("Speaker was able to positively influence my views",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g7= st.radio("Speaker had enough knowledge against the topic",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g8= st.radio("Speakers ability to stimulate interest in the topic",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g9= st.radio("Effective use of time during the lecture by the speaker",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g10= st.radio("Speakers answering capability when posting a question against the topic",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g11= st.radio("Communication skills",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g12= st.radio("I have learned something valuable from the lecture",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g13= st.radio("I understand the main points that the guest speaker was trying to convey against the topic",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g14= st.radio("Would you recommend the speaker to others",('Definitely agree','Agree','Uncertain','Disagree','Definietly disagree'))
    g15= st.text_input("Additional comments (if any): ")
    if(st.button("Submit")):
        st.balloons()
        st.success("Thank you your response has been submitted")
