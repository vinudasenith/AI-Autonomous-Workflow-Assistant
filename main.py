from nlp.intent_classifier import classify_intent

task = input("Enter a task: ")
print(classify_intent(task))
