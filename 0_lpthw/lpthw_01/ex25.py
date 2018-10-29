def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """This function will sort words for us"""
    return sorted(words)

def print_first_word(words):
    """This function will print the first word in the list."""
    word = words.pop(0)
    return word

def print_last_word(words):
    # Print the last word, using pop(), the chosen word will be removed from the list
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    words = break_words(sentence)
    sorted_sentence = sort_words(words)
    return sorted_sentence

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
