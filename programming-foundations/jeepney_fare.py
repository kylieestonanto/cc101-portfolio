# jeepney_fare.py
# Author : Kylie Estonanto, BSCS 1-1
# Purpose: Computes the jeepney fare with discount.

distance = int(input("Distance (km): "))
discount = input("Discount? (Y or N): ").strip().upper()

if distance <= 4:
    fare = 13.00
else:
    fare = 13.00 + (distance - 4) * 1.80

if discount == "Y":
    fare = fare * 0.80

print(f"Fare: PHP {fare:.2f}")