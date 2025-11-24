from stats import word_count, char_count, print_letter_counts # type: ignore

def get_book_text(file_path, encoding="utf-8"):
    with open(file_path, encoding="utf-8") as f:
        frankenstein = f.read()
        return frankenstein    


if __name__ == "__main__":
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    total_words = word_count(book_text)
    # print(f"Found {total_words} total words")
    letter_dic = {}
    letter_counts = char_count(letter_dic, book_text)
    print_letter_counts(letter_counts)
    # print(book_text[:500])  # Print the first 500 characters of the book text