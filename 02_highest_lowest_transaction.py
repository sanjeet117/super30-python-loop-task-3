# Find highest and lowest transaction without using max() and min().
transactions = [1200, 450, 800, 1500, 2300, 700, 100]

highest = transactions[0]
lowest = transactions[0]

for txn in transactions:
    if txn > highest:
        highest = txn
    if txn < lowest:
        lowest = txn

print(f"The highest is: {highest}")
print(f"The Lowest is: {lowest}")
