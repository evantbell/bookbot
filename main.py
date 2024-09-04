
def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        #do stuff
        file_contents = f.read()
        print("file length is", len(file_contents))
        print("number of words is", len(file_contents.split()))

        char_dict = []
        char_dict = get_char_counts(file_contents)
        sorted_char_dict = sort_dict(char_dict)

        print(f"--- Begin report of {book_path} ---")
        print()

        for item in sorted_char_dict:
            if not item["char"].isalpha():
                continue
            print(f"The '{item['char']}' character was found {item['num']} times")
        
        print("---- END OF REPORT ----")

def get_char_counts(text):
    low_text = text.lower()
    char_count = {}

    for char in low_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(d):
    return d["num"]

#sorts a dictionary on the key, descending order. Uses sort_on to return the index
def sort_dict(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


if __name__ == "__main__":
    main()