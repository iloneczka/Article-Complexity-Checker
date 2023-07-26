# Article Complexity Checker

## Description

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

## Installation

To run the project locally, follow these steps:

- Clone this repository to your local machine.
- Navigate to the project directory.
- Run the program:
```
python article_complexity_checker.py
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
## Tools and Plugins

The program uses the standard Python library and does not require any additional tools or plugins.

## Reusable Parts of the Project

The project does not feature specific reusable parts as it is relatively small and focused on a single task - calculating the average word length.

## Future Insights / Project Development Plans

- Implement the ability to calculate other text statistics, such as the average sentence length, the number of unique words, etc.
- Create a user interface for inputting and analyzing multiple articles at once.
- Support various languages and character sets.

## Inspirations and Acknowledgments

The program was adapted during the "Practical Python" training course. Thanks for the inspiring material and support!
