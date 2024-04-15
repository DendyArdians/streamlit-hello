import streamlit as st
import pandas as pd

import config
import utils

@st.cache_data
def load_df(csv_filename):
	df = pd.read_csv(csv_filename)
	df.fillna("-", inplace=True)
	# df.sort_values(by=["Produk", "Jenis", "Tags"], ascending=[True, True, True], inplace=True, ignore_index=True)
	df.sort_values(by="Produk", ascending=True, inplace=True, ignore_index=True)
	# df.drop([""], axis=1, inplace=True)
	df.set_index("Produk", inplace=True)
	return df

@st.cache_data
def filter_df(df, column, filter_list):
	df_copy = df[df[column].str.split(', ').apply(lambda x: any(i in filter_list for i in x))]
	return df_copy

## initialization ##

## set some streamlit config
st.set_page_config(
	page_title="Cari Herba",
	page_icon=":leaves:",
	layout="wide",
)

## remove streamlit header and footer
utils.st_markdown(config.markdown_hide_st_logo)

sidebar = st.sidebar

## prepare the data
df = load_df("sample_data.csv")
unique_tags = sorted(list(df["Label"].str.split(", ").explode().unique()))[1:]
herb_categories = sorted(df["Jenis"].unique())[1:]
# df["Harga"] = df["Harga"].apply(lambda x: "{:,}".format(x))

st.markdown(
	f"<h1 style='text-align: center; color: #35BC02;'>Sentra Herbal</h1>",
	unsafe_allow_html=True
)

tabs = st.tabs(("Tabel Produk", "Kontak", "Tentang"))

with tabs[0]:
	with st.form("Form1", clear_on_submit=False):
		col1, col2 = st.columns(2)
		with col1:
			picked_category = st.multiselect(
				"Jenis",
				key="picked_category",
				options=herb_categories,
			)

		with col2:
			picked_tags = st.multiselect(
				"Kegunaan",
				key="picked_tags",
				options=unique_tags,
			)

		st.write("\n")
		if st.form_submit_button("Filter Produk", use_container_width=True):
			pass

	st.divider()

	df_copy = df.copy()

	if picked_category:
		df_copy = filter_df(df_copy, "Jenis", picked_category)

	if picked_tags:
		df_copy = filter_df(df_copy, "Label", picked_tags)

	if picked_category or picked_tags:
		df_copy.sort_values(by="Jenis", ascending=True, inplace=True, ignore_index=False)
		st.dataframe(df_copy, use_container_width=True, height=350)

	else:
		st.dataframe(df, use_container_width=True, height=350)

st.divider()


with tabs[1]:
	st.divider()

	col1, col2, col3 = st.columns(3)
	with col1:
		st.write("Shopee")
		st.write("Tokopedia")
		st.write("Whatsapp")
	
	with col2:
		st.write("")

	with col3:
		st.write("Link to shopee")
		st.write("Link to tokopedia")
		st.write("wa.me/628xxxxxxxxxx")


with tabs[2]:
	st.markdown(
		f"<h1 style='text-align: center; color: green;'> Mengapa harus pilih Sentra Herbal? </h1>",
		unsafe_allow_html=True
	)

	utils.fn_add_markdown_style1(
		"Perusahaan Islami",
		"Dengan berbelanja di Sentra Herbal, kamu turut membangun perusahaan yang Islami (mewajibkan sholat fardhu berjamaah) & sehat (melarang merokok)"
	)

	utils.fn_add_markdown_style1(
		"Karyawan Muslimin",
		"Sentra Herbal diberdayakan kaum muslimin yang senantiasa dilatih untuk mengamalkan ajaran Islam, sehingga materil yang kamu berikan akan dimanfaatkan dengan lebih bijak, insyaAllah"
	)

	utils.fn_add_markdown_style1(
		"Kehalalan Produk Lebih Terjamin",
		"Setiap produk akan kami pastikan terbebas dari babi dan bahan lainnya yang diharamkan"
	)

	utils.fn_add_markdown_style1(
		"Professional",
		"Sentra Herbal merupakan perusahaan yang sudah dipercaya dan akan terus berusaha sebaik mungkin dalam memberikan pelayanan kepada setiap pelanggan"
	)

## sidebar content
sidebar.image(
	"images/sentra-herbal-logo.webp",
	# caption="Sentra Herbal",
	use_column_width=True)

sidebar.header("Ganti ke Herbal, yuk!")

sidebar.divider()
sidebar.write("""Berbagai produk herbal kami sediakan untuk kamu:
- Produk keperluan mandi (sabun, pasta gigi)
- Produk kecantikan
- Produk untuk Pasutri
- Obat-obatan
- Minuman sehari-hari (madu, susu, teh & kopi)
- Dan lainnya
""")