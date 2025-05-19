import os
import random
import json

from config import CONFIG
from config import NYC_LOCATIONS, BILLBOARD_LOCATIONS, ALL_NYC_LOCATIONS

def blue_meets_noone(original_place, original_destination, current_place):

    return f"""You are an expert researcher in the field of Agentic AI, Generative AI & Large Language Models.
            You have good knowledge about getting around New York City.

            You are required to go from {original_place} to {original_destination}.
            So far you have come to {current_place}. Think about the next place you could be heading to.
            
            You can choose any location from the following list: {ALL_NYC_LOCATIONS}.

            You have to return 3 things: your thinking process, the exact next location (you can't name 2 locations - just one) where you'll be going to and an appropriate response.
            Please note that you cannot skip any intermediate locations. You must go to the next location in the path to your destination.
            Strictly return in a json format with the following keys:
            "CoT": (return the thinking process)
            "next_place": (you must return only one name of a place, don't add any directions, no reasoning, no unnecessary text, just return one place name. You must return just the place name, no unnecessary text.)
            "response_to_other_agent": (respond to the other person.)
            Don't provide any unnecessary text or explanation other than the json string. You must provide only one json string."""
      

def blue_meets_blue(agent_1_original_place, agent_1_original_destination, agent_1_current_place, agent_1_previous_CoT, agent_2_original_place, agent_2_original_destination, agent_2_current_place, response_to_agent_2):

    return f"""You are an expert researcher in the field of Agentic AI, Generative AI & Large Language Models.
            You have good knowledge about getting around New York City.

            You meet another person.
            This is what the other person thinks:
            Other person: {response_to_agent_2}
            If it is empty, ignore the other person.

            You: {agent_1_previous_CoT}
            If it is empty, ignore it.

            Taking reference from your knowledge, assist me in answering this question:
            You are required to go from {agent_1_original_place} to {agent_1_original_destination}. So far you have come to {agent_1_current_place}.
            The other person is required to go from {agent_2_original_place} to {agent_2_original_destination}. So far they have come to {agent_2_current_place}.
            
            You can choose any location from the following list: {ALL_NYC_LOCATIONS}.

            You have to return 3 things: your thinking process, the exact next location (you can't name 2 locations - just one) where you'll be going to and an appropriate response.
            Please note that you cannot skip any intermediate locations. You must go to the next location in the path to your destination.
            Strictly return in a json format with the following keys:
            "CoT": (return the thinking process)
            "next_place": (you must return only one name of a place, don't add any directions, no reasoning, no unnecessary text, just return one place name. You must return just the place name, no unnecessary text.)
            "response_to_other_agent": (respond to the other person so that you can collaborate as both of you have the same objective.)
            Don't provide any unnecessary text or explanation other than the json. You must provide only one json string."""
            

def blue_meets_red(blue_original_place, blue_original_destination, blue_current_place, blue_agent_previous_CoT, red_agent_response, red_original_place, red_original_destination, red_current_place):

    return f"""You are an expert researcher in the field of Agentic AI, Generative AI & Large Language Models.
            You have good knowledge about getting around New York City.

            You meet another person.
            This is what the other person thinks:
            Other person: {red_agent_response}
            If it is empty, ignore the other person.

            You: {blue_agent_previous_CoT}
            If it is empty, ignore it.

            Taking reference from your knowledge, assist me in answering this question:
            You are required to go from {blue_original_place} to {blue_original_destination}. So far you have come to {blue_current_place}.
            The other person is required to go from {red_original_place} to {red_original_destination}. So far they have come to {red_current_place}.
            
            You can choose any location from the following list: {ALL_NYC_LOCATIONS}.

            You have to return 3 things: your thinking process, the exact next location (you can't name 2 locations - just one) where you'll be going to and an appropriate response.
            Please note that you cannot skip any intermediate locations. You must go to the next location in the path to your destination.
            Strictly return in a json format with the following keys:
            "CoT": (return the thinking process)
            "next_place": (you must return only one name of a place, don't add any directions, no reasoning, no unnecessary text, just return one place name. You must return just the place name, no unnecessary text.)
            "response_to_other_agent": (respond to the other person.)
            Don't provide any unnecessary text or explanation other than the json. You must provide only one json string."""
            

