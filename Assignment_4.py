# Task 2: Sum of Integers from starting number from user to users ending number 
# Taje input from user how much sum he want
S_num = int(input("Enter starting number for sum  "))

E_num = int(input("Enter ending number for sum  "))
# Initialize sum
total_sum = 0

# Use for loop to iterate from 1 to 50
for i in range( S_num, E_num):
    total_sum += i

# Display the final sum
print('The sum of integers from starting to ending is:',total_sum)
