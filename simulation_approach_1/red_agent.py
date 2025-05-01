import os
import random
import json

import metadata
from config import CONFIG
from google_map_distance_api import find_blue_agents_max_turns
from agents_meet import blue_meets_noone, red_meets_noone, red_meets_blue, red_meets_red, blue_meets_red, blue_meets_blue
from get_model_response import llm_inference, string_to_json

class Red_Agent:

  def __init__(self, agent_name, agent_number, original_source):
    self.agent_name = agent_name
    self.agent_number = agent_number
    self.original_source = original_source
    self.original_destination = "NYC"
    self.current_place = original_source
    self.previous_CoT = ""
    self.red_contact = 0
    self.blue_contact = 0
    self.money_earned = 0


  def red_meets_noone(self, iteration):
    """
    A Red agent meets nobody & reacts
    """
    print("Hit")
    if(self.previous_CoT == ""):
      prompt = red_meets_noone(self.current_place, "None")
    else:
      prompt = red_meets_noone(self.current_place, self.previous_CoT)

    next_place = ""
    CoT = ""
    red_response = "None"

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

    self.previous_CoT = CoT
    metadata.ITERATION.append(iteration)
    metadata.AGENT_TYPE.append("Red")
    metadata.AGENT_NAME.append(self.agent_name)
    metadata.AGENT_NUMBER.append(self.agent_number)
    metadata.ORIGINAL_SOURCE.append(self.original_source)
    metadata.ORIGINAL_DESTINATION.append(self.original_destination)
    metadata.CURRENT_PLACE.append(self.current_place)
    metadata.NEXT_PLACE.append(next_place)

    self.current_place = next_place

    metadata.BLUE_AGENT_CoT.append("None")
    metadata.RED_AGENT_CoT.append(CoT)

    metadata.BLUE_RESPONSE_TO_RED.append("None")
    metadata.BLUE_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_RED.append("None")

    metadata.BLUE_AGENT_RESPONSE_JSON.append("None")
    metadata.RED_AGENT_RESPONSE_JSON.append(response_json)

    metadata.BLUE_AGENT_TYPE.append(0)
    metadata.RED_AGENT_TYPE.append(0)

    return self.current_place, CoT, red_response


  def blue_agent_meets_red_agent(self, blue_agent, iteration):
    """
    Red was already present there.
    Blue arrives, so red addresses blue and moves.
    """
    print("Hit")
    prompt = red_meets_blue(blue_agent.original_source, blue_agent.original_destination, blue_agent.current_place, self.current_place)
    next_place = ""
    CoT = ""
    red_response_to_blue = "None"

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
        red_response_to_blue = str(response_json["response_to_other_agent"])


    self.previous_CoT = CoT
    metadata.ITERATION.append(iteration)
    metadata.AGENT_TYPE.append("Red")
    metadata.AGENT_NAME.append(self.agent_name)
    metadata.AGENT_NUMBER.append(self.agent_number)
    metadata.ORIGINAL_SOURCE.append(self.original_source)
    metadata.ORIGINAL_DESTINATION.append(self.original_destination)
    metadata.CURRENT_PLACE.append(self.current_place)
    metadata.NEXT_PLACE.append(next_place)

    self.current_place = next_place

    metadata.BLUE_AGENT_CoT.append("None")
    metadata.RED_AGENT_CoT.append(CoT)

    metadata.BLUE_RESPONSE_TO_RED.append("None")
    metadata.BLUE_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_BLUE.append(red_response_to_blue)
    metadata.RED_RESPONSE_TO_RED.append("None")

    metadata.BLUE_AGENT_RESPONSE_JSON.append("None")
    metadata.RED_AGENT_RESPONSE_JSON.append(response_json)

    metadata.BLUE_AGENT_TYPE.append(0)
    metadata.RED_AGENT_TYPE.append(0)

    return self.current_place, CoT, red_response_to_blue


  def red_agent_meets_red_agent_first_agent(self, red_agent_1, red_agent_2, iteration):
    """
    A Red Agent meets a Red Agent & reacts
    """
    print("Hit")
    prompt = red_meets_red(red_agent_1.previous_CoT, red_agent_2.previous_CoT, red_agent_1.current_place)
    next_place = ""
    CoT = ""
    red_response_to_red = "None"

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
        red_response_to_red = str(response_json["response_to_other_agent"])


    self.previous_CoT = CoT
    metadata.ITERATION.append(iteration)
    metadata.AGENT_TYPE.append("Red")
    metadata.AGENT_NAME.append(self.agent_name)
    metadata.AGENT_NUMBER.append(self.agent_number)
    metadata.ORIGINAL_SOURCE.append(self.original_source)
    metadata.ORIGINAL_DESTINATION.append(self.original_destination)
    metadata.CURRENT_PLACE.append(self.current_place)
    metadata.NEXT_PLACE.append(next_place)

    self.current_place = next_place

    metadata.BLUE_AGENT_CoT.append("None")
    metadata.RED_AGENT_CoT.append(CoT)

    metadata.BLUE_RESPONSE_TO_RED.append("None")
    metadata.BLUE_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_BLUE.append("None")
    metadata.RED_RESPONSE_TO_RED.append(red_response_to_red)

    metadata.BLUE_AGENT_RESPONSE_JSON.append("None")
    metadata.RED_AGENT_RESPONSE_JSON.append(response_json)

    metadata.BLUE_AGENT_TYPE.append(0)
    metadata.RED_AGENT_TYPE.append(0)

    return self.current_place, CoT, red_response_to_red


  def red_agent_meets_red_agent_second_agent(self, red_agent_1, red_agent_2, iteration):
      """
      A Red Agent meets a Red Agent & reacts.
      Note how the agents are switched.
      """
      print("Hit")
      prompt = red_meets_red(red_agent_2.previous_CoT, red_agent_1.previous_CoT, red_agent_2.current_place)
      next_place = ""
      CoT = ""
      red_response_to_red = "None"

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
          red_response_to_red = str(response_json["response_to_other_agent"])

      self.previous_CoT = CoT
      metadata.ITERATION.append(iteration)
      metadata.AGENT_TYPE.append("Red")
      metadata.AGENT_NAME.append(self.agent_name)
      metadata.AGENT_NUMBER.append(self.agent_number)
      metadata.ORIGINAL_SOURCE.append(self.original_source)
      metadata.ORIGINAL_DESTINATION.append(self.original_destination)
      metadata.CURRENT_PLACE.append(self.current_place)
      metadata.NEXT_PLACE.append(next_place)

      self.current_place = next_place

      metadata.BLUE_AGENT_CoT.append("None")
      metadata.RED_AGENT_CoT.append(CoT)

      metadata.BLUE_RESPONSE_TO_RED.append("None")
      metadata.BLUE_RESPONSE_TO_BLUE.append("None")
      metadata.RED_RESPONSE_TO_BLUE.append("None")
      metadata.RED_RESPONSE_TO_RED.append(red_response_to_red)

      metadata.BLUE_AGENT_RESPONSE_JSON.append("None")
      metadata.RED_AGENT_RESPONSE_JSON.append(response_json)

      metadata.BLUE_AGENT_TYPE.append(0)
      metadata.RED_AGENT_TYPE.append(0)

      return self.current_place, CoT, red_response_to_red