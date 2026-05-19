import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#4285F4"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F8F9FA"
textColor="#202124"
font="sans serif"
""", language="toml")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)