with open('hii.txt') as f:
    text = f.read().splitlines()
print(text)

lines = len(text)
words = sum(len(line.split())for line in text)
characters = sum(len(line)for line in text)
files_size_in_bytes = characters + (lines)*2
print (lines)
print (words)
print (characters)
print (files_size_in_bytes)

import os
file_size = os.path.getsize("hii.txt")
print("\nThe size of hii.txt is :",file_size,"Bytes")

