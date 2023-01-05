# 6.Display the given pyramid with the step number accepted from the user.


num = int(input("Enter the row"))
for i in range(num+1):
    for j in range(1, i + 1):
        print(i*j, end=" ")
    print("")

    