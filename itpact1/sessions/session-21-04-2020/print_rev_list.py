lst = [34, 32, 687, 1, 34, 90, 78]
'''
78
90
34
1
...
34

i    j
-------
0    6
1    5
2    4
3    3
4    2
5    1
6    0

'''
# Efficient: saves resources
# Resources: time, material, energy, memory.
# Effectiveness: Ability to achieve result with better quality.
# Reverse the list
i = 0
while(i < len(lst)):
  # easier to read ---> more readable
  j = len(lst) - 1 - i
  print(lst[j])
  i += 1


# 1 nanosecond = 0.000000001 sec.
# 1 / 1000000000 sec
