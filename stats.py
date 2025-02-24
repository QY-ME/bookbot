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

def sort_on(dict):
    return list(dict.values())[0]

def sorted_char_count (symbol_count):
    char_list = []
    for char, count in symbol_count.items():
        char_list.append({char: count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

 