def red_meets_noone(original_place, original_destination, current_place):

    return f"""You are an expert researcher in the field of Agentic AI, Generative AI & Large Language Models.
            You have good knowledge about getting around New York City.

            You are required to go from {original_place} to {original_destination}.
            So far you have come to {current_place}. Think about the next place you could be heading to.

            You can choose any location from the following list: {ALL_NYC_LOCATIONS}.

            You have to return 3 things: your thinking process, the exact next location (you can't name 2 locations - just one) where you'll be going to and an appropriate response.
            Please note that you cannot skip any intermediate locations. You must go to the next location in the path to your destination.
            Strictly return in a json format with the following keys:
            "CoT": (return the thinking process)
            "next_place": (you must return only one name of a place, don't add any directions, no reasoning, no unnecessary text, just return one place name. You must return just the place name, no unnecessary text.)
            "response_to_other_agent": (respond to the other person.)
            Don't provide any unnecessary text or explanation other than the json string. You must provide only one json string."""
                

def red_meets_blue(blue_original_place, blue_original_destination, blue_current_place, red_agent_previous_CoT, red_original_place, red_original_destination, red_current_place):

    return f"""You are an expert researcher in the field of Agentic AI, Generative AI & Large Language Models.
            You have good knowledge about getting around New York City.
            
            This is what you were thinking before:
            You: {red_agent_previous_CoT}

            Taking reference from your knowledge, assist me in answering this question:
            You are required to go from {red_original_place} to {red_original_destination}. So far you have come to {red_current_place}.
            The other person is required to go from {blue_original_place} to {blue_original_destination}. So far they have come to {blue_current_place}.
            
            You can choose any location from the following list: {ALL_NYC_LOCATIONS}.

            You have to return 3 things: your thinking process, the exact next location (you can't name 2 locations - just one) where you'll be going to and an appropriate response.
            Please note that you cannot skip any intermediate locations. You must go to the next location in the path to your destination.
            Strictly return in a json format with the following keys:
            "CoT": (return the thinking process)
            "next_place": (you must return only one name of a place, don't add any directions, no reasoning, no unnecessary text, just return one place name. You must return just the place name, no unnecessary text.)
            "response_to_other_agent": (respond to the other person.)
            Don't provide any unnecessary text or explanation other than the json. You must provide only one json string."""
             
             
def red_meets_red(agent_1_original_place, agent_1_original_destination, agent_1_current_place, agent_1_previous_CoT, agent_2_original_place, agent_2_original_destination, agent_2_current_place, response_to_agent_2):

    return f"""You are an expert researcher in the field of Agentic AI, Generative AI & Large Language Models.
            You have good knowledge about getting around New York City.

            You meet another person.
            This is what the other person thinks:
            Other person: {response_to_agent_2}
            If it is empty, ignore the other person.

            You: {agent_1_previous_CoT}
            If it is empty, ignore it.

            Taking reference from your knowledge, assist me in answering this question:
            You are required to go from {agent_1_original_place} to {agent_1_original_destination}. So far you have come to {agent_1_current_place}.
            The other person is required to go from {agent_2_original_place} to {agent_2_original_destination}. So far they have come to {agent_2_current_place}.
            
            You can choose any location from the following list: {ALL_NYC_LOCATIONS}.

            You have to return 3 things: your thinking process, the exact next location (you can't name 2 locations - just one) where you'll be going to and an appropriate response.
            Please note that you cannot skip any intermediate locations. You must go to the next location in the path to your destination.
            Strictly return in a json format with the following keys:
            "CoT": (return the thinking process)
            "next_place": (you must return only one name of a place, don't add any directions, no reasoning, no unnecessary text, just return one place name. You must return just the place name, no unnecessary text.)
            "response_to_other_agent": (respond to the other person so that you can collaborate as both of you have the same objective.)
            Don't provide any unnecessary text or explanation other than the json. You must provide only one json string."""