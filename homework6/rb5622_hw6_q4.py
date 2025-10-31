from DoublyLinkedList import DoublyLinkedList


def copy_linked_list(lnk_lst):
    copied_lst = DoublyLinkedList()
    for data in lnk_lst:
        copied_lst.add_last(data)
    return copied_lst

def deep_copy_linked_list(lnk_lst):
    copied_lst = DoublyLinkedList()
    for data in lnk_lst:
        if isinstance(data, DoublyLinkedList):
            copied_lst.add_last(deep_copy_linked_list(data))
        else:
            copied_lst.add_last(data)
    return copied_lst

lnk_lst = DoublyLinkedList()
copy = deep_copy_linked_list(lnk_lst)
print(copy)