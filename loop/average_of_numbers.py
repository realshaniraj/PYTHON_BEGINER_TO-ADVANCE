n = int(input("enter total numbers: "))

total = 0

for i in range(n):
    num = int(input("enter number: "))
    total += num

average = total / n

print("average =", average)
