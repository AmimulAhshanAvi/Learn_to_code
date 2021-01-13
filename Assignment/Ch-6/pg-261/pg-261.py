import ch1text

def count_sentences(text):
    count = 0
    terminals = '.;?!'

    for char in text:
        if char in terminals:
            count = count + 1

    return count

