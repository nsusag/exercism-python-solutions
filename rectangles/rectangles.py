def rectangles(strings):
    corners = []
    rects = 0

    # adds all corners (+) to a list
    for y, string in enumerate(strings):
        corners.append([])
        for x, char in enumerate(string):
            if char == "+":
                corners[y].append(x)

    # Checks for rectangles

    # For every line
    for y, line in enumerate(corners):

        # For every possible combination of corners on that line
        for i, corner1 in enumerate(line):
            for corner2 in line[i + 1:]:
                # Check if there exists a rectangle with those two corners on the top line

                # Check if the two corners on the top line are actually connected
                j = corner1 + 1
                while j < corner2:
                    if strings[y][j] != "-" and strings[y][j] != "+":
                        break
                    j += 1
                if j != corner2:
                    break
                
                # Check for corners on lower lines which are the same horizontal distance apart as the corners on the top line
                for lower, newline in enumerate(corners[y + 1:]):
                    if corner1 not in newline or corner2 not in newline:
                        continue
                    else: 
                        # Checks that the top and bottom corners on both sides are actually connected
                        j = y + 1
                        while j < lower + y + 1:
                            if strings[j][corner1] != "|" and strings[j][corner1] != "+":
                                break
                            if strings[j][corner2] != "|" and strings[j][corner2] != "+":
                                break
                            j += 1
                        if j != lower + y + 1:
                            break
                        
                        # Checks that the bottom corners are actually connected
                        j = corner1 + 1
                        while j < corner2:
                            if strings[lower + y + 1][j] != "-" and strings[lower + y + 1][j] != "+":
                                break
                            j += 1
                        if j != corner2:
                            break                       
                        
                        rects += 1
    print(rects)
    return rects
