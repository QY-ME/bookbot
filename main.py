def main ():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)

    print(f"{num_words} words found in the document")

def get_book_text (path_to_file):
    with open(path_to_file) as f: 
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

main()
