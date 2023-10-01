def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    letters_count = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(letters_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_characters(text):
    #convert text to lower case to eliminate duplicates
    text = text.lower()
#  Initialize an empty dictionary to store the character counts
    char_count = {}

    for char in text:  # Loop through each character in the text
        if char.isalpha():   # Check if the character is a letter
            if char in char_count:      # If the character is already in the dictionary, increment its count by 1
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


main()



