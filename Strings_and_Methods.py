""""
a = input('Enter a String :')
for b in range(0,len(a)-1):
    print(a[b]," : The Index Values is :",b)

# the end Char
a = "12345667899"
for i in a:
    print(i,end=' ')

#String Concatenationn
a = "Adarsh"
b = "Uppuleti"
print(a+" "+b)

#String Repetition

a = "Adarsh"
b = a*3
print(b)

#upper and lower
a = "Adarsh"
b = a.lower()
c = a.upper()
print(b)
print(c)

#strip
a = "    Hello Adarsh   "
b= a.strip()
print(b)

#replace
a = "Adarsh Avinesh Adarsh anil anvesh Adarsh"
b = a.replace('Adarsh',"Abhi")
print(b)

#split
a = "Adarsh Avinesh Adarsh anil anvesh Adarsh"
b = "Adarsh,Avinesh Adarsh,anil anvesh,Adarsh"
c = a.split(" ")
d = b.split(",")
print(c)
print(d)

#startswith and ends with
a = "Adarsh Avinesh Adarsh anil anvesh Adarsh"
b = a.startswith("Adarsh")
c = a.endswith("Abhi")
print(b)
print(c)

#find and index ()
a = "ABCDEFGHIJKLM"
b = a.find("D")
c = a.find("Z") # if not occur returns -1 instead of error
print(b)
print(c)

#index
a = "ABCDEFGHIJKLM"
b = a.index('D')
c = a.index("Z") # if its not found it will gives an error
print(b)
print(c)

#count
a = "AAA DD DD AA FF GG HH JJ"
b = a.count("A") # count the element no of times occured in the string
print(b)"""

"""# in and not in
a = "AAA DD DD AA FF GG HH JJ"
b = "A" in a
c = "A" not in a
d = "Z" in a 
e = "Z" not in a
print(b)
print(c)
print(d)
print(e)
"""
a = "ab"

print(a.upper())





