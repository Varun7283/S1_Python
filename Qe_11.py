a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
c=int(input("enter the number c:"))
if(a>b):
    if(a>c):
        print("a is greater")
elif(b>a):
    if(b>c):
        print("b is greater")
    else:
        print("c is greater")