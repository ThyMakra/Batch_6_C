class Stack:
    def __init__(self, max):
        self.stack = [None]*max
        self.count = 0

    def push(self,element):
        self.stack[self.count] = element
        self.count += 1

    def pop(self):
        tmp = self.stack[self.count - 1]
        self.stack[self.count -1] = None
        self.count -= 1
        return tmp

    def __len__(self):
        return self.count
    
    def status(self):
        return "full" if self.count == len(self.stack) else "empty" if self.count == 0 else "not empty or full"

class Menu:
        def __init__(self):
            maxSize = int(input("max of stack: "))
            self.stack = Stack(maxSize)
            self.menu()

        def menu(self):
            inp = input("1. Push\n2. Pop \n3. Palindrome \n4. Status \n5. Exit\n")
            try:
                option = int(inp)
                if not (option>=1 and option<=5):
                    raise ValueError('value must be 1>input>5')
                if option == 1:
                    item = input('please input your item: \n')
                    self.stack.push(item)
                elif option == 2:
                    print(self.stack.pop())
                elif option == 3:
                    string = input("write anything: ")
                    stack = Stack(len(string))
                    palindrome = True
                    for c in string:
                        stack.push(c)
                    for c in string:
                        if c != stack.pop():
                            palindrome = False
                    print('palindrom' if palindrome else "Not palindrome")
                elif option == 4:
                    print(self.stack.status())
                else:
                    return
                self.menu()
            except Exception:
                print("Error happens")
                self.menu()
Menu()