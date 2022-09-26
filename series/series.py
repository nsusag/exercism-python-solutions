def slices(series, length):
    if length > len(series) or length < 1:
        raise ValueError("An error occurred.")
    i = 0
    result = []
    while i + length - 1 < len(series):
        result.append(series[i:i + length])
        i += 1
    return result
