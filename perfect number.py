num=int(input("enter the number "))
sum_of_divisors=0
for i in range(1,num):
    if num % i==0:
        sum_of_divisors+=i


if sum_of_divisors==num:
    print(num,"is a perfect number")
else:
        print(num,"its is not an perfect number")
