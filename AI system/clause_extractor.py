import re

def extract_clauses(text):
    clause_patterns = {
        "Confidentiality": r"(confidentiality.*?)(?=\n[A-Z]|$)",
        "Termination": r"(termination.*?)(?=\n[A-Z]|$)",
        "Governing Law": r"(governing law.*?)(?=\n[A-Z]|$)"
    }

    results = {}
    for name, pattern in clause_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            results[name] = match.group(1).strip()
    return results
