list1=[]
x=int(input("enter a number to find it's binary: "))
while x>0:
    y=x%2
    list1.append(y)     #the remainders are appended to a list which will be used later
    x=x//2
length=len(list1)
#print(list1,length)

binary=0
for i in range(-1,(-length-1),-1):#reads the list backwards to generate the binary    or    list1.reverse() can be used and the for loop can have range from 0 to len(list1)
    binary=(binary*10)+list1[i]

print("binary:",binary)
