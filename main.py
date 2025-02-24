from stats import get_num_words
from stats import get_char_count

def main ():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    num_char = get_char_count(text)

    print(f"{num_words} words found in the document")
    for char in num_char:
        print(f"{char}: {num_char[char]}")

def get_book_text (path_to_file):
    with open(path_to_file) as f: 
        return f.read()



main()
