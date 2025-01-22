import os
import requests
import json

# Ensure the directory exists
output_dir = "json"
os.makedirs(output_dir, exist_ok=True)

# Define regions to fetch data for
regions = ["europe", "americas", "se_asia", "china"]

# Loop through each region and fetch leaderboard data
for region in regions:
    url = "https://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/" +\
        f"v0001?division={region}&leaderboard=0"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully retrieved data for region: {region}")
        data = response.json()
        # Save data to a JSON file
        with open(os.path.join(output_dir, f"{region}_leaderboard.json"), 'w') as f:
            json.dump(data, f, indent=4)  # Pretty-print with indent
    else:
        print(f"Failed to retrieve data for region: {region}, status code: {response.status_code}")
