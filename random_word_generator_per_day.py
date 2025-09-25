# Read words from files
# Use random library to display random words from the files
import os
from datetime import datetime
from ReadWordsFromFile import read_words_from_files
from WriteWordsToFile import write_words_to_file
from VerifyWordsInFile import verify_words_in_file


# Get the current date
day = datetime.now().strftime("%d")
month = datetime.now().strftime("%m")
year = datetime.now().strftime("%Y")

# Get the date in the format day_month_year
day_month_year = day + "_" + month + "_" + year
print("Today's date is: ", day_month_year)

# Get the current day of the week
day_of_week = datetime.now().strftime("%A")
print("Today is: ", day_of_week)


# Ask user the number of how many words to display
number_of_words_to_display = int(input("Input the number of words you want to display: "))

# Get the directory of the curent script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Read words from the file
returned_words = read_words_from_files('words.txt', number_of_words_to_display) 

# Define the output filename with the current date
filename = f'words_of_the_day_{day_month_year}.txt'

# Full path to the new file created
output_path = os.path.join(script_directory, filename)

# Verify words before writting ti new file
filltered_words = verify_words_in_file(script_directory, returned_words)

if filltered_words:
    # Write the words to a new file
    write_words_to_file(output_path, filltered_words)
    print(f'New words have been written to {output_path}')
    print(f"Displayed words: \n", '\n'.join(filltered_words))
else:
    print("No new words to write to the file.")
