def word_count(text):
    words = text.split()
    return len(words)

def char_count(letter_dic, text):
    letter_dic_copy = letter_dic.copy()
    lower_text = text.lower()

    for char in lower_text:
        if char.isalpha():
            if char in letter_dic_copy:
                letter_dic_copy[char] += 1
            else:
                letter_dic_copy[char] = 1
    return letter_dic_copy

def print_letter_counts(letter_dic):
    for letter, count in letter_dic.items():
        print(f"'{letter}': {count}")