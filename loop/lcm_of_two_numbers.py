a = int(input("enter first number: "))
b = int(input("enter second number: "))

lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print("LCM =", lcm)
