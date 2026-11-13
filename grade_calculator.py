# grade_calculator.py
# Author : Kylie Estonanto, BSCS 1-1
# Purpose: Computes the midterm rating.

lab = float(input("Laboratory grade: "))
lecture = float(input("Lecture grade: "))
rating = lab * 0.65 + lecture * 0.35
print(f"Midterm rating: {rating:.2f}")
