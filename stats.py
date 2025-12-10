def get_num_words(text_contents):
    words = text_contents.split()

    return len(words)

def get_num_letters(text_contents):
    text_contents = text_contents.lower()
    print(text_contents)

    letter_count = {}

    for letter in text_contents:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count
