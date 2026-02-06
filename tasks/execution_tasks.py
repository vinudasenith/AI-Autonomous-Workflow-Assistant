from crewai import Task
from agents.executor_agent import executor_agent

def execution_task(step, context):
    return Task(
        description=f"Summarize findings for: {step}\nContext: {context}",
        agent=executor_agent,
        expected_output="A concise summary"
    )
