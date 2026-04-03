from crewai import Agent

research_agent=Agent(
    role="Research Specialist",
    goal="Retrieve and summarize relevant information for each task step",\
    backstory="Expert researcher and summarizer"
)
