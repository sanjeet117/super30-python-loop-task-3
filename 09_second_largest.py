# Find the second-largest number in a list without using sort().
transactions = [1200, 450, 800, 1500, 2300, 700, 100]

largest = None
second_largest = None

for txn in transactions:
    if largest is None or txn > largest:
        second_largest = largest
        largest = txn
    elif txn != largest and (second_largest is None or txn > second_largest):
        second_largest = txn

print(f"The largest is: {largest}, The second largest is: {second_largest}")
