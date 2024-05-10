import streamlit as st
import base64

import config
import utils

## initialization ##

## set some streamlit config
st.set_page_config(
	page_title="Cari Herbal",
	page_icon=":leaves:",
	layout="wide",
)

## remove streamlit header and footer
utils.fn_st_markdown(config.markdown_hide_st_logo)

sidebar = st.sidebar

## prepare the data
df = utils.fn_load_df("sample_data.csv")
unique_tags = sorted(list(df["Label/Kategori"].str.split(", ").explode().unique()))[1:]
herb_categories = sorted(df["Varian"].unique())[1:]
# df["Harga"] = df["Harga"].apply(lambda x: "{:,}".format(x))

## the main header text
# st.markdown(
# 	f"<h1 style='text-align: center; color: #35BC02;'>Sentra Herbal</h1>",
# 	unsafe_allow_html=True
# )

## create multiple tabs for the menu
tabs = st.tabs(("Home", "Cari Herbal", "Belanja", "Tips", "About"))

with tabs[0]:
	col1, col2 = st.columns(2)
	with col1:
		st.image(
			"images/sentra-herbal-logo.webp",
			width=400,
		)
	
	with col2:
		st.header("Ganti ke Herbal, yuk!")

		# st.divider()
		st.write("""Berbagai produk herbal kami sediakan untuk kamu:
		\n- Obat-obatan
		\n- Produk kecantikan
		\n- Produk keperluan mandi (sabun, pasta gigi)
		\n- Produk untuk Pasutri
		\n- Bumbu masakan	
		\n- Minuman sehari-hari (madu, sari kurma, susu, teh & kopi)
		\n- Dan lainnya
		""")

with tabs[1]:
	with st.form("Form1", clear_on_submit=False):
		col1, col2 = st.columns(2)
		with col1:
			picked_category = st.multiselect(
				"Varian Herbal",
				key="picked_category",
				options=herb_categories,
			)

		with col2:
			picked_tags = st.multiselect(
				"Kegunaan/Kategori",
				key="picked_tags",
				options=unique_tags,
			)

		st.write("\n")
		if st.form_submit_button("Filter Produk", use_container_width=True):
			pass

	df_copy = df.copy()

	if picked_category or picked_tags:
		if picked_category:
			df_copy = utils.fn_filter_df(df_copy, "Varian", picked_category)

		if picked_tags:
			df_copy = utils.fn_filter_df(df_copy, "Label/Kategori", picked_tags)

		df_copy.sort_values(by="Varian", ascending=True, inplace=True, ignore_index=False)
		st.dataframe(df_copy, use_container_width=True, height=350)

	else:
		st.dataframe(df, use_container_width=True, height=350)

st.divider()


with tabs[2]:
	st.write("Simulasi Belanja")



with tabs[3]:
	gif_img_file1 = open("images/gif-01-filter-by-category.gif", "rb")
	gif_img_file2 = open("images/gif-02-reset-filter.gif", "rb")
	gif_img_file3 = open("images/gif-03-sort-by-column.gif", "rb")
	gif_img_file4 = open("images/gif-04-search-feature.gif", "rb")

	gif_img1 = base64.b64encode(gif_img_file1.read()).decode("utf-8")
	gif_img2 = base64.b64encode(gif_img_file2.read()).decode("utf-8")
	gif_img3 = base64.b64encode(gif_img_file3.read()).decode("utf-8")
	gif_img4 = base64.b64encode(gif_img_file4.read()).decode("utf-8")

	gif_img_file1.close()
	gif_img_file2.close()
	gif_img_file3.close()
	gif_img_file4.close()
	
	col1, col2 = st.columns(2)
	with col1:
		st.subheader(f"""Memfilter Produk""")
		st.write(f"""Untuk memfilter/menyaring, kamu bisa pilih opsi varian dan/atau kategori yang kamu inginkan.""")
	
	with col2:
		st.markdown(
			f'<img src="data:image/gif;base64,{gif_img1}" alt="cat gif">',
			unsafe_allow_html=True,
		)
	st.divider()

	col1, col2 = st.columns(2)
	with col1:
		st.subheader(f"""Mereset Filter""")
		st.write(f"""Untuk mereset filter, kamu bisa klik tombol silang pada filter yang ingin dihapus.""")

	with col2:
		st.markdown(
			f'<img src="data:image/gif;base64,{gif_img2}" alt="cat gif">',
			unsafe_allow_html=True,
		)
	st.divider()

	col1, col2 = st.columns(2)
	with col1:
		st.subheader(f"""Mengurutkan Produk""")
		st.write(f"""Klik salah satu/beberapa kolom tabel agar datanya terurut, misalnya klik kolom harga agar terurut tertinggi-terendah.""")
	
	with col2:
		st.markdown(
			f'<img src="data:image/gif;base64,{gif_img3}" alt="cat gif">',
			unsafe_allow_html=True,
		)
	st.divider()

	col1, col2 = st.columns(2)
	with col1:
		st.subheader(f"""Fitur Search""")
		st.write(f"""Klik tombol lup/magnifier, kemudian ketik keyword yang ingin kamu cari.""")
	with col2:
		st.markdown(
			f'<img src="data:image/gif;base64,{gif_img4}" alt="cat gif">',
			unsafe_allow_html=True,
		)
	st.divider()


with tabs[4]:
	st.markdown(
		f"<h1 style='text-align: center; color: #35BC02;'> Mengapa Lebih Baik Sentra Herbal? </h1>",
		unsafe_allow_html=True
	)

	utils.fn_add_markdown_style1(
		"Perusahaan Islami",
		"Dengan berbelanja di Sentra Herbal, kamu turut membangun perusahaan yang Islami (mewajibkan sholat fardhu berjamaah) & sehat (melarang merokok)."
	)

	utils.fn_add_markdown_style1(
		"Karyawan Muslimin",
		"Sentra Herbal diberdayakan kaum muslimin yang senantiasa dibimbing untuk mengamalkan ajaran Islam, sehingga materil yang kamu berikan akan dimanfaatkan dengan lebih bijak, insyaallah."
	)

	utils.fn_add_markdown_style1(
		"Kehalalan & Keaslian Produk Lebih Terjamin",
		"Setiap produk akan kami pastikan terbebas dari bahan yang diharamkan & dipastikan orginal karena didapat dari supplier resmi."
	)

	utils.fn_add_markdown_style1(
		"Professional",
		"Sentra Herbal merupakan perusahaan terpercaya dan terus berusaha memberikan pelayanan terbaik kepada setiap pelanggan."
	)

	st.divider()
	st.write("Whatsapp: wa.me/628xxxxxxxxxx")
