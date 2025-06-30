from transformers import pipeline

# Load legal document
with open("legal_doc.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Due to input limits, chunk the text
max_len = 1024
chunks = [text[i:i+max_len] for i in range(0, len(text), max_len)]

# Summarize each chunk
print("\n--- SUMMARY ---\n")
for i, chunk in enumerate(chunks):
    summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
    print(f"Chunk {i+1}:\n{summary[0]['summary_text']}\n")
