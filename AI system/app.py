import streamlit as st
from pdfminer.high_level import extract_text as extract_pdf_text
from io import BytesIO
from clause_extractor import extract_clauses
from summarizer import summarize_text

st.set_page_config(page_title="🧠 AI Legal Document Analyzer", layout="wide")
st.title("📄 AI-Powered Legal Document Analyzer")

uploaded_file = st.file_uploader("Upload a legal document (.pdf or .txt)", type=["pdf", "txt"])

def read_text(file):
    if file.name.endswith(".pdf"):
        return extract_pdf_text(BytesIO(file.read()))
    else:
        return file.read().decode("utf-8")

if uploaded_file:
    with st.spinner("Reading and processing document..."):
        text = read_text(uploaded_file)

    st.subheader("📜 Full Document Text")
    with st.expander("Show Raw Text"):
        st.text_area("Document Content", text, height=300)

    st.subheader("📌 Key Legal Clauses")
    clauses = extract_clauses(text)
    if clauses:
        for title, content in clauses.items():
            st.markdown(f"### 🔹 {title}")
            st.write(content)
    else:
        st.warning("No clauses matched. Try a more detailed legal file.")

    st.subheader("🧠 AI Summary")
    if st.button("Summarize Document"):
        with st.spinner("Generating Summary..."):
            summary = summarize_text(text)
        st.success("Summary Complete!")
        st.text_area("Summary", summary, height=300)
