import copy, sys

sys.setrecursionlimit(2000)

def helper(coins, target):
    shortest = []
    i = 0
    if len(table) >= target and table[target - 1] != []:
        return table[target - 1]
    while i < len(coins) and coins[i] <= target:
        if coins[i] == target:
            result = [coins[i]]
        else:
            result = copy.deepcopy(helper(coins, target - coins[i]))
            result.append(coins[i])
            result.sort()
        if sum(result) == target and (shortest == [] or len(result) < len(shortest)):
            shortest = result
        i += 1 
    while len(table) < target:
        table.append([])
    table[target - 1] = shortest 
    print(table)
    return shortest

def find_fewest_coins(coins, target):
    if target == 0:
        return []
    elif target < coins[0]:
        raise ValueError("No solution exists.")    
    global table
    table = []
    shortest = []
    i = 0
    while i < len(coins) and coins[i] <= target:
        if coins[i] == target:
            result = [coins[i]]
        else:
            result = copy.deepcopy(helper(coins, target - coins[i]))
            result.append(coins[i])
            result.sort()
        if sum(result) == target and (shortest == [] or len(result) < len(shortest)):
            shortest = result
        i += 1
    if sum(shortest) != target:
        raise ValueError("No solution exists.")
    print(table)
    return shortest

find_fewest_coins([1, 5, 10, 25], 99)
