import streamlit as st
import pandas as pd

def fn_st_markdown(markdown_script: str):
	return st.markdown(f"<style>{markdown_script}</style>", unsafe_allow_html=True)

def fn_add_markdown_style1(text1: str, text2: str):	
	return st.markdown(
		f"""<h2 style='text-align: left; color: #FF6600; font-size: 25px; font-weight: bold'>
<br>{text1}</h2>
{text2}
""",
		unsafe_allow_html=True
	)


@st.cache_data
def fn_load_df(csv_filename):
	df = pd.read_csv(csv_filename)
	df.fillna("-", inplace=True)
	# df.sort_values(by=["Produk", "Jenis", "Tags"], ascending=[True, True, True], inplace=True, ignore_index=True)
	df.sort_values(by="Produk", ascending=True, inplace=True, ignore_index=True)
	# df.drop([""], axis=1, inplace=True)
	df.set_index("Produk", inplace=True)
	return df


@st.cache_data
def fn_filter_df(df, column, filter_list):
	df_copy = df[df[column].str.split(', ').apply(lambda x: any(i in filter_list for i in x))]
	return df_copy