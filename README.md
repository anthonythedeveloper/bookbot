#Bookbot

This Python script processes a text file and generates a report detailing the total word count and the frequency of each character in the file. The analysis focuses on alphabetic characters and is case-insensitive.

---

## Features

1. **Word Counting**: Calculates the total number of words in the text file.
2. **Character Frequency Analysis**: Counts the occurrence of each alphabetic character (ignoring case).
3. **Report Generation**: Outputs a readable report with:
   - Total word count.
   - Frequency of each alphabetic character in descending order.

---

## Prerequisites

- Python 3.x installed on your system.
- A text file located at `books/frankenstein.txt` for analysis.

---

## How to Use

1. **Prepare the Text File**:
   - Ensure the `books/frankenstein.txt` file exists and contains the text you want to analyze.

2. **Run the Script**:
   - Execute the script by running the following command in your terminal:
     ```bash
     python script_name.py
     ```

3. **View the Report**:
   - The script will generate a report in the terminal, displaying:
     - The total word count.
     - The frequency of each character in descending order.

---

## Code Breakdown

### Functions

1. **`main()`**:
   - Reads the file `books/frankenstein.txt`.
   - Calls helper functions to count words and characters.
   - Prints the final report.

2. **`word_counting(text)`**:
   - Splits the text into words and returns the total count.

3. **`downsizer(text)`**:
   - Counts the frequency of each alphabetic character (case-insensitive).
   - Ignores non-alphabetic characters.

4. **`print_report(character_count, word_count)`**:
   - Generates a formatted report of the word count and character frequencies.

---

## Example Output

If the file contains the text:

```
"It was a dark and stormy night."
```

The output will look like:

```
--- Begin report of books/frankenstein.txt ---
7 words found in the document

The 'a' character was found 5 times
The 't' character was found 4 times
The 's' character was found 3 times
The 'd' character was found 2 times
The 'r' character was found 2 times
The 'k' character was found 1 time
The 'n' character was found 1 time
The 'm' character was found 1 time
The 'y' character was found 1 time
The 'i' character was found 1 time
The 'g' character was found 1 time
The 'h' character was found 1 time

--- End report ---
```

---

## Customization

- Modify the file path in the `open` statement to analyze a different file:
  ```python
  with open("path/to/your/file.txt") as f:
  ```
- Customize the sorting or filtering logic in `print_report()` as needed.

---

## License

This script is free to use and modify. Feel free to adapt it for your own projects!
