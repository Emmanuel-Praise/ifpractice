def get_marks():
    return int(input("Enter Score: "))


score = get_marks()

if not 0 <= score <= 100:
    print("Score must be between 0 and 100.")
elif score >= 90:
    grade, remark = "A+", "Outstanding"
elif score >= 80:
    grade, remark = "A", "Excellent"
elif score >= 70:
    grade, remark = "B", "Very Good"
elif score >= 65:
    grade, remark = "C+", "Good"
elif score >= 50:
    grade, remark = "D", "Satisfactory"
elif score >= 40:
    grade, remark = "E", "Needs Improvement"
else:
    grade, remark = "F", "Fail"

if 0 <= score <= 100:
    print("Grade =", grade)
    print("Remark =", remark)
