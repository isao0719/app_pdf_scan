import streamlit as st
from pdfminer.high_level import extract_text
import mojimoji

uploaded_file = st.file_uploader(
    "Choose PDF file", type="pdf", accept_multiple_files=False
)  # 場所を作る
# uploaded_file = "C:/Users/point/project/pdfscan/data/アムロジン錠２．５ｍｇ_3.pdf"
text = extract_text(uploaded_file)
text_split = text.split("\n")
pdf_text = []
for t in text_split:
    if len(t) >= 1:
        t = mojimoji.zen_to_han(t, kana=False).replace(" ", "")  # tに入れなおす
        pdf_text.append(t)


phama_name = []
kounou = []

for i in range(len(pdf_text)):
    if "販売名" in pdf_text[i]:
        phama_name.append(pdf_text[i + 1])
    if "○" in pdf_text[i]:
        kounou.append(pdf_text[i].replace("○", ""))

phama_name = list(set(phama_name))

# 1-"".join(phama_name)
phama_name_result = ",".join(phama_name)
kounou_result = ",".join(kounou)
st.write(f"薬剤名:{phama_name_result}")
st.write(f"効能:{kounou_result}")
