def check_balanced(stack, char):
    if f'{stack[-1]}{char}' in ["[]", "()", "{}"]:
        stack.pop()
        return True
    return False


def is_balanced(string):
    stack = []
    isBalanced = True

    for char in string:
        if char in ["[", "(", "{"]:
            stack.append(char)
        elif char in ["]", ")", "}"]:
            isBalanced = check_balanced(stack, char)
        else:
            isBalanced = False
        if not isBalanced:
            break
    return isBalanced


def test_if_balanced(string):
    print(f'{string} is balanced: {is_balanced(string)}')


test_if_balanced("{{)(}}")
test_if_balanced("({)}")
test_if_balanced("[({})]")
test_if_balanced("{}([])")
test_if_balanced("{()}[[{}]]")
