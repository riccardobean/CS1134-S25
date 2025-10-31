from DoublyLinkedList import DoublyLinkedList


class Integer:
    def __init__(self, num_str):
        self.dll = DoublyLinkedList()
        index = 0
        while num_str[index] == "0" and index < len(num_str) - 1:
            index += 1
        for val in range(index, len(num_str)):
            self.dll.add_last(int(num_str[val]))

    def __str__(self):
        ret_str = ""
        for val in self.dll:
            ret_str += str(val)
        return ret_str

    def __add__(self, other):
        added = ""
        cursor_self = self.dll.trailer.prev
        cursor_other = other.dll.trailer.prev
        carryover = 0
        while cursor_self is not self.dll.header and cursor_other is not other.dll.header:
            addition = cursor_self.data + cursor_other.data + carryover
            carryover = addition // 10
            remaining = addition % 10
            added += str(remaining)
            cursor_self = cursor_self.prev
            cursor_other = cursor_other.prev
        while cursor_self is not self.dll.header:
            addition = cursor_self.data + carryover
            carryover = addition // 10
            remaining = addition % 10
            added += str(remaining)
            cursor_self = cursor_self.prev
        while cursor_other is not other.dll.header:
            addition = cursor_other.data + carryover
            carryover = addition // 10
            remaining = addition % 10
            added += str(remaining)
            cursor_other = cursor_other.prev
        if carryover != 0:
            added += str(carryover)
        added = added[::-1]
        return Integer(added)

    def __mul__(self, other):
        added = []
        cursor_self = self.dll.trailer.prev
        cursor_other = other.dll.trailer.prev
        carryover = 0
        tailing_zeros = 0
        while cursor_other is not other.dll.header:
            multiplied = "0" * tailing_zeros
            while cursor_self is not self.dll.header:
                product = cursor_self.data * cursor_other.data + carryover
                carryover = product // 10
                remaining = product % 10
                multiplied += str(remaining)
                cursor_self = cursor_self.prev
            if carryover != 0:
                multiplied += str(carryover)
            carryover = 0
            multiplied = multiplied[::-1]
            added.append(Integer(multiplied))
            cursor_other = cursor_other.prev
            cursor_self = self.dll.trailer.prev
            tailing_zeros += 1
        result = Integer("0")
        for integer in added:
            result += integer
        return result


in1 = Integer("1")
print(in1 * 0)
