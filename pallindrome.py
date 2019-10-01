num=int(input("enter number"))
num2=num
rev=0
print("num=",num)
while(num!=0):
    digit=num%10
    print(digit)
    rev=(rev*10)+ digit
    num=num//10
print(rev)
if(rev==num2):
    print("number is pallindrome")
else:
    print("number is not pallindrome")
    
