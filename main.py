def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    num_words = get_num_words(file_contents)
    chars_dict = get_chars_dict(file_contents)

    chars_list = [{'name': char, 'num': count} for char, count in chars_dict.items()]
    chars_list.sort(reverse=True, key=sort_on)

    print_report(chars_list, num_words)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_chars_dict(file_contents):
    letters = {}
    for char in file_contents:
        char = char.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def print_report(chars_list, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")
    for char_dict in chars_list:
        # For special characters, we might want to make them more visible
        if char_dict["name"].isalpha():
            char_name = char_dict["name"]
            print(f"The '{char_name}' character was found {char_dict["num"]} times")
    print("--- End report ---")

def sort_on(char_dict):
    return char_dict["num"]
main()