# Read words from files
# Use random library to display random words from the files
import random
from datetime import datetime
import os


# Get the current date
day = datetime.now().strftime("%d")
month = datetime.now().strftime("%m")
year = datetime.now().strftime("%Y")

# Get the date in the format day_month_year
day_month_year = day + "_" + month + "_" + year
print("Today's date is: ", day_month_year)


# Ask user the number of how many words to display
number_of_words_to_display = int(input("Input the number of words you want to display: "))

# function to read words from files
def read_words_from_files(file_path, count):
    # Read words from the file and store them in a list
    words_list = []
    
    # using with for opening the file
    with open(file_path, 'r') as file:
        
        # Saved all the words from the file splited by space
        all_words = file.read().split()
        
        # Loop to display the number of words inputed by the user
        for _ in range(count):
                        
            # Displey a random word from the list
            words = random.choice(all_words)
            # Insert in the list the displayed word
            words_list.append(words)
    return words_list

# function to write the displayed words to a new file
def write_words_to_file(file_path, words):
    # Write a list of words to a file
    with open(file_path, 'w') as file:
        # Write each word on a new line
        file.write('\n'. join(words))
        
    print(f'Words have been written to {file_path}')
     

# Read words from the file
returned_words = read_words_from_files('words.txt', number_of_words_to_display) 

# Define the output filename with the current date
filename = f'words_of_the_day_{day_month_year}.txt'

# Get the directory of the curent script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Full path to the new file created
output_path = os.path.join(script_directory, filename)

# Write words to the files
write_words_to_file(output_path, returned_words)

# Print the words selected
print("Displayed words:\n",'\n'.join(map(str, returned_words)))         
    