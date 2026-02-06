from crewai import Task
from agents.reviewer_agent import reviewer_agent

def review_task(report):
    return Task(
        description=f"Review and polish this report:\n{report}",
        agent=reviewer_agent,
        expected_output="Final polished report"
    )