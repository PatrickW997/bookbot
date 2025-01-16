with open("books/frankenstein.txt") as f:
    count=0
    file_contents = f.read()
    words=file_contents.split()
    chars=str(words).lower()
    letters={}

    for char in chars:
        letters[char]+= 1
print(letters)
