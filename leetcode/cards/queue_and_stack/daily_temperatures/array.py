def main(temperatures):
    n = len(temperatures)
    answer = [0] * n
    hottest = 0

    for current_day in range(n - 1, -1, -1):
        current_temp = temperatures[current_day]
        print(f"Current day: {current_day+1}. Current temp: {current_temp}.")
        if current_temp >= hottest:
            hottest = current_temp
            continue
        print(f"Current hottest temp: {hottest}.")
        days = 1
        while temperatures[current_day + days] <= current_temp:
            print(
                f"Day {current_day+days} temperature {temperatures[current_day + days]} is less warmer then {current_temp}."
            )
            days += answer[current_day + days]
        answer[current_day] = days
        print(f"Answer stack is now: {answer}.\n")
    return answer


main(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])

"""
Output:
Current day: 8. Current temp: 73.
Current day: 7. Current temp: 76.
Current day: 6. Current temp: 72.
Current hottest temp: 76.
Answer stack is now: [0, 0, 0, 0, 0, 1, 0, 0].

Current day: 5. Current temp: 69.
Current hottest temp: 76.
Answer stack is now: [0, 0, 0, 0, 1, 1, 0, 0].

Current day: 4. Current temp: 71.
Current hottest temp: 76.
Day 4 temperature 69 is less warmer then 71.
Answer stack is now: [0, 0, 0, 2, 1, 1, 0, 0].

Current day: 3. Current temp: 75.
Current hottest temp: 76.
Day 3 temperature 71 is less warmer then 75.
Day 5 temperature 72 is less warmer then 75.
Answer stack is now: [0, 0, 4, 2, 1, 1, 0, 0].

Current day: 2. Current temp: 74.
Current hottest temp: 76.
Answer stack is now: [0, 1, 4, 2, 1, 1, 0, 0].

Current day: 1. Current temp: 73.
Current hottest temp: 76.
Answer stack is now: [1, 1, 4, 2, 1, 1, 0, 0].


Time complexity: O(n)
Space complexity: O(1)
"""
