num = input("Enter a number: ")

count = 0
for ch in num:
    if ch >= '0' and ch <= '9':
        count = count + 1

print("Total digits:", count)
