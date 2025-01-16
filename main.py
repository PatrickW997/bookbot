def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    num_words = get_num_words(file_contents)
    chars_dict = get_chars_dict(file_contents)

    sorted_chars_dict = sorted(chars_dict.items(), key=lambda x: x[1], reverse=False)
    print_report(sorted_chars_dict)
    print(f"Number of words: {num_words}")

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

def print_report(chars_dict):
    print("--- Character Counts Report ---")
    for char, count in chars_dict:
        # For special characters, we might want to make them more visible
        if char.isspace():
            char_name = "SPACE"
        elif char == '\n':
            char_name = "NEWLINE"
        else:
            char_name = char
        print(f"The '{char_name}' character appears {count} times")

main()