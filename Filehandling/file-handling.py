# Write a Python program that reads a text file named
# "input.txt", counts the number of words in the file, and then writes
# the count to another file named "word_count.txt".
# Instructions:

#     Create a text file named "input.txt" and write some text in it.
#     Write a Python program that reads the contents of "input.txt", counts the number of words,
#     and then writes this count to a new file named "word_count.txt".
#     Run the Python program and verify that "word_count.txt" contains the correct word count.

def word_counts(input_file, output_file):
    try:
        with open(input_file,'r') as f:
          text = f.read() 
          count_words = len(text.split())
        

        with open(output_file,'w') as f:
            f.write(str(count_words))
    
    except FileNotFoundError:
        print("File not found")
input_file = "input.txt"
output_file = "count_word.txt"
word_counts(input_file, output_file)

