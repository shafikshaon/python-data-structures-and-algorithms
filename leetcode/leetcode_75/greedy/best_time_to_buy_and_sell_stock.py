from typing import List


def main(prices: List) -> int:
    print(f"Prices are: {prices}.\n")
    min_price = float("inf")
    max_profit = 0

    for i in range(len(prices)):
        print(f"Current price: {prices[i]}.")
        if prices[i] < min_price:
            min_price = prices[i]
            print(f"Min price: {min_price}.")
        elif prices[i] - min_price > max_profit:
            print(f"Max profit ({prices[i]} - {min_price}) = {prices[i] - min_price}.")
            max_profit = prices[i] - min_price
        print("\n")
    print(f"The max profit can achieve is: {max_profit}.")
    return max_profit


main(prices=[7, 1, 5, 3, 6, 4])
print(
    "-----------------------------------------------------------------------------------------------------"
)
main(prices=[7, 6, 4, 3, 1])

# Time complexity: O(n)
# Space complexity: O(1)

# Output
"""
Prices are: [7, 1, 5, 3, 6, 4].

Current price: 7.
Min price: 7.


Current price: 1.
Min price: 1.


Current price: 5.
Max profit (5 - 1) = 4.


Current price: 3.


Current price: 6.
Max profit (6 - 1) = 5.


Current price: 4.


The max profit can achieve is: 5.
-----------------------------------------------------------------------------------------------------
Prices are: [7, 6, 4, 3, 1].

Current price: 7.
Min price: 7.


Current price: 6.
Min price: 6.


Current price: 4.
Min price: 4.


Current price: 3.
Min price: 3.


Current price: 1.
Min price: 1.


The max profit can achieve is: 0.
"""
