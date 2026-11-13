# even_odd.py
# Author : Kylie Estonanto, BSCS 1-1
# Purpose: Tells whether a number is even or odd.

n = int(input("Enter a whole number: "))

if n % 2 == 0:
    print(f"{n} is even.")
else:
    print(f"{n} is odd.")