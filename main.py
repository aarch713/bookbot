from stats import get_book_char_count_list, get_book_text_len
import sys

def main():
    if not len(sys.argv) >= 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    
    text_len = get_book_text_len(path)
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    
    print(f'Found {text_len} total words')
    print('--------- Character Count -------')
    for item in get_book_char_count_list(path):
        print(item["char"] + ": " + str(item["num"]))

if __name__ == "__main__":
    main()