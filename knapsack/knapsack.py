import copy

def helper(coins, maximum_weight):
    most_valuable = []
    i = 0
    if len(table) >= maximum_weight and table[maximum_weight - 1] != []:
        return table[maximum_weight - 1]
    while i < len(coins) and coins[i] <= maximum_weight:
        if coins[i] == maximum_weight:
            result = [coins[i]]
        else:

            result = copy.deepcopy(helper(coins, maximum_weight - coins[i]))
            result.append(coins[i])
            result.sort()
        totalweight = 0
        totalvalue = 0
        for element in result:
            totalweight += element["weight"]
            totalvalue += element["value"]
        if totalweight <= maximum_weight and totalvalue > most_valuable:
            most_valuable = totalvalue
        i += 1 
    while len(table) < maximum_weight:
        table.append([])
    table[maximum_weight - 1] = most_valuable 
    print(table)
    return most_valuable

def maximum_value(maximum_weight, items):  
    if maximum_weight == 0:
        return []
    global table
    table = []
    most_valuable = 0
    i = 0
    while i < len(items) and maximum_weight[i]["weight"] <= maximum_weight:
        if items[i]["weight"] == maximum_weight:
            result = [coins[i]]
        else:
            newlst = copy.deepcopy(items)
            del newlst[i]
            result = copy.deepcopy(helper(newlst, maximum_weight - items[i]["weight"]))
            result.append(items[i])
            result.sort()
        totalweight = 0
        totalvalue = 0
        for element in result:
            totalweight += element["weight"]
            totalvalue += element["value"]
        if totalweight <= maximum_weight and totalvalue > most_valuable:
            most_valuable = totalvalue
        i += 1
    print(table)
    return most_valuable
