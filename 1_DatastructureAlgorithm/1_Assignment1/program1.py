
arr = []
def create():
    print("Enter number of element")
    ip = int(input())
    for i in range(ip):
        s = int(input())
        arr.append(s)
def display():
    return arr
def insert():
    print("Enter element that to be inserted in valid position")
    print("Enter the position")
    p = int(input())
    print("Enter the value")
    s = int(input())
    arr.insert(p,s)
    return arr
def delete():
    print("Enter the index that you want to remove")
    s = int(input())
    del arr[s]
    return arr
create()
print(display())
print(insert())
print(delete())
