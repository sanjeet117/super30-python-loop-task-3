# Calculate total transaction value without using sum().
transactions = [1200, 450, 800, 1500, 2300, 700, 100]

total = 0
for txn in transactions:
    total += txn

print(f"The total is: {total}")
