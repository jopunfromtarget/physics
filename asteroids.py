import requests

# Import NASA API data for NEOS over a 7-day period
API_KEY = "DL3MLvqyEUJYDb358C256UXvEx3Gh6JHNF1gmCeU"
url = "https://api.nasa.gov/neo/rest/v1/feed"

params = {
    "start_date": "2025-01-01",
    "end_date": "2025-01-06",
    "api_key": API_KEY
}

# Accesses the URL above, converts to JSON file
data = requests.get(url, params=params).json()

# Gets all NEOs regardless of date to allow
# iteration over all asteroids in the file
neos_dated = data["near_earth_objects"]

clean_data = []

# Iterates through each asteroid entry in the file,
# stores relevant data in empty list 'clean_data'
for date, asteroid_list in neos_dated.items():
    for asteroid in asteroid_list:

        if not asteroid["close_approach_data"]:
            continue

        approach = asteroid["close_approach_data"][0]
        diam = asteroid["estimated_diameter"]["meters"]

        clean_data.append({
            "name": asteroid["name"],
            "mean_diameter_m": (diam["estimated_diameter_max"] + diam["estimated_diameter_min"]) / 2,
            "velocity_km_s": float(approach["relative_velocity"]["kilometers_per_second"]),
            "hazardous": asteroid["is_potentially_hazardous_asteroid"],
            "close_approach_date": approach["close_approach_date"],
        })


