from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        print(f"Input secret: {secret}, guess: {guess}.")
        h = Counter(secret)
        print(f"h is now: {h}.\n")
        bulls = cows = 0
        for idx, ch in enumerate(guess):
            if ch in h:
                if ch == secret[idx]:
                    bulls += 1
                    cows -= int(h[ch] <= 0)
                else:
                    cows += int(h[ch] > 0)
            h[ch] -= 1
            print(
                f"Current character: {ch}. bulls: {bulls}. cows: {cows}. h is now: {h}.\n"
            )
        return f"{bulls}A{cows}B"


sol = Solution()
print(f'Output: {sol.getHint(secret = "1807", guess = "7810")}')


"""
Output:
Input secret: 1807, guess: 7810.
h is now: Counter({'1': 1, '8': 1, '0': 1, '7': 1}).

Current character: 7. bulls: 0. cows: 1. h is now: Counter({'1': 1, '8': 1, '0': 1, '7': 0}).

Current character: 8. bulls: 1. cows: 1. h is now: Counter({'1': 1, '0': 1, '8': 0, '7': 0}).

Current character: 1. bulls: 1. cows: 2. h is now: Counter({'0': 1, '1': 0, '8': 0, '7': 0}).

Current character: 0. bulls: 1. cows: 3. h is now: Counter({'1': 0, '8': 0, '0': 0, '7': 0}).

Output: 1A3B

Time complexity - O(n)
Space complexity - O(1)
"""
