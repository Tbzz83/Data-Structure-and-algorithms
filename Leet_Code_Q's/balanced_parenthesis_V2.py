def is_balanced(s):
    stack = []
    keys = {
        ")": "(",
        "]": "[",
        "}": "{"}
    for char in s:
        if len(stack) == 0 and char in keys:
            stack.append('A')  # Adds something to stack so it won't mistakenly call True
            break
        if char in keys.values():  # If char is a valid option always append to our stack
            stack.append(char)
        elif keys[char] == stack[-1]:  # If the last value of stack is able to be closed by our current char we pop it
            stack.pop()
            continue
        else:
            stack.append('A')
            break

    if len(stack) != 0:
        balanced = False
    else:
        balanced = True

    return balanced

print(is_balanced("({{{{}}}))"))

