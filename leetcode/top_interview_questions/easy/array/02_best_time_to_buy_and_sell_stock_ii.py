from typing import List


def main(prices: List[int]) -> int:
    print(f"Prices array: {prices}")

    max_profit: int = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            print(
                f"Price {prices[i]} at index {i} is greater than {prices[i - 1]} at index {i - 1}"
            )
            max_profit += prices[i] - prices[i - 1]
            print(
                f"Current max profit: {max_profit}. Price difference: {prices[i] - prices[i - 1]}\n"
            )
        else:
            print(
                f"Price {prices[i]} at index {i} is less than {prices[i - 1]} at index {i - 1}\n"
            )
    print(f"Max profit: {max_profit}")
    return max_profit


main([1, 7, 2, 3, 6, 7, 6, 7])

# Time complexity - O(n)
# Space complexity - O(1)
