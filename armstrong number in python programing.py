num=int(input("enter the value"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if num==sum:
    print("iits an armstrong number")
else:
    print("its not an above number")
