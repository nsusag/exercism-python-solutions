def recite(start_verse, end_verse):
    animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
    firstline = ["I don't know why she swallowed the fly. Perhaps she'll die.", "It wriggled and jiggled and tickled inside her.", "How absurd to swallow a bird!", "Imagine that, to swallow a cat!", "What a hog, to swallow a dog!", "Just opened her throat and swallowed a goat!", "I don't know how she swallowed a cow!", "She's dead, of course!"]
    output = []
    currentverse = start_verse - 1
    while currentverse != end_verse:
        if currentverse >= start_verse:
            output.append("")
        output.append("".join(["I know an old lady who swallowed a ", animals[currentverse], "."]))
        output.append(firstline[currentverse])
        counter = currentverse
        if currentverse < 7:
            while counter > 0:
                if counter == 2:
                    output.append("She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.")
                else:
                    output.append("".join(["She swallowed the ", animals[counter], " to catch the ", animals[counter - 1], "."]))
                counter -= 1
            if currentverse != 0:
                output.append(firstline[0])
        currentverse += 1
    print(output)
    return output
