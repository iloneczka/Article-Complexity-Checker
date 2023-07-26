import pytest
from article_complexity_checker import calculate_average_word_length

def test_calculate_average_word_length_simple_text():
    text = "This is a simple test."
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 3.4

def test_calculate_average_word_length_empty_text():
    text = ""
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 0.0

def test_calculate_average_word_length_only_punctuation():
    text = "!@#$%^&*()"
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 0.0

def test_calculate_average_word_length_with_numeric_values():
    text = "The price is $20."
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 3.3

def test_calculate_average_word_length_multiple_spaces():
    text = "This      text    has   multiple  spaces."
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 5.0

def test_calculate_average_word_length_single_word():
    text = "Hello"
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 5.0

def test_calculate_average_word_length_special_characters():
    text = "This text has @#$! special characters *&^."
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 5.6

def test_calculate_average_word_length_with_numeric_words():
    text = "The price is $20. The answer is 42."
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 3.5

def test_calculate_average_word_length_with_only_numeric_words():
    text = "123 456 789"
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 0.0

def test_calculate_average_word_length_with_mixed_words():
    text = "This text contains 123 numeric 456 words."
    average_length = calculate_average_word_length(text)
    assert round(average_length, 1) == 5.6
