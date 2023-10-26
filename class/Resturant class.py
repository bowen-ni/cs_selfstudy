from datetime import datetime, time

class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return("{} menu available from {} to {}".format(self.name,self.start_time.strftime("%I:%M %p"),self.end_time.strftime("%I:%M %p")))

  def calculate_bill(self,purchase_items):
    total_price = 0
    for i in purchase_items:
      total_price += self.items[i]
    return(total_price)

class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return("the address of resturant is at {}".format(self.address))

  def available_menus(self,time):
    menu_list = []
    for i in self.menus:
      if i.start_time <= time <= i.end_time:
        menu_list.append(i.name)
    if menu_list == []:
      return("there is no available menu in {} at {}".format(self.address,time.strftime("%I:%M %p")))
    return(menu_list)


#initiate for menu class:
brunch = Menu("brunch",{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
  'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},time(11),time(16))

early_bird = Menu("early_bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
  'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,},time(15),time(18))

dinner = Menu("dinner",{
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
  'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,},time(17),time(23))

kids = Menu("kids",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00},time(11),time(21))



#initiate for franchise class:
flagship_store = Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
new_installment = Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])


#test for menu class:
print(brunch,early_bird,dinner,kids)
print(brunch.calculate_bill(["pancakes","home fries","coffee"]))
print(early_bird.calculate_bill(["salumeria plate","mushroom ravioli (vegan)"]))

#test for franchise class:
print(flagship_store.menus)
print(new_installment)

print(new_installment.available_menus(time(12)))
print(new_installment.available_menus(time(18)))
print(new_installment.available_menus(time(3)))


def main():
  # 打印欢迎信息
  print("欢迎来到我们的餐厅！")

  # 让用户选择餐厅
  restaurants = [flagship_store, new_installment]
  for index, restaurant in enumerate(restaurants, start=1):
    print(f"{index}. {restaurant}")
  restaurant_choice = input("请选择您要就餐的餐厅（输入数字）：")

  # 检查用户输入，确保其有效
  while not restaurant_choice.isdigit() or not 1 <= int(restaurant_choice) <= len(restaurants):
    print("无效的输入，请重新输入！")
    restaurant_choice = input("请选择您要就餐的餐厅（输入数字）：")

  chosen_restaurant = restaurants[int(restaurant_choice) - 1]

  # 让用户选择就餐时间
  time_input = input("请输入您的就餐时间（HH:MM AM/PM）：")
  dining_time = datetime.strptime(time_input, "%I:%M %p").time()

  # 显示该时间可用的菜单
  available_menus = chosen_restaurant.available_menus(dining_time)
  print("此时可选的菜单有：", available_menus)

  # 用户选择菜品
  total_bill = 0
  while True:
    menu_name = input("请输入您要点菜的菜单名，如果想要结账，请输入'结账'：")
    if menu_name == '结账':
      break

    # 找到用户选择的菜单
    chosen_menu = None
    for menu in chosen_restaurant.menus:
      if menu.name == menu_name:
        chosen_menu = menu
        break

    if not chosen_menu:
      print("无效的菜单名，请重新输入！")
      continue

    # 显示菜单中的菜品
    print("该菜单中有以下菜品：")
    for item, price in chosen_menu.items.items():
      print(f"{item}: {price}$")

    # 用户选择菜品
    dish_name = input("请输入您要点的菜品名：")
    while dish_name not in chosen_menu.items:
      print("无效的菜品名，请重新输入！")
      dish_name = input("请输入您要点的菜品名：")

    # 计算总账单
    total_bill += chosen_menu.calculate_bill([dish_name])
    print(f"您现在的总账单为：{total_bill}$")

  # 用户结账
  print(f"您的最终账单为：{total_bill}$，欢迎下次光临！")


# 运行main函数
if __name__ == "__main__":
  main()
