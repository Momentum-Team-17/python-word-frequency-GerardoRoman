import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def remove_punctuation(words):
    stripped_file = words.translate(str.maketrans('', '', string.punctuation))
    return stripped_file


def remove_stop_words(word_list):
    cleaned_list = []
    for word in word_list:
        if word not in STOP_WORDS:
            cleaned_list.append(word)
    return cleaned_list


def open_file(file):
    '''Uses `open` to read a text file'''
    with open(file) as opened_file:
        # file remains open for the indented lines under here
        read_file = opened_file.read()
        # remove punctuation
        stripped_file = remove_punctuation(read_file).lower()
        word_list = stripped_file.split()
        cleaned_list = remove_stop_words(word_list)
        # print(cleaned_list)
        return cleaned_list


def sort_dictionary(dictionary):
    sorted_word_count_by_frequency = sorted(
        dictionary.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_word_count_by_frequency)
    return sorted_word_count_by_frequency


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # use `open` to read a text file 
    words_to_count = open_file(file)
    word_count = {}
    for word in words_to_count:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_dictionary = sort_dictionary(word_count)
    print(sorted_dictionary)
    return sorted_dictionary


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
