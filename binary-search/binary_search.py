def find(search_list, value):
    length = len(search_list)
    left = 0
    right = length - 1 
    middle = (left + right) // 2 
    if middle < 0:
        raise ValueError("Nothing could be found")
    while search_list[middle] != value:
        print(left, middle, right)
        if left > right:
            raise ValueError("Nothing could be found")
        if search_list[middle] < value:
            left = middle + 1
        elif search_list[middle] > value:
            right = middle - 1 
        middle = (left + right) // 2
    return middle 
