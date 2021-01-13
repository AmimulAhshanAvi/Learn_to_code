def count_sentences(text):
    count = 0

    for char in text:
        if char == '.' or char == ';' or char == '?' or char == '!':
            count = count + 1

    return count
