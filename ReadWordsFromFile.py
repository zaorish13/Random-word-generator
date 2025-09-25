import random

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