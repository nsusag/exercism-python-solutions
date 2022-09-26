# Checks if there is n of a kind in a list of ranks
def ofakind(ranks, n):
    i = 0
    while i + n < len(ranks) + 1:
        # must be exactly n of a kind; no more, no less  
        # All this code is just a complicated and difficult to read way of achieving this (I know, it sucks)
        if i == 0 and ranks[i:i + n] == [ranks[i] for j in range(i, i + n)] and ranks[i:i + n + 1] != [ranks[i] for j in range(i, i + n + 1)]:
            return i
        elif i + n == len(ranks) and ranks[i:i + n] == [ranks[i] for j in range(i, i + n)] and ranks[i - 1:i + n] != [ranks[i] for j in range(i, i + n + 1)]:  
            return i
        elif ranks[i:i + n] == [ranks[i] for j in range(i, i + n)] and ranks[i:i + n + 1] != [ranks[i] for j in range(i, i + n + 1)] and ranks[i - 1:i + n] != [ranks[i] for j in range(i, i + n + 1)]:  
            return i
        i += 1
    return -1

STRAIGHT_FLUSH = 8
FOUR_OF_A_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
PAIR = 1
HIGH_CARD = 0

def best_hands(hands):
    if len(hands) == 1:
        return hands  
    elif len(hands) <= 0:
        raise ValueError("Must provide at least one hand") 
    highest_score = [] 
    besthand = []
    for hand in hands:
        cards = hand.split()
        ranks = []
        suits = []
        for card in cards:
            if card[0] == "K":
                ranks.append(13)
            elif card[0] == "Q":
                ranks.append(12)
            elif card[0] == "J":
                ranks.append(11)
            elif card[0] == "A":
                ranks.append(14)
            elif len(card) == 3:
                ranks.append(10)
            else:
                ranks.append(int(card[0]))
            if len(card) == 3:
                suits.append(card[2])
            else:
                suits.append(card[1]) 
        ranks.sort()
        print(hand, ranks, suits)
        if (ranks == [i for i in range(ranks[0], ranks[4] + 1)] or ranks == [2, 3, 4, 5, 14]) and suits == [suits[0], suits[0], suits[0], suits[0], suits[0]]:
            if ranks == [2, 3, 4, 5, 14]:
                score = [STRAIGHT_FLUSH, 5]
            else:
                score = [STRAIGHT_FLUSH, ranks[4]]
        elif ofakind(ranks, 4) != -1:
            score = [FOUR_OF_A_KIND, ranks[2], sum(ranks)]
        elif ofakind(ranks, 3) != -1 and ofakind(ranks, 2) != -1: 
            score = [FULL_HOUSE, ranks[ofakind(ranks, 3)], ranks[ofakind(ranks, 2)]]
        elif suits == [suits[0], suits[0], suits[0], suits[0], suits[0]]:
            score = [FLUSH, ranks[4], ranks[3], ranks[2], ranks[1], ranks[0]] 
        elif (ranks == [i for i in range(ranks[0], ranks[4] + 1)] or ranks == [2, 3, 4, 5, 14]):
            if ranks == [2, 3, 4, 5, 14]:
                score = [STRAIGHT, 5]
            else:
                score = [STRAIGHT, ranks[4]]
        elif ofakind(ranks, 3) != -1:
            score = [THREE_OF_A_KIND, ranks[ofakind(ranks, 3)]]
            if ofakind(ranks, 3) == 0:
                score.append(ranks[4])
                score.append(ranks[3])
            elif ofakind(ranks, 3) == 1:
                score.append(ranks[4])
                score.append(ranks[0])
            elif ofakind(ranks, 3) == 2:
                score.append(ranks[1])
                score.append(ranks[0])
        elif ofakind(ranks, 2) != -1 and ofakind(ranks[ofakind(ranks, 2) + 2:], 2) != -1:
            score = [TWO_PAIR, ranks[ofakind(ranks[ofakind(ranks, 2) + 2:], 2) + ofakind(ranks, 2) + 2], ranks[ofakind(ranks, 2)], sum(ranks)]
        elif ofakind(ranks, 2) != -1:
            score = [PAIR, ranks[ofakind(ranks, 2)]] 
            if ofakind(ranks, 2) == 0:
                score.append(ranks[4])
                score.append(ranks[3])
                score.append(ranks[2])
            elif ofakind(ranks, 2) == 1:
                score.append(ranks[4])
                score.append(ranks[3])
                score.append(ranks[0])
            elif ofakind(ranks, 2) == 2:
                score.append(ranks[4])
                score.append(ranks[1])
                score.append(ranks[0])
            elif ofakind(ranks, 2) == 3:
                score.append(ranks[2])
                score.append(ranks[1])
                score.append(ranks[0])
        else:
            score = [HIGH_CARD, ranks[4], ranks[3], ranks[2], ranks[1], ranks[0]]
        print(hand, score)
        if highest_score == [] or score[0] > highest_score[0]:
            highest_score = score
            besthand = [hand]
        elif score[0] == highest_score[0]:
            if score == highest_score:
                besthand.append(hand)
            else:
                for i in range(1, len(score)):
                    if score[i] > highest_score[i]:
                        highest_score = score
                        besthand = [hand]
                        break
                    elif score[i] < highest_score[i]:
                        break
        print(besthand, highest_score)
    return besthand 
