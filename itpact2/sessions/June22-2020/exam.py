marks = [
  [3,   5, 5, 0],
  [2.5, 3, 5, 4],
  [2.5, 0, 5, 5],
  [4,   4, 4, 0],
  [2,   3, 3, 0],
  [5,   4, 5, 0],
  [3,   0, 3, 2],
  [0,   3, 0, 0],
  [2,   6, 0, 0],
  [2.5, 0, 5, 4],
  [0,   0, 0, 6]
]

# Compute the total marks earned by each of the students.

for row in marks:
#  mysum = 0
#  for n in row:
#    mysum += n
  print("total = ", sum(row))

# Compute the average marks for each of the four questions.

# Extract the first element of each of the rows (lists).
for i in range(len(marks[0])):
  Q_i = []
  for row in marks:
    Q_i.append(row[i])

  print(Q_i)

  average_i = sum(Q_i)/len(Q_i)

  print("Average marks in Q_i = ", average_i)
