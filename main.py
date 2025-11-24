from stats import word_count, char_count, print_letter_counts, sort_letter_counts, print_sorted_letter_counts # type: ignore
import sys

def get_book_text(file_path, encoding="utf-8"):
    with open(file_path, encoding="utf-8") as f:
        frankenstein = f.read()
        return frankenstein    


if __name__ == "__main__":
    # print(sys.argv)
    file_path = "books\\frankenstein.txt"
    
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # print(
    #     "============ BOOKBOT ============\n"
    #     "Analyzing book found at books/frankenstein.txt...\n"
    #     "----------- Word Count ----------"
    # )
    book_text = get_book_text(file_path)
    total_words = word_count(book_text)
    print(f"Found {total_words} total words")
    
    # print("--------- Character Count ----------")
    letter_dic = {}
    letter_counts = char_count(letter_dic, book_text)
    sorted_letter_counts = sort_letter_counts(letter_counts)
    # print_letter_counts(letter_counts)
    print_sorted_letter_counts(sorted_letter_counts)
    # print("============= END ===============")
    # print(book_text[:500])  # Print the first 500 characters of the book text