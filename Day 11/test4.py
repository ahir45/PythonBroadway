hour = float(input("Enter the hour worked : "))
rate = float(input("Enter the base rate : "))
if hour <= 40:
    pay = hour * rate

else:
    ot = hour - 40
    normal_pay = hour * rate
    ot_pay = ot * rate * 1.5
    pay = normal_pay + ot_pay
print("payment = ", pay)

