import sys
from stats import get_num_words
from stats import get_num_letters
from stats import sort_chars

def get_book_text(book_file_path):
    with open(book_file_path) as file:
        file_contents = file.read()

##    #print(file_contents)
    return file_contents

def main():
    print("============ BOOKBOT ============")
# Old method of hardcoding txt document path
#    book = get_book_text("./books/frankenstein.txt")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.ext(1)

    book = get_book_text(sys.argv[1])
    
    print(f"Analyzing book found at {sys.argv[1]}...")
    num_words = get_num_words(book)
    print("----------- Word Count ----------")

    print(f"Found {num_words} total words")
    letter_stats = get_num_letters(book)

##    print(letter_stats)

    print("--------- Character Count -------")
    letter_ranks = sort_chars(letter_stats)
    for letter in letter_ranks:
        print(f"{letter["char"]}: {letter["num"]}")


main()
