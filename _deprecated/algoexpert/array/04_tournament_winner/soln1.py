from typing import List


def tournament_winner(competitions: List, results: List) -> str:
    team_score = {}
    for idx, team in enumerate(competitions):
        if results[idx] == 0:
            winner = team[1]
        else:
            winner = team[0]
        if winner in team_score:
            team_score[winner] += 3
        else:
            team_score[winner] = 3
    current_best = 0
    best_team = ""
    for k, v in team_score.items():
        if current_best < v:
            current_best = v
            best_team = k

    return best_team


def main():
    competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0, 0, 1]
    print(tournament_winner(competitions, results))


main()

# Time complexity - O(n)
# Space complexity - O(k)
# where n is the number if competitions and k is the number of team
