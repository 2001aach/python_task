# 4. Generate a list of four digit numbers in a given range with all their digits even and the
# number is a perfect square.


even_square_numbers = []

for num in range(1000, 10000):
    num_string = str(num)
    all_even = True
    for digit in num_string:
        if int(digit) % 2 != 0:
            all_even = False
            break
    if all_even:
        sqrt = int(num ** 0.5)
        if sqrt ** 2 == num:
            even_square_numbers.append(num)
print(even_square_numbers)




