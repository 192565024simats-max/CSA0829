try:
    N = int(input("Enter a positive"))

    if N <= 0:
        print("Please enter a positive whole number.")

    else:
        total_sum = (N * (N + 1)) // 2 
        print(f"The total sum is: {total_sum}")

except ValueError:
   print("That was not a valid number. Please try again with a whole number.")
