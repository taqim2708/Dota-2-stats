import requests
import json

regions = ["europe", "americas", "se_asia", "china"]
for region in regions:
    url = "https://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/" +\
        f"v0001?division={region}&leaderboard=0"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(f'../json/{region}_leaderboard.json', 'w') as f:
            json.dump(data, f)
    else:
        print(f"Failed to retrieve data for region: {region}")
