def get_num_words(text_contents):
    words = text_contents.split()

    return len(words)

def get_num_letters(text_contents):
    text_contents = text_contents.lower()

    letter_count = {}

    for letter in text_contents:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count

def sort_on(items):
    return items["num"]

def sort_chars(letter_count):
    sorted_dict = []

    for char in letter_count:
        if char.isalpha():
            sorted_dict.append({"char" : char, "num" : letter_count[char]})

    sorted_dict.sort(reverse=True, key=sort_on)

    return sorted_dict
