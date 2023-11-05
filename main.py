def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    num_letters = get_num_per_letter(text)
    #print(num_letters)
    print_a_report(num_letters)

def get_num_words(text):
    words = text.split()
    return len(words)

def print_a_report(dic):
    alphabet = []
    for c in dic:
        if c.isalpha():
            alphabet.append(c)
    alphabet.sort()
    for l in range(0,len(alphabet)):
        print(f"The '{alphabet[l]}' character was found {dic[alphabet[l]]} times")


def get_num_per_letter(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()