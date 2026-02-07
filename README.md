# AI-Autonomous-Workflow-Assistant

![AI Workflow Assistant_page-0001](https://github.com/user-attachments/assets/759d17a6-f3fe-4b97-869d-ca0b9abacf44)

## Overview

🚀 **AI-Autonomous-Workflow-Assistant** is an AI-powered multi-agent system designed to automate complex tasks through intelligent collaboration. Built in Python with a Streamlit interface, it leverages specialized AI agents to plan, research, execute, and review user-provided tasks. This project showcases skills in agent-based AI design, natural language processing (NLP), document handling, and workflow orchestration, making it ideal for real-world enterprise automation.

Users can upload files (PDF, Word, CSV), provide URLs or APIs, and input natural language tasks to receive structured, AI-generated outputs.

---

## Features

✅ Multi-agent architecture with Planner, Researcher, Executor, and Reviewer agents  
✅ NLP-based intent classification for task understanding  
✅ File processing support for PDF, DOCX, and CSV  
✅ Web scraping for data gathering  
✅ Vector memory store for contextual recall and efficiency  
✅ Intuitive Streamlit web interface  
✅ Modular design for scalability and easy integration  
✅ Demonstrates real-world AI workflow automation

---

## Architecture

🧠 The system employs a collaborative multi-agent pipeline:

1. **Planner Agent**: Decomposes user tasks into actionable steps
2. **Research Agent**: Collects data from uploaded files, web sources, or APIs
3. **Executor Agent**: Performs the core actions based on the plan
4. **Reviewer Agent**: Validates outputs, refines results, and ensures quality

This architecture mimics advanced AI orchestration in modern systems, promoting modularity and reliability.

---

## Tech Stack

- **Core Language**: Python
- **Frontend**: Streamlit
- **AI & NLP**: NLP-based intent classification and agent logic
- **Memory**: Vector store for contextual data management
- **Data Processing**: PyPDF2 (PDF), python-docx (Word), pandas (CSV)
- **Web Tools**: BeautifulSoup for scraping

---

## Folder Structure

```
AI-Autonomous-Workflow-Assistant/
│
├── agents/
│   ├── __init__.py
│   ├── planner_agent.py
│   ├── research_agent.py
│   ├── executor_agent.py
│   └── reviewer_agent.py
│
├── tasks/
│   ├── __init__.py
│   ├── planning_tasks.py
│   ├── research_tasks.py
│   ├── execution_tasks.py
│   └── review_tasks.py
│
├── tools/
│   ├── __init__.py
│   ├── file_reader.py
│   ├── image_processor.py
│   └── web_scraper.py
│
├── memory/
│   ├── __init__.py
│   └── vector_store.py
│
├── nlp/
│   ├── __init__.py
│   └── intent_classifier.py
│
├── app.py
├── crew.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

```

---

## Installation

⚙️ To set up the project:

### 1. Clone the repository

```bash
git clone https://github.com/vinudasenith/AI-Autonomous-Workflow-Assistant.git
```

### 2. Navigate to the directory

```bash
cd AI-Autonomous-Workflow-Assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

▶️ Launch the Streamlit app:

```bash
streamlit run app.py
```

### Steps:
1. Enter a natural language task
2. Upload files or provide URLs/APIs
3. Click **"Run Workflow"** to generate results

---

## Example Use Cases

- 📊 **Data Analysis**: Upload CSV files and ask for insights, visualizations, or summaries
- 📝 **Document Processing**: Extract and summarize information from PDFs or Word documents
- 🔍 **Research Automation**: Provide a topic and let the agents gather, analyze, and compile research
- 🤖 **Workflow Automation**: Define complex multi-step tasks and let AI handle execution

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or suggestions, feel free to reach out:

- **Email**: ha.vinudas@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/vinudasenith/
