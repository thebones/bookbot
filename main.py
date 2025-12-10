from stats import get_num_words
from stats import get_num_letters

def get_book_text(book_file_path):
    with open(book_file_path) as file:
        file_contents = file.read()

    #print(file_contents)
    return file_contents

def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)

    print(f"Found {num_words} total words")
    letter_stats = get_num_letters(book)

    print(letter_stats)

main()
