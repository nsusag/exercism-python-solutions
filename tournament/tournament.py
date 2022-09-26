def tally(rows):
    result = ["Team                           | MP |  W |  D |  L |  P"]  
    teams = {}
    for match in rows:
        data = match.split(";")
        for j in range(0, 2):
            if data[j] not in teams:
                teams[data[j]] = [0, 0, 0]
        if data[2] == "win":
            teams[data[0]][0] += 1
            teams[data[1]][2] += 1
        elif data[2] == "draw":
            teams[data[0]][1] += 1
            teams[data[1]][1] += 1
        elif data[2] == "loss":
            teams[data[0]][2] += 1
            teams[data[1]][0] += 1 
    for element in sorted(sorted(teams.items(), key=lambda team: team[0]), key=lambda team: 3 * team[1][0] + team[1][1], reverse=True):
        result.append("{team:<30} | {matches:>2} | {wins:>2} | {draws:>2} | {losses:>2} | {points:>2}".format(team=element[0],matches=element[1][0]+element[1][1]+element[1][2],wins=element[1][0],draws=element[1][1],losses=element[1][2],points=3*element[1][0]+element[1][1]))
    return result
