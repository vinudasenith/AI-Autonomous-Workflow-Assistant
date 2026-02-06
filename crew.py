from crewai import Crew
from agents.planner_agent import planner_agent
from tasks.planning_tasks import planning_task
from agents.research_agent import research_agent, perform_research
from tasks.research_tasks import research_task


def run_crew(user_input):
    task_planner = planning_task(planner_agent, user_input)

    planner_steps=task_planner.description.split("\n")

    research_results=perform_research(planner_steps)

    task_research=research_task(planner_steps)

    crew = Crew(
        agents=[planner_agent,research_agent],
        tasks=[task_planner, task_research]
    )

    crew_output = crew.kickoff()

    return {
        "crew_output": crew_output,
        "research_results": research_results,
        "planner_steps": planner_steps
    }