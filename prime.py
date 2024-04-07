num = int(input("Enter the number ="))
count = 0
for i in range(1,num):
    if num % i == 0:
        count+=1
if count==1:
    print("Its a Prime number")
else:
    print("Its not a Prime number")
    