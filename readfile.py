f = open('hii.txt','r')
data = f.readlines()
count = 0
for lines in data:
    print(lines)
    count += 1
print ('total number of lines:',count)

import os
file_size = os.path.getsize("hii.txt")
print("\nThe size of hii.txt is :",file_size,"Bytes")

