import sys
from stats import num_words, count_characters, sorted_character_count, sort_on

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_contents = get_book_text(file_path)
    result = count_characters(book_contents)
    sorted_result = sorted_character_count(result)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(book_contents)} total words")
    print("--------- Character Count -------")
    for char in sorted_result:
        if char["char"].isalpha() == True:
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

main()

