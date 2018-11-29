class Node:         # Class to create Nodes
    def __init__(self, Value, Next=None):
        self.value = Value      # value in Node
        self.next = Next        # points to next node

class Stack_LL:
    def __init__(self):
        self.__top = None       # initially top = None
        self.__len = 0          # initially length of stack = 0

    def is_empty(self):
        return self.__top == None

    def push(self, value):
        self.__top = Node(value, self.__top)        # Create Node with value = "value" & next = "top". Make new node as top
        self.__len += 1         # increment length

    def pop(self):
        if(self.is_empty()): raise IndexError("Stack is Empty")         # check if stack is empty
        else:
            temp = self.__top               # temp = top
            self.__top = self.__top.next    # top = next element
            temp.next = None                # (previous top) temp.next -> None (break the link)
            self.__len -= 1                 # decrement length
            return temp.value               # return poped value

    def __len__(self):
        return self.__len

    def __str__(self):          # return str form of linked list i.e., val1 -> val2 -> None
        temp = self.__top
        Values = []
        while temp:
            Values.append(str(temp.value))      # add values to "Values"
            temp = temp.next
        Values.append("None")
        return " -> ".join(Values)          # return all Values as string

    # __next__ and __iter__ methods are used to iterate through the object

    # __next__ is used to get the next element in the iterable object
    def __next__(self):
        temp = self.__i
        if (temp == None): raise StopIteration() # if temp = None, temp has reached the end, raise StopIteration to stop iteration
        self.__i = self.__i.next
        return temp.value

    # __iter__ returns an iterable object (self) & sets i = top, to iterate through top to end
    def __iter__(self):
        self.__i = self.__top
        return self

if __name__ == '__main__':
    S1 = Stack_LL()

    for i in range(5, 21, 5):
        print("push", i, "to stack")
        S1.push(i)

    print("\nStack : ", S1)

    print("\nPop stack, popped value = ", S1.pop())
