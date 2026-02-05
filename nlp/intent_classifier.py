import spacy

nlp=spacy.load("en_core_web_sm")

def classify_intent(text):
    text=text.lower()

    if "research" in text or "find" in text:
        return "research"
    elif "summarize" in text:
        return "summarize"
    elif "analyze" in text:
        return "analyze"
    elif "automate" in text:
        return "automation"
    else:
        return "general"

