import os
import random
import json

BILLBOARD_LOCATIONS = [
    "Times Square", "Broadway", "7th Avenue", "8th Avenue", "42nd Street", "5th Avenue", "6th Avenue", "Herald Square", 
    "Madison Square Garden", "Lincoln Tunnel", "Holland Tunnel", "Queensboro Bridge", "George Washington Bridge", 
    "The High Line", "SoHo", "Flatiron District", "Wall Street", "Fulton Street", "Barclays Center", "DUMBO", 
    "Times Square Subway Station", "Penn Station", "Grand Central Terminal", "FDR Drive", "West Side Highway",
]

NYC_LOCATIONS = [
    "Statue of Liberty", "Ellis Island Immigration Museum", "Central Park", "Times Square", "Empire State Building", 
    "Brooklyn Bridge", "Rockefeller Center", "The Metropolitan Museum of Art", "Museum of Modern Art", 
    "American Museum of Natural History", "The High Line", "Grand Central Terminal", "One World Trade Center", 
    "9/11 Memorial & Museum", "Coney Island", "Yankee Stadium", "Madison Square Garden", "Broadway Theater District", 
    "Chrysler Building", "Wall Street & New York Stock Exchange", "Fifth Avenue", "SoHo", "Greenwich Village", "Harlem", 
    "Chinatown", "Little Italy", "Battery Park", "Washington Square Park", "Prospect Park", "Brooklyn Botanic Garden",
]