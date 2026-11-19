a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a < b:
    if a < c:
        print("A is min")
    else:
        print("C is mix")
else:
    if b < c:
        print("B is max")
    else:
        print("C is min")