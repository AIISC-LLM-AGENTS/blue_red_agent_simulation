import os
import random

from config import CONFIG
from blue_agent import Blue_Agent
from red_agent import Red_Agent


model_name = CONFIG["MODEL_NAME"]
locations = CONFIG["NYC_LOCATIONS"]


def check_blue_contact_with_red_agent(blue_agent, RED_AGENTS):

  for agent in RED_AGENTS:
    if agent.current_place == blue_agent.current_place:
      blue_agent.red_contact += 1
      agent.blue_contact += 1
      return agent

  return None


def check_blue_contact_with_blue_agent(blue_agent, BLUE_AGENTS):

  for agent in BLUE_AGENTS:
    if agent == blue_agent:
      continue

    if agent.current_place == blue_agent.current_place:
      blue_agent.blue_contact += 1
      agent.blue_contact += 1
      return agent

  return None


def check_red_contact_with_blue_agent(red_agent, BLUE_AGENTS):

  for agent in BLUE_AGENTS:
    if agent.current_place == red_agent.current_place:
      red_agent.blue_contact += 1
      agent.red_contact += 1
      return agent

  return None


def check_red_contact_with_red_agent(red_agent, RED_AGENTS):

  for agent in RED_AGENTS:
    if agent == red_agent:
      continue

    if agent.current_place == red_agent.current_place:
      red_agent.red_contact += 1
      agent.red_contact += 1
      return agent

  return None


def initialize_blue_agents(num_blue_agents = CONFIG["NUM_BLUE_AGENTS"]):
  blue_agents = []

  for i in range(num_blue_agents):
    start = random.choice(range(0, CONFIG["NUM_PLACES"]))
    end = random.choice([i for i in range(0, CONFIG["NUM_PLACES"]) if i != start])
    blue_agent = Blue_Agent(model_name, i+1, locations[start], locations[end])
    blue_agents.append(blue_agent)

  return blue_agents


def initialize_red_agents(num_red_agents = CONFIG["NUM_BLUE_AGENTS"]):
  red_agents = []

  for i in range(num_red_agents):
    start = random.choice(range(0, CONFIG["NUM_PLACES"]))
    end = random.choice([i for i in range(0, CONFIG["NUM_PLACES"]) if i != start])
    red_agent = Red_Agent(model_name, i+1, locations[start], locations[end])
    red_agents.append(red_agent)

  return red_agents


def agents_status(BLUE_AGENTS, RED_AGENTS):

  # print("Blue Agents:")
  for blue in BLUE_AGENTS:
    print("Blue Agent number: ", blue.agent_number)
    print("original source = ", blue.original_source)
    print("original destination = ", blue.original_destination)
    print("current_place = ", blue.current_place)
    print("averted = ", blue.averted)
    print("blue_contact = ", blue.blue_contact)
    print("red_contact = ", blue.red_contact)
    print("turns left = ", blue.max_turns)
    print("--------------------------XXX-----------------------")

  # print("Red Agents:")
  for red in RED_AGENTS:
    print("Red Agent:")
    print("current_place = ", red.current_place)
    print("blue_contact = ", red.blue_contact)
    print("red_contact = ", red.red_contact)
    print("money_earned = ", red.money_earned)
    print("--------------------------XXX-----------------------")