# 1.Write a program to find the factorial of a number.

number=int(input("enter the number"))
factorial=1
if number<0:
    print("factorial does not exist")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("factorial of",number,"is:",factorial)
