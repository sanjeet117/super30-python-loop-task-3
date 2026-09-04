# Find the average temperature of the given readings.
temperatures = [32, 35, 28, 40, 38, 31, 42]

total = 0
count = len(temperatures)

for temp in temperatures:
    total += temp

avg = total / count
print(f"The average is : {avg:.2f}")
