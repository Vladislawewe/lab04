def count_common_elements(*lists):

 if not lists:
  return 0

 common_elements = set(lists[0])
 for lst in lists[1:]:
  common_elements.intersection_update(lst)
 return len(common_elements)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
result = count_common_elements(list1, list2, list3)
print("Количество одинаковых элементов:", result)