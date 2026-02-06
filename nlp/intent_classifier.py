import spacy

nlp=spacy.load("en_core_web_sm")

def classify_intent(text: str) -> str:
    text=text.lower()

    if any(word in text for word in ["research", "find","search"]):
        return "research"
    elif any(word in text for word in ["summarize", "summary"]):
        return "summarize"
    elif any(word in text for word in ["analyze", "analysis"]):
        return "analyze"
    elif any(word in text for word in ["automate", "automation"]):
        return "automation"
    else:
        return "general"

