# number_list = [10,20,30,45,50,89,78,85]
# avg = sum(number_list)/len(number_list)
# print("The average is ", round(avg,2))


user_str=input("Enter The String")
spi=user_str.split()
d={}
for i in spi:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)