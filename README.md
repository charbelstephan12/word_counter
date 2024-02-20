# Word Counter

## Overview
The Word Counter is a simple tool designed to count the number of words in text files within a specified directory. This tool is useful for developers, writers, and anyone who needs to quickly analyze the word count of their textual content.

## Features
- Counts the total number of words in each text file within a specified directory.
- Supports various text file formats (e.g., .txt, .md).
- Provides a summary report with the total word count for the entire directory.

## Requirements
- Python 3.x

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/charbelstephan12/word_counter.git
   ```
2. Optionally, create a virtual environment to manage dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   # OR
   venv\Scripts\activate      # For Windows
   ```
4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Word Counter script, specifying the directory containing the text files you want to analyze:
   ```bash
   python word_counter.py /path/to/your/directory
   ```
2. View the generated report to see the word count statistics.

## Example
Suppose you have a directory named "documents" containing multiple text files:

```
documents/
├── document1.txt
├── document2.md
└── document3.txt
```

To count the words in all text files within the "documents" directory, run the following command:
```bash
python word_counter.py documents
```
