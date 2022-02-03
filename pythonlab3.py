def swap(x,y):
    print('Before swapping a:',x)
    print('Before swapping b:',y)

    x,y = y,x
    return x,y

a = input('Enter a number:')
b = input('Enter a number:')
c,d= swap(a,b)

print('After swapping a becomes:',c)
print('After swapping b becomes:',d)



