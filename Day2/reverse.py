print("Enter The Number ")
no=int(input())
temp=no
rev=0
while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
print("The Reversed Number is ",rev)

print("Also Checking The Number Is palindrome Or Not.............")
print("Answer IS :")
if (no == rev):
    print(end="The Number is palindrome")
else:
    print("....................not palindrome................")


#with The help of indexing
number=[1,4,8,9][::-1]

print("reversed Number is ",number)