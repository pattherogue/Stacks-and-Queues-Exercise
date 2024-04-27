from stack import Stack

def polish_notation_calculator(expression):
    tokens = expression.split()
    stack = Stack()
    operators = "+-*/"
    for token in tokens[::-1]:
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == "+":
                stack.push(operand1 + operand2)
            elif token == "-":
                stack.push(operand1 - operand2)
            elif token == "*":
                stack.push(operand1 * operand2)
            elif token == "/":
                stack.push(operand1 / operand2)
    return stack.peek()
