from crewai import Crew
from agents.planner_agent import planner_agent
from tasks.planning_tasks import planning_task

def run_crew(user_input):
    task = planning_task(planner_agent, user_input)

    crew = Crew(
        agents=[planner_agent],
        tasks=[task]
    )

    return crew.kickoff()