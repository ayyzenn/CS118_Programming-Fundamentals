#Write a program that examines three variables x , y , and z and prints the largest odd number among them.
#If none of them are odd, it should print a message to that effect.

x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
z=int(input("Enter the value of z: "))
a=0
b=0
c=0
print("The value of x is:",x)
print("The value of y is:",y)
print("The value of z is:",z)
if x % 2 !=0:
    a=x
if y % 2 !=0:
    b=y
if z % 2 !=0:
    c=z
if x % 2 == 0:
    print("x is not a odd number. ")
if y % 2 == 0:
    print("y is not a odd number. ")
if z % 2 == 0:
    print("z is not a odd number. ")
print("The maximum odd number is:",max(a,b,c))