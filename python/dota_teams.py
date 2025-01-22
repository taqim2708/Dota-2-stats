import json
from collections import defaultdict


def group_players_by_team_id(json_file_path: str) -> dict:
    with open(json_file_path, "r") as file:
        data = json.load(file)

    leaderboard = data.get("leaderboard", [])
    teams = defaultdict(list)

    for player in leaderboard:
        team_id = player.get("team_id")
        if team_id is not None:
            teams[team_id].append(player)

    return teams


# Example usage
if __name__ == "__main__":
    regions = ["europe", "americas", "se_asia", "china"]
    json_file_path = f"json/{regions[3]}_leaderboard.json"
    teams = group_players_by_team_id(json_file_path)
    for team_id, players in teams.items():
        if len(players) > 3:
            print(f"Team ID: {team_id}")
            for player in players:
                print(player)
