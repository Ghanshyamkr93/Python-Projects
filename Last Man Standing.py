a=input('Enter a number: ') #last man standing puzzle

a=int(a)
b=bin(a)
c= b[:2]+b[3:]+b[2]
c=int(c,2)

print ("Last Man standing in the circle is: ",c)
