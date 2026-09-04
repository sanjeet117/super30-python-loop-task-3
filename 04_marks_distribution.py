# Count student mark distribution across different grade brackets.
marks = [78, 92, 45, 67, 88, 53, 99]

count_90_plus = 0
count_75_89 = 0
count_50_74 = 0
count_below_50 = 0

for mark in marks:
    if mark >= 90:
        count_90_plus += 1
    elif 75 <= mark <= 89:
        count_75_89 += 1
    elif 50 <= mark <= 74:
        count_50_74 += 1
    else:
        count_below_50 += 1

print(f"90+: {count_90_plus}")
print(f"75-89: {count_75_89}")
print(f"50+: {count_50_74}")
print(f"Below 50: {count_below_50}")
