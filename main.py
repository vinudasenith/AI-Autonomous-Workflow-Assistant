from nlp.intent_classifier import classify_intent
from crew import run_crew
from tasks.planning_tasks import planning_task

user_task = input("Enter a task: ")
intent= classify_intent(user_task)
print("Detected intent:", intent)

crew_output = run_crew(user_task)

print("\nCrew Output:")
print(crew_output)
