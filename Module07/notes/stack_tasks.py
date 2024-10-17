def create_stack():
    return[]

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")


stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')
print(peek(stack))