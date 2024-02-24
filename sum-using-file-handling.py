# Write a Python program that reads a list of numbers from a file named 
# "numbers.txt", calculates the sum of these numbers, and then writes the sum to another file named "sum.txt".
# Instructions:

#     Create a text file named "numbers.txt" and write some numbers (one number per line) in it.
#     Write a Python program that reads the numbers from "numbers.txt", calculates 
#     their sum, and then writes this sum to a new file named "sum.txt".
#     Run the Python program and verify that "sum.txt" contains the correct sum.

def calculate_sum(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
         numbers = [int(line.strip()) for line in f.readlines()]
         total_sum = sum(numbers)
        
        with open(output_file,'w') as f:
            f.write(str(total_sum))
        print("sum sucessfully written to",output_file)
    except FileNotFoundError:
       print("File not found")
input_file = "numbers.txt" 
output_file = "sum.txt"
calculate_sum(input_file , output_file)
