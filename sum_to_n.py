# sum_to_n.py
# Author : Kylie Estonanto, BSCS 1-1
# Purpose: Sums the numbers from 1 to n.

n = int(input("Enter a positive whole number: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum of 1 to {n} = {total}")