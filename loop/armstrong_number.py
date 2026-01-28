n = int(input("enter number: "))
temp = n
total = 0

while n > 0:
    digit = n % 10
    total += digit ** 3
    n = n // 10

if total == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
