from nlp.intent_classifier import classify_intent
from crew import run_crew


user_task = input("Enter a task: ")
intent= classify_intent(user_task)
print("Detected intent:", intent)

results=run_crew(user_task)

print("\nCrew Output:")
print(results["crew_output"])

print("\nResearch Results:")
for res in results["research_results"]:
    print(f"\nStep: {res['step']}")
    for doc in res["docs"]:
        print(f"- {doc.page_content[:200]}...")
