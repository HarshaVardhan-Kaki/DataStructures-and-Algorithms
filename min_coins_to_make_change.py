# O(nd) time and O(n) space
# n is target amount and d is no.of denominations
def minNumberOfCoinsForChange(n, denoms):
    coins = [float("inf") for i in range(n+1)]
    coins[0] = 0
    for i in range(len(coins)):
        for denom in denoms:
            if denom <= i:
                coins[i] = min(coins[i],1 + coins[i - denom])
    return coins[-1] if coins[-1] != float("inf") else -1

