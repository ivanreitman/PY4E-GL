def computegrade(score):
  if score >= 0.9:
    return("A")
  elif score >= 0.8:
    return("B")
  elif score >= 0.7:
    return("C")
  elif score >= 0.6:
    return("D")
  elif score >= 0:
    return("F")
  else:
    return("Bad score")

score = input("Enter score: ")

try:
  score = float(score)
except:
  score = -1

print(computegrade(score))