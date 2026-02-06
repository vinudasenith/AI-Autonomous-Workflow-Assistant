from crewai import Agent

planner_agent=Agent(
    role="Task Planner",
    goal="Break tasks into clear steps",
    backstory="Expert in planning and strategy"
)