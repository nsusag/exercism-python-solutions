def ci_list(lst):
    result = []
    for char in lst:
        result.append(char.lower())
    return result

def find_anagrams(word, candidates):
    anagrams = []    
    lst_word = ci_list(word) 
    for candidate in candidates:
        if len(candidate) == len(word) and ci_list(candidate) != lst_word:
            for char in candidate:
                if char.lower() in lst_word:
                    del lst_word[lst_word.index(char.lower())]
                else:
                    break
        if lst_word == []:
            anagrams.append(candidate)
            lst_word = ci_list(word)
    print(anagrams)
    return anagrams
