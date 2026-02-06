from crewai import Task

def planning_task(agent,user_input):
    return Task(
        description=f"Break this into steps: {user_input}",
        agent=agent
    )