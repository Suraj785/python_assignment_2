list1 = [5, 7, 9, 14, 10, 20, 4]


def minimum(list1):
  minimum = list1[0]
  for each in list1:
    if each < minimum:
      minimum = each
    else:
      continue
  return minimum


print("Minimum is : ", minimum(list1))
