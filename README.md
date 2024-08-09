# Text Summarization Application

## Overview

This application is a simple text summarizer that uses natural language processing (NLP) techniques to extract the most important sentences from a given text. The summarized version provides a concise overview of the original content by focusing on the key information.

## Features

- **Text Cleaning:** The input text is cleaned by removing unwanted spaces, numbers, punctuation, and converting all text to lowercase.
- **Word Frequency Calculation:** The application calculates the frequency of each word, ignoring common stopwords (e.g., "the", "and", "is").
- **Sentence Scoring:** Each sentence is scored based on the word frequencies, and the sentences with the highest scores are selected for the summary.
- **Summarization:** The application generates a summary by selecting the top `n` sentences with the highest scores.

## Requirements

- Python 3.x
- NLTK library

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required Python libraries:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the NLTK data:**

   Before running the script, make sure to download the necessary NLTK data by running:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage

1. **Prepare the Input Text:**

   Save the text you want to summarize in a file named `sample.txt` in the same directory as the script.

2. **Running the Script:**

   The script can be executed from the command line or any Python environment. Here's an example of how to run it:

   ```bash
   python app.py
   ```

3. **Sample Input File:**

   - Ensure the input text is saved in `sample.txt`.

4. **Output:**

   The script will print the original text and the summarized text. You can control the length of the summary by changing the value of `n` in the `summarize_text` function.

   ```python
   summary = summarize_text(sample_text, n=2)
   ```

## Example

- **Original Text:**

   The content of `sample.txt` will be processed by the script.

- **Summarized Text:**

   The summarized text will be printed based on the content in `sample.txt`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

**Vishu Vaishnav**
