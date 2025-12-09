numbers=list(map(int,input("enter numbers separated by space:").split()))
numbers.sort()
mean=sum(numbers)/len(numbers)
n=len(numbers)
if n%2==0:
    median=(numbers[n//2-1]+numbers[n//2])/2
else:
    median=numbers[n//2]
mode=max(numbers,key=numbers.count)    

print("median=",median)
print("mode=",mode)
print("mean=",mean)
    
