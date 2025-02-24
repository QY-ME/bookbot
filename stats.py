def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lowercase = text.lower()
    symbols_count = {}
    for symbols in lowercase:
        if symbols in symbols_count:
            symbols_count[symbols] += 1
        else:
            symbols_count[symbols] = 1
    return symbols_count