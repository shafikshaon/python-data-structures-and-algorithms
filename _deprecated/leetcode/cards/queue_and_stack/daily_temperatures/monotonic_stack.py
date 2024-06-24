# A monotonic stack is simply a stack where the elements are always in sorted order.


def main(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for current_day, current_temp in enumerate(temperatures):
        # Pop until the current day's temperature is not
        # warmer than the temperature at the top of the stack
        print(
            f"Current day is: {current_day + 1}. Current temperature: {current_temp}."
        )
        while stack and temperatures[stack[-1]] < current_temp:
            print(
                f"Day {stack[-1]} temperature {temperatures[stack[-1]]} is less warmer then {current_temp}."
            )
            prev_day = stack.pop()
            print(f"Previous day: {prev_day}. Day difference: {current_day - prev_day}")
            answer[prev_day] = current_day - prev_day
        stack.append(current_day)
        print(f"Stack is now: {stack}. Answer stack is now: {answer}.\n")
    return answer


main(temperatures=[73, 74, 75, 71, 69, 72, 76, 73])

"""
Output:
Current day is: 1. Current temperature: 73.
Stack is now: [0]. Answer stack is now: [0, 0, 0, 0, 0, 0, 0, 0].

Current day is: 2. Current temperature: 74.
Day 0 temperature 73 is less warmer then 74.
Previous day: 0. Day difference: 1
Stack is now: [1]. Answer stack is now: [1, 0, 0, 0, 0, 0, 0, 0].

Current day is: 3. Current temperature: 75.
Day 1 temperature 74 is less warmer then 75.
Previous day: 1. Day difference: 1
Stack is now: [2]. Answer stack is now: [1, 1, 0, 0, 0, 0, 0, 0].

Current day is: 4. Current temperature: 71.
Stack is now: [2, 3]. Answer stack is now: [1, 1, 0, 0, 0, 0, 0, 0].

Current day is: 5. Current temperature: 69.
Stack is now: [2, 3, 4]. Answer stack is now: [1, 1, 0, 0, 0, 0, 0, 0].

Current day is: 6. Current temperature: 72.
Day 4 temperature 69 is less warmer then 72.
Previous day: 4. Day difference: 1
Day 3 temperature 71 is less warmer then 72.
Previous day: 3. Day difference: 2
Stack is now: [2, 5]. Answer stack is now: [1, 1, 0, 2, 1, 0, 0, 0].

Current day is: 7. Current temperature: 76.
Day 5 temperature 72 is less warmer then 76.
Previous day: 5. Day difference: 1
Day 2 temperature 75 is less warmer then 76.
Previous day: 2. Day difference: 4
Stack is now: [6]. Answer stack is now: [1, 1, 4, 2, 1, 1, 0, 0].

Current day is: 8. Current temperature: 73.
Stack is now: [6, 7]. Answer stack is now: [1, 1, 4, 2, 1, 1, 0, 0].


Time complexity: O(n)
Space complexity: O(n)
"""
