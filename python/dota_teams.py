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
    json_file_path = f"json/{regions[0]}_leaderboard.json"
    teams = group_players_by_team_id(json_file_path)

    sorted_teams = sorted(
        teams.items(),
        key=lambda item: sum(player["rank"] for player in item[1]) / len(item[1]),
    )

    for team_id, players in sorted_teams:
        if len(players) > 3:
            print(f"Team ID: {team_id}")
            print(
                f"Average rank: {sum(player['rank'] for player in players) / len(players)}"
            )
            for player in players:
                print(player)
