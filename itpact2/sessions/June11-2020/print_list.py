# Write a program that prints all elements of a list in the same order.

fruits = ['orange', 'pineapple', 'apple', 'mango', 'blackberry', 'grapes', 'leechy', 'guava', 'strawberry', 'watermelon']

# for each of the fruits in the fruits list print that fruit.

'''
count = 0
while(count < len(fruits)):
  fruit = fruits[count]
  print(fruit)
  count += 1
'''

for fruit in fruits:
  print(fruit)

print ("********")

for i in range(len(fruits)):
  print(fruits[i])
