
# input year
year=int(input("Enter an Year"))

if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print("The Given Year is a leap Year ")
else:
    print("The Given Yaer is not an Leap Year")
