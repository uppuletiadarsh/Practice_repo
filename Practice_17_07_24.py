"""# find() 
sentence = 'Python is Difficult To Learn And Difficult To Code'
res = sentence.find("p") # if substring not in mainstring it will give -1 instead of error
res1= sentence.find("P")
print(res)
print(res1)

for i in sentence:
    a = sentence.find(i)
    print("The element :",i,"The Index Value Of First Occurance",a)
    

#rfind()----------------------------------------------------------------------
sen = "Hello Python World This is Adarsh"
b = sen.rfind("H")
c = sen.rfind("Z") #not in string
print(b)
print(c)

#index()-------------------------------------------------------------------------
sen = "Hello Python World This is Adarsh"
z = sen.index("H")
print(z)
#c = sen.index("Z") #it gives an error
for i in sen:
    c = sen.index(i)
    print("The Element is :",i,"The INdex is :",c)

#rindex()---------------------------------------------------------------------------
sen = "Hello Python World This is Adarsh"
b = sen.rindex("W")
print(b)
#b = sen.rindex("w") #error

#count()------------------------------------------------------------------------------
sen = "Hello Python World This is Adarsh  I was Trained In Python Fullstack In Python"
a = sen.count("a")
b = sen.count("h")
print(a)
print(b)
#-----------------------------------------------------------------------------------------------
for i in sen:
    b = sen.count(i)
    print("The Element :",i,"The No Of Occurances :",b)

#split()--------------------------------------------------------------------------------------
sen1= "Hello Python World This is Adarsh  I was Trained In Python Fullstack In Python"
sen2= "Hello ,Python World, This is Adarsh , I was Trained ,In Python ,Fullstack In Python"
sen3= "Hello Python World This# is Adarsh # I was Trained In #Python Fullstack In Python"
sen5= "Hello Python World This is @Adarsh  I was Trained In Python@ Fullstack In Python"

a = sen1.split()
b= sen2.split(",")
c = sen3.split("#")
d = sen5.split("@")
e = sen1.split('h')
res =[a,b,c,d,e]
for i in res:
    print("The Result List :",i)
########------------------------------------------------------------------------------------------
count = 0
for word in a:
    if word in sen1:
        count=count+1
        print(word,": The Count :",count)


#replace()--------------------------------------------------------------------------------------
sen1= "Hello Python World This is Adarsh  I was Trained In Python Fullstack In Python"
new_sen = sen1.replace('Python',"Java")
new_sen1 = sen1.replace(' ',"-")

print(new_sen)
print(new_sen1)
print()

old = "Python"
new = "Java"
words = sen1.split()
list1 = []
for word in words:
    if word == old:
        list1.append(new)
    else:
        list1.append(word)

new_sentence = " ".join(list1)
print("Org Sentence:",sen1)
print()
print("new Sentence:",new_sentence)


#join()-----------------------------------------------------------------------------------------
sen2 = "Hello ,Python World, This is Adarsh , I was Trained ,In Python ,Fullstack In Python"
splt  = sen2.split(",")
join = "-".join(splt)
print(join)
splt2= sen2.split(" ")
join2 = "==".join(splt2)
print(join2)

#upper-----------------------------------------------------------------------------------------------
a = "Hello ,Python World, This is Adarsh , I was Trained ,In Python ,Fullstack In Python"
b = a.upper()
print(b)
#lower------------------------------------------------------------------------------------------------
a = "Hello ,Python World, This is Adarsh , I was Trained ,In Python ,Fullstack In Python"
b = a.lower()
print(b)
#swapcase()---------------------------------------------------------------------------------------
a = "Hello ,Python World, This is Adarsh , I was Trained ,In Python ,Fullstack In Python"
b = a.swapcase()
print(b)
#title()-------------------------------------------------------------------------------------------
a = "hello ,python world, this is adarsh , i was trained ,in python ,fullstack in python"
b = a.title()
print(b)

#capitalize()---------------------------------------------------------------------------------------
a = "hello ,python world, this is adarsh , i was trained ,in python ,fullstack in python"
b = a.capitalize()
print(b)

#startswith()-------------------------------------------------------------------------------------
a = "WWW.GOOGLE.COM"
b = a.startswith("WWW")
c = a.startswith("DDD")
d = a.endswith(".COM")
e = a.endswith("MMM")
res = [b,c,d,e]
for i in res :
    print(i)

number = input("Enter a number :")
if len(number)==13:
    if (number.startswith('+91')):
        print("Indian Number")
    elif(number.startswith('+11')):
        print("USA Number")
    elif(number.startswith('+44')):
        print("Uk Number")
    elif (number.startswith('+61')):
        print("Aus Number")
    else:
        print("Invalid Number")
else:
    print("Ivalid Number")

#endswith()-------------------------------------------------------------------------
url = input("Enter A website Url :")
if (url.endswith(".com") and url.startswith("www")):
    print("It Is a Proper Website Url")
else:
    print("Invalid website Url")
#--------------------------------------------------------------------------------------
strg = input("Enter a string :")
if (strg[0].isupper()):
    print("The total Converted To Uppercase: ",strg.upper())
else:
    print("The total Converted To lowercase: ",strg.lower())




"""
#53
a = 'abababcacadcadef'
b =''
for i in a :
    if i not in b:
        b=b+i
print(b)      



    