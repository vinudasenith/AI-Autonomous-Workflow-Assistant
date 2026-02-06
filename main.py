from nlp.intent_classifier import classify_intent
from crew import run_crew


user_task = input("Enter a task: ")
intent= classify_intent(user_task)
print("Detected intent:", intent)

results=run_crew(user_task)

print("\nFinal Polished Report:")
print(results["crew_output"])