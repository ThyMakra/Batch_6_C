import re

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

opStack = Stack()
postFix = []
pre = {
    "^": 3,
    "%": 3,
    "*": 3,
    "/":3,
    "-":2,
    "+":2,
    "(":1,
}

def infixToPostfix(eps):
    eps = re.sub(r'([0-9])\s?([a-zA-z])','\g<2>*\g<1>',eps)
    for ep in re.sub(r'\s', '', eps):
        if re.match(r'[^\+\-\*\/\%\^\(\)]', ep):
            postFix.append(ep)
        elif ep == '(':
            opStack.push(ep)
        elif ep == ')':
            top = opStack.pop()
            while top != '(':
                postFix.append(top)
                top = opStack.pop()
        else:
            while len(opStack)>0 and \
            (pre[opStack.peek()]>=pre[ep]):
                postFix.append(opStack.pop())
            opStack.push(ep)
        print(opStack.stack, postFix)

    while len(opStack) > 0:
        postFix.append(opStack.pop())
    return " ".join(postFix)

k = infixToPostfix(input("expression: \n"))
print(k)