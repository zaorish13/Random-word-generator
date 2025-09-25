# function to write the displayed words to a new file
def write_words_to_file(file_path, words):
    # Write a list of words to a file
    with open(file_path, 'w') as file:
        # Write each word on a new line
        file.write('\n'. join(words))
        
    print(f'Words have been written to {file_path}')