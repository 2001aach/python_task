# 9. Write a program to find whether the given number is an Amstrong number or not. [use
# while loop]


num = int(input("Enter a number: "))
sum = 0
n1 = len(str(num))
print(n1)
temp = num

while temp > 0:
   digit = temp % 10
   sum += digit ** n1
   temp //= 10

if num == sum:
   print(num,"is an Amstrong number")
else:
   print(num,"is not an Amstrong number")