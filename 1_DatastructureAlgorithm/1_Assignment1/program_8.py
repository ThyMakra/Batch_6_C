def traversal(n,t):
    if t == 'n':
        if n == circular[-1]:
            print(circular[0])
        else:
            print(circular[circular.index(n)+1]) 
    else:
        if n == circular[0]:
            print(circular[-1])
        else:
            print(circular[circular.index(n)-1]) 
def deletion(el):
    circular.remove(el)
    print(circular)

def insertion(index,value):   
    circular.insert(index,value)
    print(circular)



circular = []
number_element = int(input("Input linked List Size:"))
for i in range(number_element):
    circular.append(int(input()))
print(circular)


#Traversal Node 
node, travel = int(input("Which node do you start to traversal:")),input("Go to next/previous? n/p: ")
traversal(node,travel)

#Delete the element
deletion(int(input("Which element do you want to delete?:")))

#insert the element
insertion(int(input("which index do you want to insert?:")),int(input("Input value of new node:")))