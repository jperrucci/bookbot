def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = get_sliced_dict(chars_dict)
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document")
    print("")
    for char in chars_list:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_sliced_dict(dict):
    chars_list = []
    for char in dict:
        if char.isalpha() == True:
            chars_list.append({"char": char, "count": dict[char]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


def sort_on(dict):
    return dict["count"]


main()