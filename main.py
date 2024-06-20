def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_char = char_count(text)
    print(f"{num_words} words found in the document")

def num_char(text):
    """Returns a count of the number of character instances
        from the provided text.  

    Args:
        text (string): The context of a text document.

    Returns:
        dict: returns a dictionary key = char, 
            value = and int value of instances.
    """
    
    
    
def word_count(text):
    """Returns a word count from the provided text.  

    Args:
        text (string): The context of a text document.

    Returns:
        int: returns the word count.
    """
    words = text.split()
    return len(words)


def get_book_text(path):
    """Fetches the contents of a text file located at path.

    Args:
        path (string): relative path of the text.

    Returns:
        string: returns the content of file in path.
    """
    with open(path) as f:
        return f.read()


main()