def get_book_text(book_file_path):
    with open(book_file_path) as file:
        file_contents = file.read()

    #print(file_contents)
    return file_contents

def get_num_words(text_contents):
    words = text_contents.split()

    return len(words)

def main():
    book = get_book_text("./books/frankenstein.txt")
    
    num_words = get_num_words(book)

    print(f"Found {num_words} total words")

main()
