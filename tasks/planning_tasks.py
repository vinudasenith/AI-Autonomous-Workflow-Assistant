from crewai import Task
from agents.planner_agent import planner_agent

def planning_task(agent,user_input):
    return Task(
        description=f"Break this into steps: {user_input}",
        agent=agent,
        expected_output="A list of clear, actionable steps.",
    )