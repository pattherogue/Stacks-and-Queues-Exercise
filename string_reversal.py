from stack import Stack

def reverse_string(string):
    reversed_str = ''
    stack = Stack()
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str
