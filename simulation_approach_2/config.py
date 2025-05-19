import os

from dotenv import load_dotenv
load_dotenv()
from locations import BILLBOARD_LOCATIONS, NYC_LOCATIONS, ALL_NYC_LOCATIONS

CONFIG = {
    "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
    "GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY"),
    "MODEL_NAME": "meta-llama/llama-4-scout-17b-16e-instruct",
    "BILLBOARD_LOCATIONS": BILLBOARD_LOCATIONS,
    "NYC_LOCATIONS": NYC_LOCATIONS,
    "ALL_NYC_LOCATIONS": ALL_NYC_LOCATIONS,
    "NUM_BLUE_AGENTS": 5,
    "NUM_RED_AGENTS": 5,
    "NUM_PLACES": len(NYC_LOCATIONS),
}