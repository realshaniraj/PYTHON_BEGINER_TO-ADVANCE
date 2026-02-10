n = int(input("enter number: "))

product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n = n // 10

print("product of digits =", product)
