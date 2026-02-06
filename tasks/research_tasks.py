from crewai import Task
from agents.research_agent import research_agent

def research_task(task_steps):
    return Task(
        description=f"Research and summarize the following steps: {task_steps}",
        agent=research_agent,
        expected_output="Relevant info retrieved and summarized"
    )