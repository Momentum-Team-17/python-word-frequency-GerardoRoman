STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def open_file(file):
    '''Uses `open` to read a text file'''
    with open(file) as opened_file:
        # file remains open for the indented lines under here
        read_file = opened_file.read()
        word_list = read_file.split()
        print(word_list)


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # use `open` to read a text file 
    open_file(file)


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
