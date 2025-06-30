import re

# Load the legal document
with open("legal_doc.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Define clause patterns
clause_patterns = {
    "confidentiality": r"(confidentiality.*?)(?=\n[A-Z])",
    "termination": r"(termination.*?)(?=\n[A-Z])",
    "governing_law": r"(governing law.*?)(?=\n[A-Z])"
}

# Extract clauses
def extract_clauses(text, patterns):
    results = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            results[key] = match.group(1).strip()
    return results

clauses = extract_clauses(text, clause_patterns)

# Print results
for name, content in clauses.items():
    print(f"\n--- {name.upper()} CLAUSE ---\n{content}\n")
