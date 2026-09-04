# Accept 10 numbers from the user and store them in a list using a loop.
numbers = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

print("Collected numbers:", numbers)
