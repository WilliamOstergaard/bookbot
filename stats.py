def num_words(book_contents):
    word_list = book_contents.split()
    word_count = len(word_list)
    return word_count

def count_characters(book_contents):
    lowered_txt = book_contents.lower()
    char_counts = {}
    for char in lowered_txt:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(items):
    return items["num"]

def sorted_character_count(char_counts):
    final_list = []
    for char in char_counts:
        new_dict = {"char": char, "num": char_counts[char]}
        final_list.append(new_dict)

    return sorted(final_list, reverse=True,key=sort_on)
    