def chop(choplist):
  del choplist[0]
  del choplist[-1]

def middle(middlelist):
  return(middlelist[1:-1])

choplist = [1,2,3,4,5,6]
middlelist = [1,2,3,4,5,6]

print("choplist before chopping:", choplist)
chop(choplist)
print("choplist after chopping", choplist)

print("middlelist before middle():", middlelist)
print("middle of middlelist:", middle(middlelist))
print("middlelist after middle():", middlelist)