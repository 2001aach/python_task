# 5.Write a program using a for loop to print the multiplication table of n, where n is entered
# by the user

num = int(input('Enter the number'))
for i in range(1, 11):
   print(num, '*', i, '=', num*i)
