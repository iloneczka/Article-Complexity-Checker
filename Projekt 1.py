"""
BBC Article Complexity Checker

This program calculates the complexity of articles and posts, allowing journalists to parameterize their work
and automatically determine whether they are writing simple and easy-to-understand texts.
It calculates the average word length and displays the result.

Usage:
1. Run the program.
2. Enter the text to be analyzed.
3. The program will display the average word length of the given text.
"""

import string

PUNCTUATION = string.punctuation

def remove_punctuation(text: str) -> str:
    """
    Remove punctuation marks from the text.

    Parameters:
    - text (str): The text to process.

    Returns:
    - str: The text without punctuation marks.
    """
    cleaned_text = text
    for char in PUNCTUATION:
        cleaned_text = cleaned_text.replace(char, "")
    return cleaned_text

def calculate_average_word_length(text: str) -> float:
    """
    Calculate the average word length in the text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    - float: The average word length.
    """
    words = remove_punctuation(text).split()
    words_without_numbers = [w for w in words if not w.isnumeric()]
    words_lengths = [len(w) for w in words_without_numbers]
    average_word_length = sum(words_lengths) / len(words_lengths)
    return average_word_length

def main() -> None:
    """
    The main function of the program.

    Prompts the user to enter text, calculates the average word length,
    and displays the result.
    """
    user_text = input("Write your text: ")

    average_length = calculate_average_word_length(user_text)
    print("The average word length of the given text is:", average_length)

if __name__ == "__main__":
    main()
    