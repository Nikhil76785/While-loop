number = int(input("Please enter a number: "))
sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if (number == sum):
    print(f"{number} is an armstrong number.")

else:
    print(f"{number} is not an armstrong number.")