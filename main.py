import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.png",width=600)

with col2:
    st.title("Pat McClard")
    content = """
    Hi, I'm Pat!  I am a Python programmer with over 25 years of experience in the business world managing clients
    and projects in the BPO space.  I started programming when I was 13 years old and have maintained my interest
    in technology and programming since that time.  I recently decided it was time to turn that hobby into my
    profession and chose Python as the language to focus on first.  I believe that my extensive experience managing
    clients and projects gives me a unique perspective as a programmer.   This site includes 20 projects that I have 
    coded myself to show the breadth of my programming skills.
    """
    st.info(content)
