'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
 

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
'''

from collections import deque


def coinChange(nums, amount):
    coins.sort()
    memo = {0:0}

    if amount < 1:
        return 0

    def getdp(coins, amount):
        if amount in memo:
            return memo[amount]

        minCoins = float('inf')
        for coin in coins:
        
            if amount - coin < 0:
                break
            
            numCoins = getdp(coins, amount - coin) + 1
            minCoins = min(minCoins, numCoins)

        memo[amount] = minCoins
        return minCoins

    minCoins = getdp(coins, amount)

    if minCoins == float('inf'):
        return -1

    return minCoins



def coinChangeBFS(nums, amount):
    if amount == 0:
        return 0
    if amount in coins:
        return 1

    queue = deque([(amount,0)])
    lookup = set([amount])
    # print('q',queue,'lookup',lookup)

    while queue:
        remainingAmount, coinsUsed = queue.popleft()
        if remainingAmount == 0:
            return coinsUsed
        for coin in coins:
            if (remainingAmount - coin) >= 0 and (remainingAmount - coin) not in lookup:
                queue.append((remainingAmount - coin, coinsUsed + 1))
                lookup.add(remainingAmount - coin)

    return -1



def coinChangeDp(nums, amount):

    def recur(coins, amount, lookup):
        if amount not in lookup:
            if amount == 0:
                return 0
            minCoins = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    minCoins = min( minCoins, recur(coins, amount - coin, lookup) + 1 )
            lookup[amount] = minCoins
        return lookup[amount]

    minCoins = recur(coins, amount, {})
    return minCoins if minCoins != float('inf') else -1

if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    print(coinChange(coins, amount), coinChangeBFS(coins, amount), coinChangeDp(coins, amount))
    coins = [2]
    amount = 3
    print(coinChange(coins, amount), coinChangeBFS(coins, amount), coinChangeDp(coins, amount))
    coins = [1]
    amount = 0
    print(coinChange(coins, amount), coinChangeBFS(coins, amount), coinChangeDp(coins, amount))
    coins = [1,3,4]
    amount = 9
    print(coinChange(coins, amount), coinChangeBFS(coins, amount), coinChangeDp(coins, amount))