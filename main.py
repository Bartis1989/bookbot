def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    characters = character_count(text)
    sorted_dict = sort_dict(characters)
    report = create_report(sorted_dict, book_path, words)
    #print(text)
   # print(words)
    #print(characters)
    print(report)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count (text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_text = text.lower()
    character_dict = {}
    for char in lower_text:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict


def sort_dict(dict):
    sorted_dict = {}
    dict_to_list = list(dict.items())
    for tuple in dict_to_list:        
        if tuple[0].isalpha() == True:
            sorted_dict[tuple[0]] = tuple[1]
    sorted_dict = sorted(sorted_dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_dict
    
def create_report(list, book_path, words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for tuple in list:
        print(f"The '{tuple[0]}' character was found {tuple[1]} times")
    print("--- End report ---")
    
    
main()