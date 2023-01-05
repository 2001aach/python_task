# 3.Write a program to find the sum of all items in a list.[Using for loop]

list = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    list.append(numbers)
print(list)
print("Sum of items in a list is :", sum(list))


