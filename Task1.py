#for -1

a = input("enter the String :")
b =len(a)+1
for i in range(-1,-b,-1):
    print(a[i])
print()
print()

#for -2
a = input("Enter a String :")
b = len(a)-1
for i in range(b,-1,-1):
    print(a[i])

# by using while loop

a = input('Enter a String :')
b = len(a)
c = 0
while c < b :
    b = b-1
    print(a[b])