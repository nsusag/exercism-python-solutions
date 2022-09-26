def latest(scores):
    return scores[len(scores) - 1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    new_scores = scores.copy()
    new_scores.sort()
    result = []
    i = 0
    while len(scores) > i and i < 3:
        result.append(new_scores[len(new_scores) - i - 1])
        i = i + 1
    return result 
