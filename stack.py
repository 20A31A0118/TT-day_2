def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0


def maruthipush(stack, item):
    stack.append(item)
    print("pushed item: " +item)

def maruthipop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    else:
        return stack.pop()

stack = create_stack()
maruthipush(stack, str(input()))
maruthipush(stack, str(input()))
maruthipush(stack, str(input()))
maruthipush(stack, str(input()))
print("popped item: " + maruthipop(stack))
print("popped item: " + maruthipop(stack))
print("popped item: " + maruthipop(stack))
print("popped item: " + maruthipop(stack))
print("popped item: " + maruthipop(stack))
print("stack after popping an elementing:" + str(stack))


