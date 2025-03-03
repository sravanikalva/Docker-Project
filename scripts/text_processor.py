import os
from collections import Counter
import socket
import re

# Function to read file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().lower()

# Function to count words
def count_words(text):
    words = text.split()
    return len(words), Counter(words)

# Function to handle contractions (split words like "can't" into "can" and "t")
def handle_contractions(text):
    contractions = re.sub(r"n't", ' not', text)
    contractions = re.sub(r"'re", ' are', contractions)
    contractions = re.sub(r"'ll", ' will', contractions)
    contractions = re.sub(r"'ve", ' have', contractions)
    contractions = re.sub(r"'m", ' am', contractions)
    contractions = re.sub(r"'s", ' is', contractions)
    contractions = re.sub(r"'d", ' had', contractions)
    
    words = re.findall(r'\b\w+\b', contractions)
    return len(words), Counter(words)

# ✅ Updated File Paths
file1 = '/home/data/IF-1.txt'  # Updated to match your file name
file2 = '/home/data/AlwaysRememberUsThisWay-1.txt'  # Updated file name

# Count words in each file
text1 = read_file(file1)
word_count1, freq_words1 = count_words(text1)

text2 = read_file(file2)
word_count2, freq_words2 = handle_contractions(text2)

# Grand total of words across both files
total_words = word_count1 + word_count2

# Top 3 frequent words in each file
top3_file1 = freq_words1.most_common(3)
top3_file2 = freq_words2.most_common(3)

# Get the container's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# ✅ Updated Output Path
output_path = '/home/data/output/result.txt'

# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write results to result.txt
with open(output_path, 'w') as result_file:
    result_file.write(f"Word count for IF-1.txt: {word_count1}\n")
    result_file.write(f"Word count for AlwaysRememberUsThisWay-1.txt: {word_count2}\n")
    result_file.write(f"Grand total of words: {total_words}\n")
    result_file.write(f"Top 3 words in IF-1.txt: {top3_file1}\n")
    result_file.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt: {top3_file2}\n")
    result_file.write(f"Container IP Address: {ip_address}\n")

# Print the contents of result.txt
with open(output_path, 'r') as file:
    print(file.read())
