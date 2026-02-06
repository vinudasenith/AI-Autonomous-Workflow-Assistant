from nlp.intent_classifier import classify_intent

task = input("Enter a task: ")
intent= classify_intent(task)

print("Detected intent:", intent)
