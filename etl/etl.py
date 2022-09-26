def transform(legacy_data):
    output = {}
    for i in [1, 2, 3, 4, 5, 8, 10]: 
        if i in legacy_data:
            for char in legacy_data[i]:
                output[char.lower()] = i
    return output
