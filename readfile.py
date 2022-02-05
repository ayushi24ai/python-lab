f = open('hii.txt','r')
data = f.readlines()
count = 0
for lines in data:
    print(lines)
    count += 1
print ('total number of lines:',count)

