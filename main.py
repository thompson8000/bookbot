def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

import sys
from stats import word_count 
from stats import char_count
from stats import sorted_dict

def main():
    #print(sys.argv)
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>") 
       sys.exit(1)
    location = sys.argv[1]
    #printout = get_book_text("books/frankenstein.txt")
    printout = get_book_text(location)
    num_words = word_count(printout)
    char_dictionary = char_count(printout)
    output = f"Found {num_words} total words"
    sorted = sorted_dict(char_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {location}...")
    print("----------- Word Count ----------")
    print(output)
    print("--------- Character Count -------")
    for i in sorted:
        char = i["name"]
        count = i["num"]    
        if char.isalpha():
            print(f"{char}: {count}")


    print("============= END ===============")
    #print(char_dictionary)

main()