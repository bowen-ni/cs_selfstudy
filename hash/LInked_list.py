class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert(self, new_node):
        current_node = self.head_node

        if not current_node:
            self.head_node = new_node

        while (current_node):
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node = next_node

    def __iter__(self):
        current_node = self.head_node
        while (current_node):
            yield current_node.get_value()
            current_node = current_node.get_next_node()


#
# swap_node(my_list,7,5)
# print(my_list.stringify_list())
#
# print(nth_last_node(my_list, 2).value)
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

