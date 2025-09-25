**************
Random Word Generator (Daily)

A simple Python script that reads words from a text file and generates a set of random words each day.  
The generated words are also saved into a new file named with the current date (e.g., `words_of_the_day_23_09_2025.txt`).

**************
Features
- Reads words from a given file (`words.txt`)
- Lets the user choose how many random words to generate
- Ensures words are unique across all generated files (no repeats on different days)
- Saves the generated words into a file with the current date in its name
- Code is split into separate modules for clarity:
   - read_words_from_file.py → function to read random words
   - verify_words_in_file.py → function to check if words were already used
   - write_words_to_file.py → function to write new words to today’s file
   - random_word_generator.py → main script that ties everything together

**************
Requirements
- Python 3.7+ (tested on Python 3.10+)

No external libraries are required (only Python’s built-in modules are used).


**************
Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/zaorish13/random-word-generator.git
   cd random-word-generator
