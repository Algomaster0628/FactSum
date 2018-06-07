def fact(num): # Returns sum of factorials till n.
  if num > 1:
     factorial = num*fact(num-1)
  elif num == 1 or num == 0:
      return 1
  return factorial

def FactSum(n):
  mylist = []
  for nums in range(n):
    mylist.append(nums)
  sumup = 0
  for digit in mylist:
    sumup += fact(digit)
  return sumup


x = FactSum(21)
print(x)
