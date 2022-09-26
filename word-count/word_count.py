to_be_replaced = ['\t', '\n', '_', ',', '.', '"', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':']

def count_words(sentence):
    word_list = {}
    new_sentence = ""
    for i, char in enumerate(sentence):
        if char in to_be_replaced:
            new_sentence = new_sentence + ' '
        elif char.isalpha():
            new_sentence = new_sentence + char.lower()
        elif char == "'":
            if sentence[i - 1].isalpha() and i < len(sentence) - 1 and sentence[i + 1].isalpha():
                new_sentence = new_sentence + char
            else:
                new_sentence = new_sentence + ' '
        else:
            new_sentence = new_sentence + char
    for word in new_sentence.split():
        for char in word:
            if not char.isalpha() and not char.isdigit() and not char == "'":
                break
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1
    return word_list
