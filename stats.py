
def word_count(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):
    char_dict={}
    chars = list(book_text.lower())
    for c in chars:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict

def sort_on(items):
    return items("num")

def sorted_dict(char_dict):
    list_dicts=[]
    for char in char_dict:
        list_dicts.append({"name": char, "num": char_dict[char]})
    list_dicts.sort(reverse=True, key=lambda item:item["num"])
    return list_dicts
#    print(list_dicts)
#    list_dicts.sort(reverse=True, key=sort_on)
#    print(list_dicts)