cp = float(input("Enter cost price: "))

student = input("Are you a student? (yes/no): ")

if student == "yes":
    if cp > 500:
        discount = cp * 10 / 100
    else:
        discount = cp * 5 / 100
else:
    if cp > 500:
        discount = cp * 8 / 100
    else:
        discount = cp * 2 / 100

final_price = cp - discount

print("discount=", discount)
print("final_Price", final_price)