from src.parser import read_pdf, read_docx, read_txt
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Privacy Copilot",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Privacy Copilot")
st.subheader("AI 기반 개인정보처리방침 분석")

uploaded_file = st.file_uploader(
    "개인정보처리방침 파일을 업로드하세요.",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:
    st.success("파일 업로드 완료!")

    st.write("### 파일 정보")
    st.write(f"파일명 : {uploaded_file.name}")
    st.write(f"파일형식 : {Path(uploaded_file.name).suffix}")
    st.write(f"크기 : {uploaded_file.size:,} bytes")
    
    suffix = Path(uploaded_file.name).suffix.lower()

    if suffix == ".pdf":
        text = read_pdf(uploaded_file)

    elif suffix == ".docx":
        text = read_docx(uploaded_file)

    elif suffix == ".txt":
        text = read_txt(uploaded_file)

    else:
        text = "지원하지 않는 파일 형식입니다."

    st.divider()

    st.subheader("문서 내용")

    st.text_area(
        "추출된 텍스트",
        text,
        height=350
    )