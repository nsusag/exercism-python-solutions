def measure(bucket_one, bucket_two, goal, start_bucket): 
    movecount = 0
    if start_bucket == "one":
        firstfilled = [bucket_one, bucket_one]
        movecount += 1
        if bucket_two == goal:
            return (2, "two", firstfilled[0])
        other = [0, bucket_two]
    elif start_bucket == "two":
        firstfilled = [bucket_two, bucket_two]
        movecount += 1
        if bucket_one == goal:
            return (2, "one", firstfilled[0])
        other = [0, bucket_one]
    while firstfilled[0] != goal:
        if other[0] == other[1]:
            other[0] = 0
        elif firstfilled[0] > 0: 
            other[0] += firstfilled[0]
            if other[0] > other[1]:
                firstfilled[0] = other[0] - other[1]
                other[0] = other[1]
            else:
                firstfilled[0] = 0
        elif firstfilled[0] == 0:
            firstfilled[0] = firstfilled[1]
        movecount += 1
    return (movecount, start_bucket, other[0])
