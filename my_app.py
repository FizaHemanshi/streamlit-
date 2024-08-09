import streamlit as st

st.write("Hello world :getting bore, hello brother")
st.title("Display title use st.title()")
st.write("To write text use st.write()")
st.header("I am header to write header use st.header()")
st.subheader("I am subheader to write subheader use st.subheader()")
st.text("Hey I am simple text to write simple text use st .text")
# To create hyperlink
st.markdown("[streamlit](https://streamlit.io/)")
st.markdown("[Streamlit CheatSheet](https://cheat-sheet.streamlit.io/)")
st.success("Success!")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error!")

from PIL import Image
img = Image.open("smj.jpg")
st.image(img, width=300, caption="Satyamev Jayate")