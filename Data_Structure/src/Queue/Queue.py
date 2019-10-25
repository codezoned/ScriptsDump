class Queue:

    def __init__(self, Size = 10):
        self.__size = Size                #Store the size of the queue
        self.__queue = [None]*Size        #generate a List of length "Size" containing None (initial value)
        self.__head = self.__tail = 0     #Initial value of head & tail = 0
        self.__i = -1                     # i is used as index in __next__ method to iterate through the Queue object

    def isEmpty(self):
        return self.__head == self.__tail    #If head == tail, Queue is empty

    def isFull(self):
        return self.__tail == self.__size    #if tail == size of queue, queue is full

    def EnQueue(self, value):
        if(self.isFull()): raise IndexError("Overflow Error - Queue is Full")
        self.__queue[self.__tail] = value    #insert "value" at tail
        self.__tail += 1                     #increment tail

    def DeQueue(self):
        if(self.isEmpty()): raise IndexError("Unerflow Error - Queue is Empty")
        self.__head += 1                      #Increment head
        return self.__queue[self.__head-1]    #Return value at head-1 (previous head = value to be deleted)

    def __len__(self):
        return self.__tail - self.__head    #return number of elements in the queue

    def __getitem__(self, index):                                    # __getitem__ method is used to get element stored at a particular index
        if(self.__head <= (index + self.__head) < self.__tail):      #if the index is valid (between head & tail)
            return self.__queue[index + self.__head]                 #return the value
        else: raise IndexError("Index out of range")                 #else raise error

    # __next__ and __iter__ methods are used to iterate through the object (used internally at Line 58 in for loop to print all element)

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

    print("\nCreated Queue of size 5")
    Q1 = Queue(5)

    print("\nEnQueue (Insert) 5")
    Q1.EnQueue(5)
    print("EnQueue (Insert) 15")
    Q1.EnQueue(15)

    print("\nPrint Queue")
    for i in Q1:
        print(i, end=", ")

    print("\n\nDeQueue (Delete), Deleted element = ", Q1.DeQueue())
    print("DeQueue (Delete), Deleted element = ", Q1.DeQueue())

    print("\nQueue empty\n")

    print("\n\nDeQueue / Delete, Deleted element = ", Q1.DeQueue())		#This line raises error as the Queue is empty & cannot delete any element
