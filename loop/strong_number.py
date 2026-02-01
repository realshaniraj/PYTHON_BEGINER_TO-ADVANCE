n = int(input("enter number: "))
temp = n
total = 0

while n > 0:
    digit = n % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact
    n = n // 10

if total == temp:
    print("Strong number")
else:
    print("Not a strong number")
