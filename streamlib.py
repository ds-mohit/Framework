# streamlit is used to create a web application
#there is no need ofr css and html
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import time

#page configuration
st.set_page_config(

    page_title="Streamlit page configuration",
    page_icon="😂",
    layout="wide"
)

#page title
st.title('Hello world')
# 
st.header('Streamlit App')
#to write a subheader
st.subheader('Streamlit is a framwork for Machine Learning and Data Science')
# to write a text
st.write('Hello world')
#to change font style
st.markdown("<h1 style='text-align: center; color: red;'>Hello world</h1>", unsafe_allow_html=True)
# to write a markdown
st.markdown("```Hello world```")
# to write a code
st.code('print("Hello world")')
# to write a latex(formula)
st.latex(r"a^2 + b^2 = c^2")
# to create a line on page
st.divider()
# metrices and message
st.header(" Metrices and Message ")

st.metric(label="Revenue",value=1234,delta="+10%",delta_color="inverse")

st.error("This is an error message")
st.warning("This is a warning message")
st.info("This is an info message")
st.success("This is a success message")
st.exception("This is an exception message")    

st.divider()

st.header(" Data Display")
# creating data
df = pd.DataFrame(np.random.randn(10, 2), columns=['a', 'b'])
st.dataframe(df)
st.table(df)
st.json(df.to_dict())

st.divider()

st.header("Charts")
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
# st.altair_chart(df)

chart=alt.Chart(df.reset_index()).mark_line().encode(x='index',y='a')
st.altair_chart(chart,use_container_width=True)
fig, ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)

# to take data in this we use forms
with st.form("Input Form"):
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0)
    mood = st.radio("Select your mood", ["happy", "sad", "neutral"])
    languages = st.multiselect("Select your languages", ["English", "French", "Hindi"])
    
    submit = st.form_submit_button("Submit")
    
    if submit:
        st.success(
            f"Name: {name}, Age: {int(age)}, Mood: {mood}, Languages: {languages}, Submitted: {submit}"
        )

st.divider()

cal1,cal2,cal3=st.columns([6,4,2])
with cal1:
    name = st.text_input("Enter your name:")
    name
    age = st.number_input("Enter your age:", min_value=0)
with cal2:
    mood = st.radio("Select your mood", ["happy", "sad", "neutral"])
    languages = st.multiselect("Select your languages", ["English", "French", "Hindi"])
with cal3:
    title=st.title("Done")

# making forms using with via first make form then use cal
with st.form("Via col"):
    cal1,cal2=st.columns(2)
    with cal1:
        name = st.text_input("Enter your name:")
        age = st.number_input("Enter your age:", min_value=0)
    with cal2:
        mood = st.radio("Select your mood", ["happy", "sad", "neutral"])
        languages = st.multiselect("Select your languages", ["English", "French", "Hindi"])
    
    submit = st.form_submit_button("Submit")
    
    if submit:
        st.success(
            f"Name: {name}, Age: {int(age)}, Mood: {mood}, Languages: {languages}, Submitted: {submit}"
        )

cal1,cal2=st.columns(2)
with cal1:
    number=st.slider("Select a number:",0,100)
with cal2:
    color=st.color_picker("Select a color:","#ff0000")

st.text_area("Enter the txt")
st.time_input("Select the time")
st.file_uploader("Upload a file")
st.date_input("Select a date")

st.divider()

st.header("Media")

st.image(r"C:\Users\dell\Downloads\gear-5-luffy-one-piece-5k-3840x2160-16501.jpg",caption="Luffy")
st.audio(r"https://file-examples.com/wp-content/uploads/2017/11/file_example_MP3_700KB.mp3")
st.video(r"https://youtu.be/IhiKMxOxS2U?si=FYFtrfY5fbIs7lho")

st.divider()
# for making sidebar we use this with . what to show there
st.sidebar.header("Sidebar of your web app")
st.sidebar.write("Hello world")
st.sidebar.selectbox("Select a number",range(10))
st.sidebar.button("this is a button")
st.divider()

st.header("Container")
with st.container():
    st.write("this is a container")

with st.expander("Expander"):
    st.write("you can expand this")

with st.spinner("Loading  Data..."):
    time.sleep(10)
    st.success("Data Loaded")
#st.toast("Data Loaded",icon="👍")

st.write("niche link di hui hai streamlit ki")
st.page_link("http://streamlit.io",label="Streamlit Website",icon="📃")
