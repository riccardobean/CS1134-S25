from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(sorted_list, pointer1, pointer2):
        if pointer1 is srt_lnk_lst1.trailer and pointer2 is srt_lnk_lst2.trailer:
            return sorted_list
        if pointer1 is srt_lnk_lst1.trailer:
            sorted_list.add_last(pointer2.data)
            return merge_sublists(sorted_list, pointer1, pointer2.next)
        if pointer2 is srt_lnk_lst2.trailer:
            sorted_list.add_last(pointer1.data)
            return merge_sublists(sorted_list, pointer1.next, pointer2)
        if pointer1.data <= pointer2.data:
            sorted_list.add_last(pointer1.data)
            return merge_sublists(sorted_list, pointer1.next, pointer2)
        else:
            sorted_list.add_last(pointer2.data)
            return merge_sublists(sorted_list, pointer1, pointer2.next)

    sorted_list = DoublyLinkedList()
    return merge_sublists(sorted_list, srt_lnk_lst1.header.next, srt_lnk_lst2.header.next)
