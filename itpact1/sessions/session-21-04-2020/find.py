lst = [23, 1, 567,33,566,33,678]

n = int(input("Enter the number to find: "))

i = 0
found = False
while(i < len(lst)):
  if(n == lst[i]):
    found = True
    break
  else:
    i += 1

print(found)
