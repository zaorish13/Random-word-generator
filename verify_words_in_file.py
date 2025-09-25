import os

# Function to verifiy if the words in day file already exist
def verify_words_in_file(directory, words):
    all_used_words = []
    
    # Loop through all file in the directory
    for fname in os.listdir(directory):
        if fname.startswith("words_of_the_day_") and fname.endswith('.txt'):
            with open(os.path.join(directory, fname), 'r') as file:
                used_words = file.read().splitlines()
                all_used_words.extend(used_words)
                print(f'Loaded {len(used_words)} words from {fname}')
                print(f'All used words so far: {len(all_used_words)}')
                print(all_used_words)
    # Compare today;s words with all previously used words
    new_words = []
    for word in words:
        if word in all_used_words:
            print(f'The word "{word}" has already been used.')
        else:
            print(f'The word "{word}" is new and will be added')
            new_words.append(word)
            
    return new_words