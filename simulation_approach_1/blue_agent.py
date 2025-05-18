import os
import random
import json

import metadata
from config import CONFIG
from google_map_distance_api import find_blue_agents_max_turns
from agents_meet import blue_meets_noone, red_meets_noone, red_meets_blue, red_meets_red, blue_meets_red, blue_meets_blue
from get_model_response import llm_inference, string_to_json


def change_string(place, CoT, response):
  """
  This function is used to change the string to lower case
  """
  place = place.lower().strip()
  CoT = CoT.lower().strip()
  response = response.lower().strip()

  return place, CoT, response

class Blue_Agent:

  def __init__(self, agent_name, agent_number, original_source, original_destination):
    self.agent_name = agent_name
    self.agent_number = agent_number
    self.original_source = original_source
    self.original_destination = original_destination
    self.current_place = original_source
    self.previous_CoT = ""
    self.max_turns = find_blue_agents_max_turns(original_source, original_destination)
    self.red_contact = 0
    self.blue_contact = 0
    self.averted = 0
    self.not_averted = 0

  def blue_meets_noone(self, iteration):
    """
    A Blue agent meets nobody & reacts
    """
    print("Hit")
    prompt = blue_meets_noone(self.original_source, self.original_destination, self.current_place)

    next_place = ""
    CoT = ""
    blue_response = "None"

    response = llm_inference(prompt)
    if(response == None):
      next_place = self.current_place
      CoT = "None"

    else:
      response_json = string_to_json(response)

      if(response_json == None):
        next_place = self.current_place
        CoT = "None"
      else:
        next_place = str(response_json["next_place"])
        CoT = str(response_json["CoT"])
        
    next_place, CoT, blue_response = change_string(next_place, CoT, blue_response)

    self.previous_CoT = CoT
    metadata.ITERATION.append(iteration)
    metadata.AGENT_TYPE.append("Blue")
    metadata.AGENT_NAME.append(self.agent_name)
    metadata.AGENT_NUMBER.append(self.agent_number)
    metadata.ORIGINAL_SOURCE.append(self.original_source)
    metadata.ORIGINAL_DESTINATION.append(self.original_destination)
    metadata.CURRENT_PLACE.append(self.current_place)
    metadata.NEXT_PLACE.append(next_place)

    self.current_place = next_place

    metadata.BLUE_AGENT_CoT.append(CoT)
    metadata.RED_AGENT_CoT.append("None")

    metadata.BLUE_RESPONSE_TO_RED.append("None")
    metadata.BLUE_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_RED.append("None")

    metadata.BLUE_AGENT_RESPONSE_JSON.append(response_json)
    metadata.RED_AGENT_RESPONSE_JSON.append("None")

    metadata.BLUE_AGENT_TYPE.append(0)
    metadata.RED_AGENT_TYPE.append(0)

    return self.current_place, CoT, blue_response


  def blue_agent_meets_red_agent(self, red_agent_response_to_blue, iteration):
    """
    This is when Red has already moved on, so Blue moves by pondering on Red's response.
    """
    print("Hit")
    prompt = blue_meets_red(self.original_source, self.original_destination, self.current_place, red_agent_response_to_blue)
    next_place = ""
    CoT = ""
    blue_response_to_red = "None"

    response = llm_inference(prompt)
    if(response == None):
      next_place = self.current_place
      CoT = "None"

    else:
      response_json = string_to_json(response)

      if(response_json == None):
        next_place = self.current_place
        CoT = "None"
      else:
        next_place = str(response_json["next_place"])
        CoT = str(response_json["CoT"])
        blue_response_to_red = str(response_json["response_to_other_agent"])
        
    next_place, CoT, blue_response_to_red = change_string(next_place, CoT, blue_response_to_red)

    # print("Blue")
    print(response_json)

    self.previous_CoT = CoT
    metadata.ITERATION.append(iteration)
    metadata.AGENT_TYPE.append("Blue")
    metadata.AGENT_NAME.append(self.agent_name)
    metadata.AGENT_NUMBER.append(self.agent_number)
    metadata.ORIGINAL_SOURCE.append(self.original_source)
    metadata.ORIGINAL_DESTINATION.append(self.original_destination)
    metadata.CURRENT_PLACE.append(self.current_place)
    metadata.NEXT_PLACE.append(next_place)

    self.current_place = next_place

    metadata.BLUE_AGENT_CoT.append(CoT)
    metadata.RED_AGENT_CoT.append("None")

    metadata.BLUE_RESPONSE_TO_RED.append(blue_response_to_red)
    metadata.BLUE_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_RED.append("None")

    metadata.BLUE_AGENT_RESPONSE_JSON.append(response_json)
    metadata.RED_AGENT_RESPONSE_JSON.append("None")

    metadata.BLUE_AGENT_TYPE.append(0)
    metadata.RED_AGENT_TYPE.append(0)

    return self.current_place, CoT, blue_response_to_red


  def blue_agent_meets_blue_agent_first_agent(self, blue_agent_1, blue_agent_2, iteration):
    """
    Blue_a was already present there.
    Blue_b arrives, so Blue_a addresses Blue_b and moves.
    Blue_b stays put (for now).
    """
    print("Hit")
    prompt = blue_meets_blue(blue_agent_1.original_source, blue_agent_1.original_destination, blue_agent_1.current_place, blue_agent_1.previous_CoT, blue_agent_2.original_source, blue_agent_2.original_destination, blue_agent_2.current_place, "")
    next_place = ""
    CoT = ""
    blue_response_to_blue = "None"

    response = llm_inference(prompt)
    if(response == None):
      next_place = self.current_place
      CoT = "None"

    else:
      response_json = string_to_json(response)

      if(response_json == None):
        next_place = self.current_place
        CoT = "None"
      else:
        next_place = str(response_json["next_place"])
        CoT = str(response_json["CoT"])
        blue_response_to_blue = str(response_json["response_to_other_agent"])
        
    next_place, CoT, blue_response_to_blue = change_string(next_place, CoT, blue_response_to_blue)

    self.previous_CoT = CoT
    metadata.ITERATION.append(iteration)
    metadata.AGENT_TYPE.append("Blue")
    metadata.AGENT_NAME.append(self.agent_name)
    metadata.AGENT_NUMBER.append(self.agent_number)
    metadata.ORIGINAL_SOURCE.append(self.original_source)
    metadata.ORIGINAL_DESTINATION.append(self.original_destination)
    metadata.CURRENT_PLACE.append(self.current_place)
    metadata.NEXT_PLACE.append(next_place)

    self.current_place = next_place

    metadata.BLUE_AGENT_CoT.append(CoT)
    metadata.RED_AGENT_CoT.append("None")

    metadata.BLUE_RESPONSE_TO_RED.append("None")
    metadata.BLUE_RESPONSE_TO_BLUE.append(blue_response_to_blue)
    metadata.RED_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_RED.append("None")

    metadata.BLUE_AGENT_RESPONSE_JSON.append(response_json)
    metadata.RED_AGENT_RESPONSE_JSON.append("None")

    metadata.BLUE_AGENT_TYPE.append(0)
    metadata.RED_AGENT_TYPE.append(0)

    return self.current_place, CoT, blue_response_to_blue


  def blue_agent_meets_blue_agent_second_agent(self, blue_agent_1, blue_agent_2, iteration):
    """
    This is when Blue_a has already moved on, so Blue_b moves by pondering on Blue_a's response.
    Note the agents have switched.
    """
    print("Hit")
    prompt = blue_meets_blue(blue_agent_2.original_source, blue_agent_2.original_destination, blue_agent_2.current_place, blue_agent_2.previous_CoT, blue_agent_1.original_source, blue_agent_1.original_destination, blue_agent_1.current_place, metadata.BLUE_RESPONSE_TO_BLUE[-1])
    next_place = ""
    CoT = ""
    blue_response_to_blue = "None"

    response = llm_inference(prompt)
    if(response == None):
      next_place = self.current_place
      CoT = "None"

    else:
      response_json = string_to_json(response)

      if(response_json == None):
        next_place = self.current_place
        CoT = "None"
      else:
        next_place = str(response_json["next_place"])
        CoT = str(response_json["CoT"])
        blue_response_to_blue = str(response_json["response_to_other_agent"])

    next_place, CoT, blue_response_to_blue = change_string(next_place, CoT, blue_response_to_blue)

    self.previous_CoT = CoT
    metadata.ITERATION.append(iteration)
    metadata.AGENT_TYPE.append("Blue")
    metadata.AGENT_NAME.append(self.agent_name)
    metadata.AGENT_NUMBER.append(self.agent_number)
    metadata.ORIGINAL_SOURCE.append(self.original_source)
    metadata.ORIGINAL_DESTINATION.append(self.original_destination)
    metadata.CURRENT_PLACE.append(self.current_place)
    metadata.NEXT_PLACE.append(next_place)

    self.current_place = next_place

    metadata.BLUE_AGENT_CoT.append(CoT)
    metadata.RED_AGENT_CoT.append("None")

    metadata.BLUE_RESPONSE_TO_RED.append("None")
    metadata.BLUE_RESPONSE_TO_BLUE.append(blue_response_to_blue)
    metadata.RED_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_RED.append("None")

    metadata.BLUE_AGENT_RESPONSE_JSON.append(response_json)
    metadata.RED_AGENT_RESPONSE_JSON.append("None")

    metadata.BLUE_AGENT_TYPE.append(0)
    metadata.RED_AGENT_TYPE.append(0)

    return self.current_place, CoT, blue_response_to_blue