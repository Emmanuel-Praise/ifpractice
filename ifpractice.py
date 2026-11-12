def get_marks():
    return int(input("Enter Score: "))


score = get_marks()

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 65:
    grade = "C+"
elif score >= 50:
    grade = "D"
elif score >= 40:
    grade = "E"
else:
    grade = "F"

print("Grade =", grade)
