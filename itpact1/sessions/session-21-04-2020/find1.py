lst = [23, 56, 21, 67, 78, 24, 1, 56]

x = int(input("Enter the value to be searched: "))
i = 0
found = False # crossmark
while(i < len(lst)):
  print("Loop")
  if(lst[i] == x):
    found = True # checkmark
    break
  i += 1

print(found)
