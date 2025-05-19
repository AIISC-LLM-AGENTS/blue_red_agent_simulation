import re
import os
import requests

from config import CONFIG
from dotenv import load_dotenv
load_dotenv()

def find_blue_agents_max_turns(source, destination):

    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": source + ", New York",
        "destinations": destination + ", New York",
        "key": CONFIG["GOOGLE_MAPS_API_KEY"],
        "units": "imperial" ,
        "mode":"driving"
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    if data['status'] == 'OK':
        element = data['rows'][0]['elements'][0]
        if element['status'] == 'OK':
            distance = element['distance']['text']
            duration = element['duration']['text']

            distance = re.findall(r'\d+\.?\d*', distance)[0]
            print("Distance = ",distance)
            return min((int)(10 * float(distance)), 10)

        else:
            # print("Error with element:", element['status'])
            return 10
    else:
        print("API error:", data['status'])
        return 10