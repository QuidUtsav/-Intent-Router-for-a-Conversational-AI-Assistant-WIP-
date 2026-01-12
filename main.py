#Importing Necessary Libraries
import random
from transformers import pipeline


model = pipeline(
    task="zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)
label =["social conversation","factual information lookup"]
chat_content = ["hi","hello","thanks","thank you"]
search_content = ["who", "what", "when", "where", "how does","tell me about"]
SOCIAL_ACT_PATTERNS = {
  "GREETING": ["hi", "hello", "hey"],
  "GRATITUDE": ["thank", "thanks"],
  "PERMISSION_REQUEST": ["can i ask", "may i ask"],
  "WELLBEING_QUERY": ["how are you", "how do you feel"],
}
SOCIAL_ACT_RESPONSES = {
  "GREETING": [
      "Hey 🙂 What can I help you with?",
      "Hi there! How can I assist?"
  ],
  "GRATITUDE": [
      "You're welcome!",
      "Glad I could help 🙂"
  ],
  "PERMISSION_REQUEST": [
      "Of course. Go ahead.",
      "Sure, what do you want to ask?"
  ],
  "WELLBEING_QUERY": [
      "I'm doing well — how can I help you today?",
      "I'm just here to help you 🙂"
  ]
}

def route_intent(text):
  result=model(text,label)

  top_labels,top_scores=result["labels"],result["scores"]
  if(any(x in text for x in chat_content)):
    final_decision = "social conversation"
  elif(any(x in text for x in search_content)):
    final_decision = "factual information lookup"
  else:
    if(top_scores[0]<=.55):
      final_decision = "factual information lookup"
    else:
      final_decision = top_labels[0]

  return final_decision

def handle_social_conversation(text):
  for key,value in SOCIAL_ACT_PATTERNS.items():
    if any(x in text for x in value):
      return key
  return None



def handle_factual_information_lookup(text):
  print("Let me look that up for you.")
  return "(Search results will appear here)"

while(True):
  text=input("what do you have in mind today? ")
  text=text.lower()
  intent = route_intent(text)
  print(f"{intent}")

  if intent =="social conversation":
    social_act = handle_social_conversation(text)
    if social_act:
      return_text = random.choice(SOCIAL_ACT_RESPONSES[social_act])
    else:
      return_text = random.choice(SOCIAL_ACT_RESPONSES["GREETING"])
    print(f"{return_text}")
  else:
    return_text = handle_factual_information_lookup(text)
    print(f"{return_text}")
  print("press 1 to exit")
  if(input()=="1"):
    break
