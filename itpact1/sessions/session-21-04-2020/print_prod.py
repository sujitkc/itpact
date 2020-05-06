lst = [34, 32, 687, 1, 34, 90, 78]

product = 1
i = 0
while(i < len(lst)):
  product *= lst[i]
  i += 1

# 1 * lst[0] * lst[1] * ... * lst[n] where n = len(lst) - 1.
print("product = ", product)
