class Queue_Circular:

	def __init__(self, Size=10):
		self.__size = Size+1
		self.__queue = [None]*(Size+1)
		self.__head = self.__tail = 0
		self.__i = -1

	def isEmpty(self):
		return self.__head == self.__tail
	def isFull(self):
		return (self.__tail+1)%self.__size == self.__head

	def EnQueue(self, value):
		if(self.isFull()): raise IndexError("Overflow Error - Queue is Full")
		self.__queue[self.__tail] = value
		self.__tail = (self.__tail+1)%self.__size

	def DeQueue(self):
		if(self.isEmpty()): raise IndexError("Unerflow Error - Queue is Empty")
		self.__head = (self.__head+1)%self.__size
		return self.__queue[(self.__head-1)%self.__size]

	def __len__(self):
		return self.__tail-self.__head if(self.__tail>=self.__head) else self.__size-self.__head+self.__tail

	def __getitem__(self, index):
		if(0 <= index < len(self)):
			return self.__queue[(index+self.__head)%self.__size]
		else: raise IndexError("Index out of range")

	def __next__(self):
		self.__i += 1
		if(self.__i < len(self)): return self.__getitem__(self.__i)
		else: raise StopIteration()

	def __iter__(self):
		self.__i = -1
		return self

if __name__ == '__main__':
	print("\nCreate Circular Queue of size 5\n")
	Q1 = Queue_Circular(5)

	for i in range(5, 30, 5):
		print("EnQueue (Insert) ", i)
		Q1.EnQueue(i)

	print("\nPrint Queue")
	for i in Q1:
		print(i, end=", ")

	print("\n\nEnQueue (Insert) 30")
	try: Q1.EnQueue(30)
	except IndexError: print("Queue is Full")

	print("\nDeQueue (Delete), Deleted value = ", Q1.DeQueue())

	print("\nEnQueue (Insert) 30")
	Q1.EnQueue(30)

	print("\nPrint Queue")
	for i in Q1:
		print(i, end=", ")
