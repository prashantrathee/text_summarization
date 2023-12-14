Text Summarization Project
==========================

Overview
--------

This Python project, named "text\_summarization," aims to provide a simple and effective text summarization solution. The core functionality is implemented in the `Summarize.py` module, where a class named `Summarizer` is defined. This class is responsible for summarizing a given text file and returning the result.

Project Structure
-----------------

*   **text\_summarization/**
    *   **main.py**: The main script to execute the text summarization.
    *   **Summarize.py**: The module containing the `Summarizer` class.
    *   **text.txt**: A sample text file for testing the summarization.

Getting Started
---------------

git clone https://github.com/your-username/text_summarization.git
Navigate to the project directory:


**Usage**
**To use the text summarization functionality in your main.py script, follow these steps:**

1. Import the Summarizer class: from Summarize import Summarize
2. Instantiate the class with text file : summarizer = Summarize(text)
3. Print summary : print(summarizer.summarize())
