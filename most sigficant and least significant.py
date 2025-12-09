num=int(input("enter the number"))
num=abs(num)
isd=num%10
while num>=10:
    num//=10
msd=num
print("most significant digit:",msd)
print("least significant digit:",isd)
