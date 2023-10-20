#first method
def find_min(my_list):
  if not my_list:
    return None
  if len(my_list) == 1:
    return my_list[0]
  for i in range(len(my_list)):
    if my_list[i] <= find_min(my_list[(i+1):]):
      return my_list[i]


#second method
# def find_min(my_list, min = None):
#   if not my_list:
#     return min
#
#   if not min or my_list[0] < min:
#     min = my_list[0]
#   return find_min(my_list[1:], min)
#
# print(find_min([13, 72, 19, 5, 86]))
