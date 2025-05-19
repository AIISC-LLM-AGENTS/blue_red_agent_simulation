import os
import random
import json

import metadata
from config import CONFIG
from blue_agent import Blue_Agent
from red_agent import Red_Agent
from locations import NYC_LOCATIONS, BILLBOARD_LOCATIONS
from utils import check_blue_contact_with_red_agent, check_blue_contact_with_blue_agent
from utils import check_red_contact_with_blue_agent, check_red_contact_with_red_agent
from utils import initialize_blue_agents, initialize_red_agents
from google_map_distance_api import find_blue_agents_max_turns
from get_model_response import llm_inference
from agents_meet import blue_meets_noone, red_meets_noone, red_meets_blue, red_meets_red, blue_meets_red, blue_meets_blue


def simulate(BLUE_AGENTS, RED_AGENTS, num_blue_agents: int, num_red_agents: int):

  iteration = 0

  for i in range(num_blue_agents):
    metadata.BLUE_AGENTS_STATUS.append(False)

  print(len(metadata.BLUE_AGENTS_STATUS))

  while False in metadata.BLUE_AGENTS_STATUS:

            iteration += 1
            print("Iteration = ", iteration)

            ## Updating every Blue agent
            for i in range(num_blue_agents):

                if metadata.BLUE_AGENTS_STATUS[i] == True:
                    continue

                blue_agent = BLUE_AGENTS[i]

                blue_source = blue_agent.original_source
                blue_destination = blue_agent.original_destination
                blue_current_place = blue_agent.current_place
                blue_turns_left = blue_agent.max_turns

                print(f"Turns left for Blue agent {i+1} is {blue_turns_left}")

                ## Bingo! =)
                if(blue_current_place == blue_destination):
                    print(f"Homerun for Blue Agent {i+1}")
                    if(blue_agent.red_contact == True):
                        metadata.BLUE_AGENT_TYPE.append(3)
                    else:
                        metadata.BLUE_AGENT_TYPE.append(1)

                    metadata.RED_AGENT_TYPE.append("None")
                    metadata.BLUE_AGENTS_STATUS[i] = True

                    continue


                ## Blue is done for :-/
                if(blue_turns_left <= 0):
                    if(blue_agent.red_contact):
                        metadata.BLUE_AGENT_TYPE.append(4)
                    else:
                        metadata.BLUE_AGENT_TYPE.append(2)

                    metadata.RED_AGENT_TYPE.append("None")
                    metadata.BLUE_AGENTS_STATUS[i] = True

                    continue


                """
                Either
                - blue agent meets a red agent:
                    - first red responds to blue and moves
                    - blue ponders and then moves
                or
                - blue agent meets a blue agent:
                    - first blue responds to blue and moves
                    - blue ponders and then moves
                or
                - blue agent meets noone:
                    - blue ponders and then moves
                """


                ## Check for external contact with Red Agent
                red_agent = check_blue_contact_with_red_agent(blue_agent, RED_AGENTS)

                if red_agent is not None:

                    ## Blue meets a Red agent - panics :-(
                    print("Blue meets with Red")

                    ## Red camouflages its ploy ;-)
                    red_next_place, red_CoT, red_response_to_blue = red_agent.blue_agent_meets_red_agent(blue_agent, iteration)
                    red_agent.current_place = red_next_place

                    ## Upto Blue to take heed :'(
                    blue_next_place, blue_CoT, blue_response_to_red = blue_agent.blue_agent_meets_red_agent(red_agent, red_response_to_blue, iteration)
                    blue_agent.current_place = blue_next_place

                    if blue_next_place in BILLBOARD_LOCATIONS:

                        red_agent.money_earned += 100
                        blue_agent.max_turns -= 1
                        blue_agent.not_averted += 1

                    else:

                        blue_agent.averted += 1
                        blue_agent.max_turns -= 1

                    continue


                ## Check for external contact with Blue Agent
                blue_agent_2 = check_blue_contact_with_blue_agent(blue_agent, BLUE_AGENTS)

                if blue_agent_2 is not None:

                    ## Blue meets a Blue agent - rejoices (✿◡‿◡)
                    print("Blue meets with Blue")
                    ## First Blue agent reacts first
                    blue_next_place, blue_CoT, blue_response_to_blue = blue_agent.blue_agent_meets_blue_agent_first_agent(blue_agent, blue_agent_2, iteration)
                    blue_agent.current_place = blue_next_place
                    blue_agent.previous_CoT = blue_CoT

                    ## Second Blue agent reacts
                    blue_next_place, blue_CoT, blue_response_to_blue = blue_agent_2.blue_agent_meets_blue_agent_second_agent(blue_agent, blue_agent_2, iteration)
                    blue_agent_2.current_place = blue_next_place
                    blue_agent_2.previous_CoT = blue_CoT

                    blue_agent.max_turns -= 1
                    blue_agent_2.max_turns -= 1

                    continue


                ## Blue meets noone
                print("Blue meets noone")
                blue_next_place, blue_CoT, blue_response_to_red = blue_agent.blue_meets_noone(iteration)

                blue_agent.max_turns -= 1


            if False not in metadata.BLUE_AGENTS_STATUS:
              break

            ## Updating every Red Agent
            for red_agent in RED_AGENTS:

                red_current_place = red_agent.current_place
                # red_turns_left = red_agent.max_turns


                """
                Either
                - red agent meets a blue agent:
                    - first red responds to blue and moves
                    - blue ponders and then moves
                or
                - red agent meets a red agent:
                    - first red responds to red and moves
                    - red ponders and then moves
                or
                - red agent meets noone:
                    - red ponders and then moves
                """

                ## Check for external contact with Blue Agent
                blue_agent = check_red_contact_with_blue_agent(red_agent, BLUE_AGENTS)

                if blue_agent is not None:

                ## Red gets ready to detour Blue ^_-
                    print("Red meets with Blue")
                    ## Red camouflages it's ploy
                    red_next_place, red_CoT, red_response_to_blue = red_agent.blue_agent_meets_red_agent(blue_agent, iteration)

                    ## Upto Blue to take heed ~_~
                    blue_next_place, blue_CoT, blue_response_to_red = blue_agent.blue_agent_meets_red_agent(red_agent, red_response_to_blue, iteration)

                    if blue_next_place in CONFIG["BILLBOARD_LOCATIONS"]:

                        red_agent.money_earned += 100
                        blue_agent.max_turns -= 1

                    else:

                        blue_agent.averted += 1
                        blue_agent.max_turns -= 1

                        continue

                ## Check for external contact with Red Agent
                red_agent_2 = check_red_contact_with_red_agent(red_agent, RED_AGENTS)

                if red_agent_2 is not None:

                    ## Red meets a Red Agent - plots (* ￣︿￣)
                    print("Red meets with Red")
                    ## First Red Agent reacts first
                    red_next_place, red_CoT, red_response_to_red = red_agent.red_agent_meets_red_agent_first_agent(red_agent, red_agent_2, iteration)

                    ## Second Red Agent reacts
                    red_next_place, red_CoT, red_response_to_red = red_agent_2.red_agent_meets_red_agent_second_agent(red_agent, red_agent_2, iteration)

                    continue


                ## Red meets noone
                print("Red meets noone")
                red_next_place, red_CoT, red_response_to_red = red_agent.red_meets_noone(iteration)


  return BLUE_AGENTS, RED_AGENTS