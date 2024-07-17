"""# by using replace
a = "How Are You Adarsh Are You Ok ?"
b = a.replace(" ",'')

print(b)  # the out put is : HowAreYouAdarshAreYouOk?
#------------------------------------------------------------------
#by split and join
a = "How Are You Adarsh Are You Ok ?"
b = a.split(" ")
c = "".join(b)
print(c)

#---------------------------------------------------------
a = "How Are You Adarsh Are You Ok ?"
b = ''
for i in a:
    if i !=" ":
        b = b+i
print(b)"""

a = "How Are You Adarsh Are You Ok ?"
b = ''
c = 0
while (c < len(a)):
    if (a[c]!=''):
        b = b+a[c]
    c = c+1
print(b)

 





