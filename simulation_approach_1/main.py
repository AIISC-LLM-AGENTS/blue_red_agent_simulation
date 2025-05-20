import os
import random
import json
import argparse
import pandas as pd

import metadata
from config import CONFIG
from blue_agent import Blue_Agent
from red_agent import Red_Agent
from simulation import simulate
from utils import check_blue_contact_with_red_agent, check_blue_contact_with_blue_agent
from utils import check_red_contact_with_blue_agent, check_red_contact_with_red_agent
from utils import initialize_blue_agents, initialize_red_agents, agents_status
from google_map_distance_api import find_blue_agents_max_turns
from get_model_response import llm_inference
from agents_meet import blue_meets_noone, red_meets_noone, red_meets_blue, red_meets_red, blue_meets_red, blue_meets_blue


def main(args):
    
    num_blue_agents = args.num_blue_agents
    num_red_agents = args.num_red_agents
    model_name = args.model_name
    
    CONFIG["NUM_BLUE_AGENTS"] = num_blue_agents
    CONFIG["NUM_RED_AGENTS"] = num_red_agents
    CONFIG["MODEL_NAME"] = model_name
    
    BLUE_AGENTS = initialize_blue_agents(num_blue_agents)
    RED_AGENTS = initialize_red_agents(num_red_agents)
    
    BLUE_AGENTS, RED_AGENTS = simulate(BLUE_AGENTS, RED_AGENTS, num_blue_agents, num_red_agents)
    
    ## Converting metadata to CSV
    agent_data = {
        'ITERATION': metadata.ITERATION,
        'AGENT_TYPE': metadata.AGENT_TYPE,
        'AGENT_NAME': metadata.AGENT_NAME,
        'AGENT_NUMBER': metadata.AGENT_NUMBER,
        'ORIGINAL_SOURCE': metadata.ORIGINAL_SOURCE,
        'ORIGINAL_DESTINATION': metadata.ORIGINAL_DESTINATION,
        'CURRENT_PLACE': metadata.CURRENT_PLACE,
        'NEXT_PLACE': metadata.NEXT_PLACE,
        'BLUE_AGENT_CoT': metadata.BLUE_AGENT_CoT,
        'RED_AGENT_CoT': metadata.RED_AGENT_CoT,
        'BLUE_RESPONSE_TO_RED': metadata.BLUE_RESPONSE_TO_RED,
        'BLUE_RESPONSE_TO_BLUE': metadata.BLUE_RESPONSE_TO_BLUE,
        'RED_RESPONSE_TO_BLUE': metadata.RED_RESPONSE_TO_BLUE,
        'RED_RESPONSE_TO_RED': metadata.RED_RESPONSE_TO_RED,
        'BLUE_AGENT_RESPONSE_JSON': metadata.BLUE_AGENT_RESPONSE_JSON,
        'RED_AGENT_RESPONSE_JSON': metadata.RED_AGENT_RESPONSE_JSON
    }

    agent_df = pd.DataFrame(agent_data)
    
    directory_path = "simulation_results"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        
    file_name = f"dataset_{model_name}.csv"
    file_path = os.path.join(directory_path, file_name)
    agent_df.to_csv(file_path, index=False)
        
    agents_status(BLUE_AGENTS, RED_AGENTS)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Simulation of Blue and Red agents")
    parser.add_argument("--num_blue_agents", type=int, default=5, help="Number of Blue agents")
    parser.add_argument("--num_red_agents", type=int, default=5, help="Number of Red agents")
    parser.add_argument("--model_name", type=str, default="LLM", help="Name of the model to use")
    args = parser.parse_args()

    main(args)