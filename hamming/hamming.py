def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("distance: input parameters are of unequal length")
    distance = 0
    for char_a, char_b in zip(strand_a, strand_b):
        if char_a != char_b:
            distance += 1
    return distance
