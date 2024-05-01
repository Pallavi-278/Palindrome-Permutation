def can_form_palindrome(s):
    char_set = set()
    for char in s:
        if char in char_set:
            char_set.remove(char)
        else:
            char_set.add(char)
    if len(char_set) <= 1:
        return "YES"
    else:
        return "NOT"

s = input()
result = can_form_palindrome(s)
print(result)