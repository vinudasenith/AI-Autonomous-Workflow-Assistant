from crewai import Task
from agents.executor_agent import executor_agent
from tools.file_reader import read_pdf, read_word, read_csv
from tools.image_processor import extract_text_from_image
from tools.web_scraper import fetch_web_text, fetch_api_data

def execution_task(step, context,input_type="text",input_data=None):

    if input_type=="pdf":
        content=read_pdf(input_data)
    elif input_type=="word":
        content=read_word(input_data)
    elif input_type=="csv":
        content=read_csv(input_data)
    elif input_type=="image":
        content=extract_text_from_image(input_data)
    elif input_type=="web":
        content=fetch_web_text(input_data)
    elif input_type=="api":
        content=fetch_api_data(input_data)
    else:
        content=context
    return Task(
        description=f"Summarize findings for: {step}\nContext: {content}",
        agent=executor_agent,
        expected_output="A concise summary"
    )
