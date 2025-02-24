import sys 
from stats import get_num_words
from stats import get_char_count
from stats import sorted_char_count

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]

    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    num_char = get_char_count(text)
    sorted_chars = sorted_char_count(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text (path_to_file):
    with open(path_to_file) as f: 
        return f.read()


main()
