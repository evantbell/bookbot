
def main():
    with open("books/frankenstein.txt") as f:
        #do stuff
        file_contents = f.read()
        print("file length is", len(file_contents))
        print("number of words is", len(file_contents.split()))

        char_dict = []
        char_dict = list(get_char_counts(file_contents))
        print("unsorted: ",char_dict)

        char_dict.sort(reverse=True, key=sort_on)
        print("sorted: ",char_dict)

def get_char_counts(text):
    low_text = text.lower()
    char_count = {}

    for char in low_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict


if __name__ == "__main__":
    main()