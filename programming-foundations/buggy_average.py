# buggy_average.py
# Author : Kylie Estonanto, BSCS 1-1
# Purpose: Debugged quiz-average program.

count = 1
total = 0
while count <= 3:
       score = float(input("Enter score: "))
       total = total + score
       count += 1

average = total / 3
if average >= 75:
      print("PASSED")
else:
      print("FAILED")

print(f"Average:{average}")
