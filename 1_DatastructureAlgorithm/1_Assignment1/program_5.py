class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack)==0
    
    def peek(self):
        return self.stack[-1]
    def display(self):
        print(*self.stack,sep=" ")

def compute(val1,symbol,val2):
    if symbol == "+":
        return val1 + val2
    if symbol == "-":
        return val1 - val2
    if symbol == "/":
        return val1 / val2
    if symbol == "%":
        return val1 % val2
    if symbol == "*":
        return val1 * val2
    if symbol == "^":
        return val1 ** val2
    return 0
def eval(postfix):
    s = Stack()
    for op in postfix:
        symbol = op
        if symbol.isdigit():
            s.push(symbol)
            s.display()
        else:
            s.push(symbol)
            s.display()
            symbol = s.pop()
            val2 = float(s.pop())
            val1 = float(s.pop())
            res = compute(val1,symbol,val2)
            s.push(res)
        
    return s.pop()

postfix = str(input("Enter the postfix expression: "))
ans = eval(postfix)
print(ans)