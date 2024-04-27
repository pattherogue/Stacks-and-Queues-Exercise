from stack import Stack

def browser_navigation():
    forward_stack = Stack()
    backward_stack = Stack()

    def visit_site(site):
        backward_stack.push(site)
        forward_stack = Stack()  # Reset forward stack

    def go_back():
        if backward_stack.is_empty():
            print("Cannot go back, already at the beginning")
        else:
            current_site = backward_stack.pop()
            forward_stack.push(current_site)
            print("Went back to:", current_site)

    def go_forward():
        if forward_stack.is_empty():
            print("Cannot go forward, already at the latest page")
        else:
            current_site = forward_stack.pop()
            backward_stack.push(current_site)
            print("Went forward to:", current_site)

    return visit_site, go_back, go_forward
