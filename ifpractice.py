score = int(input("Enter Score: "))

if 50 <= score < 60:
    print("Grade = C")
elif 60 <= score < 70:
    print("Grade = B")
elif 70 <= score < 80:
    print("Grade = B+")
elif score >= 80:
    print("Grade = A")
else:
    print("Grade = D")