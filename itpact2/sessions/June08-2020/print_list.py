# Write a program that prints all elements of a list in the same order.

fruits = [
 'orange',
 'pineapple',
 'apple',
 'mango',
 'blackberry',
 'grapes',
 'leechy',
 'guava',
 'strawberry',
 'watermelon'
]

count = 0
while(count < len(fruits)):
  fruit = fruits[count]
  print(fruit)
  count += 1
