from crewai import Agent
from memory.vector_store import search

research_agent=Agent(
    role="Research Specialist",
    goal="Retrieve and summarize relevant information for each task step",\
    backstory="Expert researcher and summarizer"
)

def perform_research(task_steps):
    results=[]
    for step in task_steps:
        relevant_docs = search(step, k=3) 
        results.append({
            "step": step,
            "docs": relevant_docs
        })
    return results
