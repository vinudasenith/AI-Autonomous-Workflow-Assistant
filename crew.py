from crewai import Crew

from agents.planner_agent import planner_agent
from agents.research_agent import research_agent
from agents.executor_agent import executor_agent
from agents.reviewer_agent import reviewer_agent

from tasks.research_tasks import research_task
from tasks.planning_tasks import planning_task
from tasks.execution_tasks import execution_task
from tasks.review_tasks import review_task


def run_crew(user_input, input_type="text", input_data=None):

    context=""
    
    if input_type == "pdf":
        context = f"PDF Content: {input_data}"

    elif input_type == "image":
        context = f"Image analysis result: {input_data}"

    elif input_type == "web":
        context = f"Web data: {input_data}"

    else:
        context = user_input

    task_planner = planning_task(planner_agent, context)

    task_research=research_task(context)

    task_execute = execution_task(context, "Use research findings")

    task_review = review_task(context)

    
    crew = Crew(
        agents=[planner_agent,research_agent,executor_agent,reviewer_agent],
        tasks=[task_planner, task_research,task_execute, task_review],
        verbose=False
    )

    result = crew.kickoff()

    final_output = result.tasks_output[-1].raw

    return {
        "crew_output": final_output,

    }