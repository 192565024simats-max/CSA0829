from itertools import permutations

s = input("Enter a string: ")

count = 0
for p in permutations(s):
    print("".join(p))
    count += 1

print("Total number of permutations:", count)
