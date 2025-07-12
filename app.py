import streamlit as st

st.write("Hello, *World!* :sunglasses:")
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.markdown("*Streamlit* is **really** ***cool***.")


st.metric(label="Temperature", value="70 °F")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
