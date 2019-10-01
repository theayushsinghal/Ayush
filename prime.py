a=int(input("enter a number"))
flag=0
for i in range(2,a):
    if (a%i==0):
        flag=1
    
if(flag==0):
    print("number is prime")
else:
    print("number is not prime")
        
