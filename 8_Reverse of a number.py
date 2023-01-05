# 8. Write a program to print the reverse of a number. [use while loop]


number = int(input("Enter thenumber: "))
revers_number = 0
while (number > 0):
    remainder = number % 10
    revers_number = (revers_number * 10) + remainder
    number = number // 10
print("The reverse number is : {}".format(revers_number))