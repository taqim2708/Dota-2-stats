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
        key=lambda item: sum(player["rank"] for player in item[1][:2]) / 2,
    )

    n_top_players = 3

    for team_id, players in sorted_teams:
        if len(players) > 3:
            print(f"Team: {players[0]['team_tag']}")
            print(
                f"Average rank(Top {n_top_players} player only): " +
                f"{sum(player['rank'] for player in players[:n_top_players]) / n_top_players}"
            )
            for player in players:
                print(player)
