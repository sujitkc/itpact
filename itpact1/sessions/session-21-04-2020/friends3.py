n = int(input("Enter the number of contributions: "))

i = 0
contribution = []
while(i < n):
  contri = int(input("Enter the contribution from the friend number " + 
    str(i + 1) + ": "))
  contribution.append(contri)
  i += 1

total = 0
i = 0
while(i < len(contribution)):
  total += contribution[i]
  i += 1

print("total = ", total)

average = total / len(contribution)

print("average = ", average)

i = 0
while(i < len(contribution)):
  print("friend number " + str(i + 1) + " will pay " + str(average - contribution[i]) + ".")
  i += 1
