import pandas as pd
from PyPDF2 import PdfReader
import docx

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def read_word(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string(index=False)