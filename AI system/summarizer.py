from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")


def summarize_text(text):
    max_len = 1024
    chunks = [text[i:i+max_len] for i in range(0, len(text), max_len)]
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return "\n\n".join(summaries)
