hours = input("Enter hours: ")
rate = input("Enter rate: ")
overtime = 0
if float(hours) > 40:
  overtime = float(hours) - 40
  hours =  40
pay = float(hours) * float(rate) + overtime * 1.5 * float(rate)
print(pay)