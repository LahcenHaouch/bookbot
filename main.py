def main():
    file_path = "./books/frankenstein.txt"
    print_report(file_path)


def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
        return text

def get_words(text):
    return text.split()

def get_word_count(words):
    return len(words)

def get_char_dict(words):
    result = {}
    for char in words:
        lowercased_char = char.lower()

        if not lowercased_char.isalpha():
            continue

        if lowercased_char in result:
            result[lowercased_char] += 1
        else:
            result[lowercased_char] = 1
    return result

def get_sort_key(d):
    return d["count"]

def get_sorted_char_list(char_dict):
    sorted_char_list = []

    for char in char_dict:
        sorted_char_list.append({"char": char, "count": char_dict[char]})

    sorted_char_list.sort(reverse=True, key=get_sort_key)
    return sorted_char_list


def print_report(file_path):
    text = get_book_text(file_path)
    
    print(f"--- Begin report of {file_path} ---")
    
    words = get_words(text)
    word_count = get_word_count(words)
    
    print(f"{word_count} words found in the document")
    
    char_dict = get_char_dict(words)
    sorted_char_list = get_sorted_char_list(char_dict)
    
    for element in sorted_char_list:
        print(f"The '{element["char"]}' character was found {element["count"]} times")
    
    print("--- End report ---")

main()
