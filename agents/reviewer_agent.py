from crewai import Agent

reviewer_agent = Agent(
    role="Reviewer Agent",
    goal="Review and polish the final report for clarity and completeness",
    backstory="Expert editor and quality checker"
)