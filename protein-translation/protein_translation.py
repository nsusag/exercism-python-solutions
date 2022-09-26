def proteins(strand):
    index = 0 
    output = []
    while index + 3 <= len(strand):
        current = strand[index:index + 3]
        print(current)
        if current == "AUG":
            output.append("Methionine")
        elif current == "UUU" or current == "UUC":
            output.append("Phenylalanine")
        elif current == "UUA" or current == "UUG":
            output.append("Leucine")
        elif current == "UCU" or current == "UCC" or current == "UCA" or current == "UCG":
            output.append("Serine")
        elif current == "UAU" or current == "UAC":
            output.append("Tyrosine")
        elif current == "UGU" or current == "UGC":
            output.append("Cysteine")
        elif current == "UGG":
            output.append("Tryptophan")
        elif current == "UAA" or current == "UAG" or current == "UGA":
            break 
        index += 3
    print(output)
    return output
