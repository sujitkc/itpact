lst = [23, 56, 21, 67, 78, 24, 1, 56]

i = 0
m = lst[0]

while(i < len(lst)):
  # if the current element is greater than m then change m to the current element
  if(lst[i] > m):
    m = lst[i]
  i += 1

print("maximum value = ", m)
