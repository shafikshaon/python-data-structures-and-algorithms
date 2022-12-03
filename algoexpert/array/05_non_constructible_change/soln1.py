from typing import List


def non_constructible_coin(coins: List) -> int:
    coins.sort()
    current_changed = 0
    for coin in coins:
        if coin > current_changed + 1:
            return current_changed + 1
        current_changed += coin
    return current_changed + 1


def main():
    coins = [5, 7, 1, 1, 2, 3, 22]
    print(non_constructible_coin(coins))


main()

# Time complexity - O(log(n))
# Space complexity - O(n)
