# Write a program that prints all elements of a list in reverse order.

lst = [4, 5, 2, 7, 9]

count = len(lst) - 1
i = 0
while(count >= 0):
  element = lst[count]
  print(element)
  print(i)
  i += 1
#  count -= 1 # count = count - 1
