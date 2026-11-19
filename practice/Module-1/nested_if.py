a = int(input("Enter Subject 1 marks: "))
b = int(input("Enter Subject 2 marks: "))
c = int(input("Enter Subject 3 marks: "))
d = int(input("Enter Subject 4 marks: "))

total = a + b + c + d

pr = total / 4

print("Total Marks:", total)
print("Percentage:", pr, "%")

if a >= 40 and b >= 40 and c >= 40 and d >= 40:

    if pr >= 70:
        print("Result: Distinction")
    elif pr >= 60:
        print("Result: First Class")
    elif pr >= 50:
        print("Result: Second Class")
    elif pr >= 35:
        print("Result: Pass")
    else:
        print("Result: Fail")

else:
    print("Result: Fail")