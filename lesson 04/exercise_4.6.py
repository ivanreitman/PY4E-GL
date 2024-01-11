def computepay(hours, rate):
  pay = hours * rate
  if(hours > 40):
    pay = pay + 0.5 * rate * (hours - 40)
  return pay

hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
  hours = float(hours)
  rate = float(rate)
except:
  print("Please enter a number for hours or rate.")
  quit()

print("Pay", computepay(hours,rate))