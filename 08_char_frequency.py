# Count frequency of every character in a string without using Counter.
text = "Sanjeet"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(f"{char} -> {count}")
