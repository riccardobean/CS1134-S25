from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        if len(orig_str) == 0:
            raise Exception("String cannot be empty")
        self.dll = DoublyLinkedList()
        index = 0
        while index < len(orig_str):
            freq = 1
            char = orig_str[index]
            while index + 1 < len(orig_str) and orig_str[index] == orig_str[index + 1]:
                freq += 1
                index += 1
            self.dll.add_last((char, freq))
            index += 1

    def __add__(self, other):
        total = []
        cursor = self.dll.header.next
        while cursor.next is not self.dll.trailer:
            total.append(cursor.data)
            cursor = cursor.next
        self_last = self.dll.trailer.prev
        other_first = other.dll.header.next
        if self_last.data[0] == other_first.data[0]:
            char = self_last.data[0]
            freq = self_last.data[1] + other_first.data[1]
            total.append((char, freq))
        else:
            total.append(self_last.data)
            total.append(other_first.data)

        cursor = other_first.next
        while cursor is not other.dll.trailer:
            total.append(cursor.data)
            cursor = cursor.next

        new_str = ""
        for tpl in total:
            new_str += tpl[0]*tpl[1]
        return CompactString(new_str)


    def __lt__(self, other):
        self_node = self.dll.header.next
        other_node = other.dll.header.next

        self_char = self_node.data[0]
        self_freq = self_node.data[1]
        other_char = other_node.data[0]
        other_freq = other_node.data[1]

        while self_node is not self.dll.trailer and other_node is not other.dll.trailer:
            if self_char != other_char:
                return self_char < other_char
            if self_freq > other_freq:
                if other_node.next is not other.dll.trailer:
                    other_node = other_node.next
                    other_char = other_node.data[0]
                    other_freq = other_node.data[1]
                else:
                    return False
            elif self_freq < other_freq:
                if self_node.next is not self.dll.trailer:
                    self_node = self_node.next
                    self_char = self_node.data[0]
                    self_freq = self_node.data[1]
                else:
                    return True
            else:
                if self_node.next is self.dll.trailer and other_node.next is other.dll.trailer:
                    return False
                if self_node.next is self.dll.trailer and other_node.next is not other.dll.trailer:
                    return True
                if self_node.next is not self.dll.trailer and other_node.next is other.dll.trailer:
                    return False
                if self_node.next is not self.dll.trailer and other_node.next is not other.dll.trailer:
                    self_node = self_node.next
                    self_char = self_node.data[0]
                    self_freq = self_node.data[1]
                    other_node = other_node.next
                    other_char = other_node.data[0]
                    other_freq = other_node.data[1]


    def __le__(self, other):
        self_node = self.dll.header.next
        other_node = other.dll.header.next

        self_char = self_node.data[0]
        self_freq = self_node.data[1]
        other_char = other_node.data[0]
        other_freq = other_node.data[1]

        while self_node is not self.dll.trailer and other_node is not other.dll.trailer:
            if self_char != other_char:
                return self_char < other_char
            if self_freq > other_freq:
                if other_node.next is not other.dll.trailer:
                    other_node = other_node.next
                    other_char = other_node.data[0]
                    other_freq = other_node.data[1]
                else:
                    return False
            elif self_freq < other_freq:
                if self_node.next is not self.dll.trailer:
                    self_node = self_node.next
                    self_char = self_node.data[0]
                    self_freq = self_node.data[1]
                else:
                    return True
            else:
                if self_node.next is self.dll.trailer:
                    return True
                if self_node.next is not self.dll.trailer and other_node.next is other.dll.trailer:
                    return False
                if self_node.next is not self.dll.trailer and other_node.next is not other.dll.trailer:
                    self_node = self_node.next
                    self_char = self_node.data[0]
                    self_freq = self_node.data[1]
                    other_node = other_node.next
                    other_char = other_node.data[0]
                    other_freq = other_node.data[1]

    def __gt__(self, other):
        self_node = self.dll.header.next
        other_node = other.dll.header.next

        self_char = self_node.data[0]
        self_freq = self_node.data[1]
        other_char = other_node.data[0]
        other_freq = other_node.data[1]

        while self_node is not self.dll.trailer and other_node is not other.dll.trailer:
            if self_char != other_char:
                return self_char > other_char
            if self_freq > other_freq:
                if other_node.next is not other.dll.trailer:
                    other_node = other_node.next
                    other_char = other_node.data[0]
                    other_freq = other_node.data[1]
                else:
                    return True
            elif self_freq < other_freq:
                if self_node.next is not self.dll.trailer:
                    self_node = self_node.next
                    self_char = self_node.data[0]
                    self_freq = self_node.data[1]
                else:
                    return False
            else:
                if self_node.next is self.dll.trailer:
                    return False
                if self_node.next is not self.dll.trailer and other_node.next is other.dll.trailer:
                    return True
                if self_node.next is not self.dll.trailer and other_node.next is not other.dll.trailer:
                    self_node = self_node.next
                    self_char = self_node.data[0]
                    self_freq = self_node.data[1]
                    other_node = other_node.next
                    other_char = other_node.data[0]
                    other_freq = other_node.data[1]

    def __ge__(self, other):
        self_node = self.dll.header.next
        other_node = other.dll.header.next

        self_char = self_node.data[0]
        self_freq = self_node.data[1]
        other_char = other_node.data[0]
        other_freq = other_node.data[1]

        while self_node is not self.dll.trailer and other_node is not other.dll.trailer:
            if self_char != other_char:
                return self_char > other_char
            if self_freq > other_freq:
                if other_node.next is not other.dll.trailer:
                    other_node = other_node.next
                    other_char = other_node.data[0]
                    other_freq = other_node.data[1]
                else:
                    return True
            elif self_freq < other_freq:
                if self_node.next is not self.dll.trailer:
                    self_node = self_node.next
                    self_char = self_node.data[0]
                    self_freq = self_node.data[1]
                else:
                    return False
            else:
                if self_node.next is self.dll.trailer and other_node.next is not other.dll.trailer:
                    return False
                if self_node.next is self.dll.trailer and other_node.next is other.dll.trailer:
                    return True
                if self_node.next is not self.dll.trailer and other_node.next is other.dll.trailer:
                    return True
                if self_node.next is not self.dll.trailer and other_node.next is not other.dll.trailer:
                    self_node = self_node.next
                    self_char = self_node.data[0]
                    self_freq = self_node.data[1]
                    other_node = other_node.next
                    other_char = other_node.data[0]
                    other_freq = other_node.data[1]

    def __repr__(self):
        ret_str = ""
        for node in self.dll:
            ret_str += (node[1] * node[0])
        return ret_str


cs = CompactString("")
print(cs)
