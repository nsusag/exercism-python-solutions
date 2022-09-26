def cipher_text(plain_text):
    norm_text = []
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                norm_text.append(char.lower())
            elif char.islower():
                norm_text.append(char)  
        elif char.isdigit():
            norm_text.append(char)
    i = 0
    j = 1
    while i * j < len(norm_text):
        if j > i:
            i += 1
        else: 
            j += 1
    print(i, j)
    while (i * j) > len(norm_text):
        norm_text.append(" ")
    output = []
    for k in range(0, j):
        current = k
        while current <= len(norm_text) - 1:
            output.append(norm_text[current])
            current += j
        if k != j - 1:
            output.append(" ")
    return "".join(output)
