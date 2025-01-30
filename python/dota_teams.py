import json
from collections import defaultdict


def group_players_by_team_id(json_file_path: str) -> dict:
    with open(json_file_path, "r") as file:
        data: dict = json.load(file)

    leaderboard: list[dict] = data.get("leaderboard", [])
    teams = defaultdict(list)

    for player in leaderboard:
        team_id = player.get("team_id")
        if team_id is not None:
            teams[team_id].append(player)

    return teams


# Example usage
if __name__ == "__main__":
    regions = ["europe", "americas", "se_asia", "china"]
    try:
        region_index = int(
            input(
                "Enter region number (1: europe, 2: americas, 3: se_asia, 4: china): "
            ).strip()
        )
        region = regions[region_index - 1]
    except (ValueError, IndexError):
        print("Invalid region number. Please enter a valid number.")
        exit(1)
    json_file_path = f"json/{region}_leaderboard.json"
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
