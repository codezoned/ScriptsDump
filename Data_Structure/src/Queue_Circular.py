class Queue_Circular:

    def __init__(self, Size=10):
        self.__size = Size+1              #Store Size+1 in size
        self.__queue = [None]*(Size+1)    #generate a List of length "size" containing None (initial value)
        self.__head = self.__tail = 0     #Initial value of head & tail = 0
        self.__i = -1                     # i is used as index in __next__ method to iterate through the Queue object

    def isEmpty(self):
        return self.__head == self.__tail        #If head == tail, Queue is empty
    def isFull(self):
        return (self.__tail+1)%self.__size == self.__head    #if next tail (circular increment) == head, queue is full

    def EnQueue(self, value):
        if(self.isFull()): raise IndexError("Overflow Error - Queue is Full")
        self.__queue[self.__tail] = value                #store "value" at tail
        self.__tail = (self.__tail+1)%self.__size        #increment tail by 1 & mod size (circular increment)

    def DeQueue(self):
        if(self.isEmpty()): raise IndexError("Unerflow Error - Queue is Empty")
        self.__head = (self.__head+1)%self.__size            # increment head (circular increment)
        return self.__queue[(self.__head-1)%self.__size]     # Return value at head-1 (circular decrement) (previous head = value to be deleted)

    #if tail > head, return tail - head
    #else, return size - head + tail
    def __len__(self):
        return self.__tail-self.__head if(self.__tail>=self.__head) else self.__size-self.__head+self.__tail

    # __getitem__ is used to get value at a particular index
    def __getitem__(self, index):
        if(0 <= index < len(self)):                                 #if index is between 0 & len of queue
            return self.__queue[(index+self.__head)%self.__size]    #return the value at index
        else: raise IndexError("Index out of range")                #else, raise exception

    # __next__ and __iter__ methods are used to iterate through the object (used internally at Line 56 & 69 in for loop to print all element)

    # __next__ is used to get the next element in the iterable object
    def __next__(self):
        self.__i += 1        # i is the index of the element to return
        if(self.__i < len(self)): return self.__getitem__(self.__i)    #use __getitem__ to get the value at index i
        else: raise StopIteration()        # if i is larger than len, all the elements have been traversed, raise StopIteration to stop iteration

    # __iter__ returns an iterable object (self) & sets i = -1, to iterate through 0 to end
    def __iter__(self):
        self.__i = -1
        return self

if __name__ == '__main__':
    print("\nCreate Circular Queue of size 5\n")
    Q1 = Queue_Circular(5)

    #insert 5, 10, 15, 20, 25 in Queue Q1
    for i in range(5, 30, 5):
        print("EnQueue (Insert) ", i)
        Q1.EnQueue(i)

    print("\nPrint Queue")
    for i in Q1:
        print(i, end=", ")

    print("\n\nEnQueue (Insert) 30")
    try: Q1.EnQueue(30)         #This raises error because the Queue is full
    except IndexError: print("Queue is Full")

    print("\nDeQueue (Delete), Deleted value = ", Q1.DeQueue())

    print("\nEnQueue (Insert) 30")
    Q1.EnQueue(30)

    print("\nPrint Queue")
    for i in Q1:
        print(i, end=", ")
