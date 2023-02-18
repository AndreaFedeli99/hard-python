import re

def insert_words():
    word = ''
    words = []
    while word != 'stop':
        word = input("Insert one word, one of this punctuation sign . , ! ? ir stop to stop inserting words --> ")
        if word != 'stop':
            words.append(word)
    return words

def format_words(words):
    print("The formatted string you've insert is:")
    phrase = words[0].capitalize() + " "
    for word in words[1:]:
        if re.match(r"[.!?]", word) != None:
            phrase = phrase[:-1] + word + "\n"
        elif word == ',':
            phrase = phrase[:-1] + word + " "
        elif re.match(r"[.!?]", phrase[-2:]) != None:
            phrase += word.capitalize() + " "
        else:
            phrase += word + " "
    return phrase

def get_number_of_words(phrase):
    return len(phrase.split())

def get_number_of_punctuation_sign(phrase):
    return len(re.split(r"[.,!?]", phrase))

def get_number_of_phrases(phrase):
    return len(re.split(r"[.?!]", phrase))

def get_chars_freq(phrase):
    chars_frequence = {}
    for c in phrase:
        if re.match(r"[\w]", c) != None:
            try:
                chars_frequence[c.lower()] += 1
            except:
                chars_frequence.update({c.lower(): 1})
    return chars_frequence

def get_most_frequent_character(phrase):
    chars_frequence = {}
    most_frq_char = []
    max_freq = 0
    chars_frequence = get_chars_freq(phrase)
    for c,f in chars_frequence.items():
        if f >= max_freq:
            if f > max_freq:
                most_frq_char.clear()
            max_freq = f
            most_frq_char.append(c)
    return most_frq_char

def get_least_frequent_character(phrase):
    chars_frequence = {}
    least_frq_char = []
    min_freq = len(phrase) + 1
    chars_frequence = get_chars_freq(phrase)
    for c,f in chars_frequence.items():
        if f <= min_freq:
            if f < min_freq:
                least_frq_char.clear()
            min_freq = f
            least_frq_char.append(c)
    return least_frq_char

words = insert_words()
phrase = format_words(words)
print("\n{}".format(phrase))
print(f"The number of received word is {get_number_of_words(phrase)}")
print(f"The number of punctuation sign is {get_number_of_punctuation_sign(phrase)}")
print(f"The number of phrases is {get_number_of_phrases(phrase)}")
print(f"The most frequent character are {get_most_frequent_character(phrase)}")
print(f"The least frequent character are {get_least_frequent_character(phrase)}")