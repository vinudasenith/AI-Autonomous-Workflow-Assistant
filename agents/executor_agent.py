from crewai import Agent

executor_agent=Agent(
    role="Executor Agent",
    goal="Summarize research results and generate actionable outputs",
    backstory="Expert in compiling research into structured reports"
)