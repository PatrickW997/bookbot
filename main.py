def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    num_words = get_num_words(file_contents)
    chars_dict = get_chars_dict(file_contents)

    sorted_chars_dict = sorted(chars_dict.items(), key=lambda x: x[1], reverse=False)
    print(chars_dict)
    print("---------")
    print(sorted_chars_dict)
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

main()