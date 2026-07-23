from src.ai_analyzer import analyze_with_ai
from src.analyzer import analyze
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

       # ===== 새 문서 업로드 시 AI 결과 초기화 =====
    if st.session_state.get("last_file") != uploaded_file.name:
        st.session_state.last_file = uploaded_file.name
        st.session_state.pop("ai_result", None)
 
    suffix = Path(uploaded_file.name).suffix.lower()

    if suffix == ".pdf":
        text = read_pdf(uploaded_file)

    elif suffix == ".docx":
        text = read_docx(uploaded_file)

    elif suffix == ".txt":
        text = read_txt(uploaded_file)
        st.write("=== 디버그 ===")
        st.code(repr(text[:100]))

    else:
        text = "지원하지 않는 파일 형식입니다."

    st.divider()

    st.subheader("문서 내용")

    st.text_area(
        "추출된 텍스트",
        text,
        height=350
    )

    result = analyze(text)

    total = len(result)
    passed = sum(result.values())
    score = int((passed / total) * 100)

    st.subheader("분석 결과")



    for item, ok in result.items():
        if ok:
            st.success(f"{item} : 확인")
        else:
            st.error(f"{item} : 없음")

    
    st.divider()

    st.metric(
    label="개인정보처리방침 기본 점수",
    value=f"{score}점"
    )

    st.divider()

# ==========================
# AI 분석
# ==========================
    st.subheader("🤖 AI 분석")

    if st.button("🤖 AI 분석 실행"):
        with st.spinner("AI가 개인정보처리방침을 분석하는 중입니다..."):
            st.session_state.ai_result = analyze_with_ai(text)

# AI 분석 결과가 있으면 출력
    if "ai_result" in st.session_state:

        ai_result = st.session_state.ai_result

        st.markdown(ai_result)

        st.download_button(
            label="📥 AI 분석 결과 저장",
            data=ai_result,
            file_name="privacy_analysis.md",
            mime="text/markdown",
       )