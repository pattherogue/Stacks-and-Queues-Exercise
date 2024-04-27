from stack import Stack

def balanced_brackets(string):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if opening_brackets.index(top_char) != closing_brackets.index(char):
                return False
    return stack.is_empty()
