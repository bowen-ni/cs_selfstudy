class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

def swap_node(linked_list, val1, val2):
    prev1, curr1, prev2, curr2 = None, None, None, None

    current = linked_list.head_node
    previous = None

    while current:
        if current.value == val1:
            curr1,prev1 = current,previous
        elif current.value == val2:
            curr2, prev2 = current,previous
        previous = current
        current = current.next_node

    if prev1 == None:
        linked_list.head_node = curr2
    else:
        prev1.next_node = curr2

    if prev2 == None:
        linked_list.head_node = curr1
    else:
        prev2.next_node = curr1

        stock_node = curr1.next_node
        curr1.next_node = curr2.next_node
        curr2.next_node = stock_node

def nth_last_node(linked_list, n):
  current = None
  tail_seeker = linked_list.head_node
  count = 0
  while tail_seeker:
    tail_seeker = tail_seeker.get_next_node()
    count += 1
    if count >= n+1:
      if current is None:
        current = linked_list.head_node
      else:
        current = current.get_next_node()
  return current

my_list = LinkedList()
my_list.insert_beginning(5)
my_list.insert_beginning(1)
my_list.insert_beginning(3)
my_list.insert_beginning(12)
my_list.insert_beginning(7)

print("Linked List:")
print(my_list.stringify_list())

swap_node(my_list,7,5)
print(my_list.stringify_list())

print(nth_last_node(my_list, 2).value)
    # def swap_node(self,val1,val2):
    #     current_node = self.head_node
    #     if val1 == self.head_node.value:
    #         while current_node.next_node:
    #             if current_node.next_node.value == val2:
    #                 self.head_node.next_node = current_node.next_node.next_node
    #                 swap_node = self.head_node
    #                 self.head_node = current_node.next_node
    #                 current_node.next_node = swap_node
    #             current_node = current_node.next_node
    #     if val2 == self.head_node.value:
    #         while current_node.next_node:
    #             if current_node.next_node.value == val1:
    #                 self.head_node.next_node = current_node.next_node.next_node
    #                 swap_node = self.head_node
    #                 self.head_node = current_node.next_node
    #                 current_node.next_node = swap_node




# def main():
#     # 创建一个新的链表
#     my_list = LinkedList()
#
#     # 向链表中添加节点
#     my_list.insert_beginning(5)
#     my_list.insert_beginning(4)
#     my_list.insert_beginning(3)
#     my_list.insert_beginning(2)
#     my_list.insert_beginning(1)
#
#     print("Linked List:")
#     print(my_list.stringify_list())
#
#     # 删除中间节点
#     value_to_remove = 3
#     my_list.remove_node(value_to_remove)
#     print(f"Linked List after removing {value_to_remove}:")
#     print(my_list.stringify_list())
#
#     # 删除头节点
#     value_to_remove = 1
#     my_list.remove_node(value_to_remove)
#     print(f"Linked List after removing {value_to_remove}:")
#     print(my_list.stringify_list())
#
#     # 删除尾节点
#     value_to_remove = 5
#     my_list.remove_node(value_to_remove)
#     print(f"Linked List after removing {value_to_remove}:")
#     print(my_list.stringify_list())
#
#     # 创建多个不同的链表对象
#     list1 = LinkedList()
#     list1.insert_beginning(1)
#     list1.insert_beginning(2)
#
#     list2 = LinkedList()
#     list2.insert_beginning(3)
#     list2.insert_beginning(4)
#
#     print("Linked List 1:")
#     print(list1.stringify_list())
#
#     print("Linked List 2:")
#     print(list2.stringify_list())
#
# if __name__ == "__main__":
#     main()

