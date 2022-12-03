from typing import List


def update_scores(winning_team, point, scores):
    if winning_team not in scores:
        scores[winning_team] = 0
    scores[winning_team] += point


def tournament_winner(competitions: List, results: List) -> str:
    current_best_team = ""
    scores = {current_best_team: 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        winning_team = home_team if result == 1 else away_team  # 1 means home team win
        update_scores(winning_team, 3, scores)

        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team
    return current_best_team


def main():
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    results = [0, 0, 1]
    print(tournament_winner(competitions, results))


main()

# Time complexity - O(n)
# Space complexity - O(k)
# where n is the number if competitions and k is the number of team
