import os
import random
import json

BILLBOARD_LOCATIONS = [
    "times square", "broadway", "7th avenue", "8th avenue", "42nd street", "5th avenue", "6th avenue", "herald square",
    "madison square garden", "lincoln tunnel", "holland tunnel", "queensboro bridge", "george washington bridge",
    "the high line", "soho", "flatiron district", "wall street", "fulton street", "barclays center", "dumbo",
    "times square subway station", "penn station", "grand central terminal", "fdr drive", "west side highway",
    "statue of liberty", "ellis island immigration museum", "central park", "empire state building",
    "brooklyn bridge", "rockefeller center", "the metropolitan museum of art", "museum of modern art",
    "american museum of natural history", "one world trade center", "9/11 memorial & museum", "coney island",
    "yankee stadium", "broadway theater district", "chrysler building", "wall street & new york stock exchange",
    "fifth avenue", "greenwich village", "harlem", "chinatown", "little italy", "battery park",
    "washington square park", "prospect park", "brooklyn botanic garden",
]

NYC_LOCATIONS = [
    "bronx", "staten island", "queens", "brooklyn", "manhattan", "la guardia airport", "john f kennedy airport",
    "newark liberty international airport", "city hall", "federal hall", "lincoln center", "carnegie hall",
    "apollo theater", "cooper union", "new york university", "columbia university", "barnard college", "fordham university",
    "brooklyn college", "york college", "st. john's university", "new york botanical garden", "bronx zoo", "prospect park zoo",
    "hudson river", "east river", "broad channel", "roosevelt island", "washington heights", "inwood", "upper west side",
    "upper east side", "midtown", "downtown", "chelsea", "garment district", "murray hill", "kips bay", "hamilton heights",
    "manhattanville", "van cortlandt park", "pelham bay park", "city island", "little neck", "bayside", "forest hills",
    "jamaica", "flushing", "astoria", "long island city", "lic waterfront", "jackson heights", "elmhurst", "rego park",
    "fresh meadows", "sunnyside", "woodside", "ridgewood", "bushwick", "greenpoint", "williamsburg", "carroll gardens",
    "park slope", "williamsburg bridge", "verrazano-narrows bridge", "throgs neck bridge", "bronx–whitestone bridge",
    "rfk bridge", "brooklyn heights promenade", "dumbo waterfront", "brooklyn navy yard", "gouverneur hospital",
    "nypa roosevelt island", "museum mile", "fifth avenue historic district", "sofia park"          
]

ALL_NYC_LOCATIONS = NYC_LOCATIONS + BILLBOARD_LOCATIONS
