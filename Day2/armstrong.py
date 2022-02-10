print("Enter The Number ")
no=int(input())
temp=no
rev=0
while(temp>0):
    digit=temp%10
    rev=rev+digit*digit*digit
    temp=temp//10

if (no == rev):
    print(end="The Number is Armstrong")
else:
    print("....................not Armstrong................")

