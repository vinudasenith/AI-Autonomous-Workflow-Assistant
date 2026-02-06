from crewai import Crew

from agents.planner_agent import planner_agent
from agents.research_agent import research_agent, perform_research
from agents.executor_agent import executor_agent
from agents.reviewer_agent import reviewer_agent

from tasks.research_tasks import research_task
from tasks.planning_tasks import planning_task
from tasks.execution_tasks import execution_task
from tasks.review_tasks import review_task


def run_crew(user_input):
    task_planner = planning_task(planner_agent, user_input)

    task_research=research_task(user_input)

    task_execute = execution_task(user_input, "Use research findings")

    task_review = review_task(user_input)

    
    crew = Crew(
        agents=[planner_agent,research_agent,executor_agent,reviewer_agent],
        tasks=[task_planner, task_research,task_execute, task_review]
    )

    result = crew.kickoff()

    return {
        "crew_output": result,

    }