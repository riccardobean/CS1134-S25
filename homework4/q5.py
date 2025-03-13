def count_lowercase(s, low, high):
    if low == high:
        if s[low] == s[low].lower():
            return 1
        else:
            return 0
    else:
        if s[low] == s[low].lower():
            return 1 + count_lowercase(s, low + 1, high)
        else:
            return 0 + count_lowercase(s, low + 1, high)


def is_number_of_lowercase_even(s, low, high):
    if low == high:
        if s[low] == s[low].lower():
            return False
        else:
            return True
    else:
        temp = is_number_of_lowercase_even(s, low + 1, high)
        if temp:
            if s[low] == s[low].lower():
                return False
            else:
                return True
        else:
            if s[low] == s[low].lower():
                return True
            else:
                return False