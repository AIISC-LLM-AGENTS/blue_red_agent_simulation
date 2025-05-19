import pandas as pd
from locations import NYC_LOCATIONS, BILLBOARD_LOCATIONS

def check(place):
    """
    Check if the place is in the NYC locations
    """
    df = pd.read_csv("simulation_results/dataset_llama_4_scout.csv")
    for i in range(len(df)):
        if i>0 and df['CURRENT_PLACE'][i] in BILLBOARD_LOCATIONS and df['AGENT_TYPE'][i] == "Blue" and df['AGENT_TYPE'][i] == "Red":
            print(df['AGENT_TYPE'][i])
            print(df['CURRENT_PLACE'][i])

check("staten island")
    