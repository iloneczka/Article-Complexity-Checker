# Article Complexity Checker

## Table of contents
* [General info](#general-info)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Testing for Development](#testing-for-evelopment)
* [Solutions](#solutions)
* [Future Plans](#future-plans)
* [Inspirations and Acknowledgments](#inspirations-and-acknowledgments)

## General info

The "Article Complexity Checker" program calculates the complexity of articles and text posts, enabling journalists to parameterize their work and automatically determine whether they are writing simple and easy-to-understand texts. It calculates the average word length and displays the result.

## Features

- Calculate the average word length in the text.
- Remove punctuation marks from the text before calculating the average.
- Exclude words consisting solely of numbers from the calculation.

## Technologies Used

The program is written in Python.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Prerequisites

To run this project, make sure you have Python 3.11.2 installed on your computer.

## Setup

To run the project locally, follow these steps:

- Clone this repository to your local machine.
- Navigate to the project directory.
- Run the program:
```
python3 article_complexity_checker.py
```

## Testing for Development

To ensure the correctness of the `article_complexity_checker.py` module, we have created a test suite in `test_article_complexity_checker.py` using pytest. 
The test cases cover different scenarios to verify the `calculate_average_word_length()` and `remove_punctuation()` functions.

These tests will help ensure that the functions in `article_complexity_checker.py` work correctly and return the expected results. If any of the tests fail, it will help identify any issues that need to be addressed in the code.

### Running Tests
To run the tests, follow these steps:

1. Install pytest if you haven't already, by:
``` 
pip3 install pytest
```
2. Navigate to the project directory.

3. Run the tests by running the following command in the terminal:
```
pytest test_article_complexity_checker.py
```


## Solutions

### Issues and Resolutions:

#### Removing Punctuation

There was an issue with removing punctuation marks from the text. The original implementation used a loop to replace each punctuation mark with an empty string. The solution was to use the `str.replace()` method instead of a loop, which is more efficient.

```python
def remove_punctuation(text: str) -> str:
    cleaned_text = text
    for char in PUNCTUATION:
        cleaned_text = cleaned_text.replace(char, "")
    return cleaned_text
```

## Future Plans

- Implement the ability to calculate other text statistics, such as the average sentence length, the number of unique words, etc.
- Create a user interface for inputting and analyzing multiple articles at once.
- Support various languages and character sets.

## Inspirations and Acknowledgments

The program was adapted during the "Practical Python" training course. Thanks for the inspiring material and support!
