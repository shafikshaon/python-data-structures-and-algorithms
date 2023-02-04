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


Time complexity - O(n)
Space complexity - O(1)
"""
