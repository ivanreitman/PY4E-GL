hours = input("Enter hours: ")
rate = input("Enter rate: ")
overtime = 0
try:
  hours = float(hours)
  rate = float(rate)
  if float(hours) > 40:
    overtime = float(hours) - 40
    hours =  40
  pay = float(hours) * float(rate) + overtime * 1.5 * float(rate)
  print(pay)
except:
  print("Please enter a number for hours or rate.")

# worked example uses quit() to skip the rest of the program if the input is not valid