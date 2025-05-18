import os
import json

from config import CONFIG
from llama_index.llms.groq import Groq

os.environ["GROQ_API_KEY"] = CONFIG["GROQ_API_KEY"]
os.environ["GOOGLE_MAPS_API_KEY"] = CONFIG["GOOGLE_MAPS_API_KEY"]
os.environ["OPENAI_API_KEY"] = CONFIG["GROQ_API_KEY"]

def get_json_string(text):
  
  if text == None:
    return None
  
  start = text.rfind("{")
  if start == -1:
    return None
  
  end = text.rfind("}")
  if end == -1:
    return None
  
  required_text = text[start:end+1]
  return required_text


def string_to_json(text):
  
  json_string = get_json_string(text)
  if(json_string == None):
    return None
  
  print(json_string)
  
  return json.loads(json_string)


def validate_response(text):

  start = text.rfind("{")
  if start == -1:
    return None

  end = text.rfind("}")
  if end == -1:
    return None

  text = text[start:end+1]

  data = json.loads(text)

  if all(key in data for key in ["CoT", "next_place", "response_to_other_agent"]):
    print("Validated!")
    return True
  else:
    return False


def llm_inference(prompt):

  count = 0
  llm = Groq(model=CONFIG["MODEL_NAME"], api_key=CONFIG["GROQ_API_KEY"])

  while(count < 3):

    text = llm.complete(prompt).text
    if(validate_response(text)):
      return text

    count += 1

  return ""

