import string 

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_char = char_count(text)
    report(num_words, num_char, book_path)
    

def char_count(text):
    """Returns a count of the number of character instances
        from the provided text.  

    Args:
        text (string): The context of a text document.P

    Returns:
        dict: returns a dictionary key = char, 
            value = and int value of instances.
    """
    chars = [*text.lower()]     # Creates a list in which each element is a single char in lowercase
    letters = list(string.ascii_lowercase)      # Creates a list of all letters in alphabet
    count_dict = {letter: 0 for letter in letters}      # Constructs a dict where key = letter, value = 0
    count = 0
    
    """ Loop which iterates through the characters within chars and for every occurrance of that
        char within the text, it increments the count. Finally, it adds the count to the corresponding
        letter in count_dict. """ 
           
    for char in chars:
        if char in count_dict:
            count_dict[char] += 1
    
    return count_dict 
    
def word_count(text):
    """Returns a word count from the provided text.  

    Args:
        text (string): The context of a text document.

    Returns:
        int: returns the word count.
    """
    # Splits the text into a list where each element is a word
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

def report(num_words, num_char, book_path):
    """Function prints a report on the provided text. Outputs num of words and the num of instances for each char.

    Args:
        num_words (int): Number of words within the provided text
        num_char (dict): A dictionary where key = character & value = num of instances within text
        book_path (string): The path to the provide text
    """
    
    print(f"--- Report on {book_path} ---")
    print(f"{num_words} words found in the document.")
    
    for char, count in num_char.items():
        print(f"The '{char}' character was found {count} times.")
        
main()
