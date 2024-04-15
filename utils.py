import streamlit as st

def st_markdown(markdown_script: str):
	return st.markdown(f"<style>{markdown_script}</style>", unsafe_allow_html=True)

def fn_add_markdown_style1(text1: str, text2: str):	
	return st.markdown(
		f"""<h2 style='text-align: left; color: #FF6600; font-size: 25px; font-weight: bold'>
<br>{text1}</h2>
{text2}
""",
		unsafe_allow_html=True
	)