class Queue:

	def __init__(self, Size = 10):
		self.__size = Size
		self.__queue = [None]*Size
		self.__head = self.__tail = 0
		self.__i = -1

	def isEmpty(self):
		return self.__head == self.__tail

	def isFull(self):
		return self.__tail == self.__size

	def EnQueue(self, value):
		if(self.isFull()): raise IndexError("Overflow Error - Queue is Full")
		self.__queue[self.__tail] = value
		self.__tail += 1

	def DeQueue(self):
		if(self.isEmpty()): raise IndexError("Unerflow Error - Queue is Empty")
		self.__head += 1
		return self.__queue[self.__head-1]

	def __len__(self):
		return self.__tail - self.__head

	def __getitem__(self, index):
		if(self.__head <= (index + self.__head) < self.__tail):
			return self.__queue[index + self.__head]
		else: raise IndexError("Index out of range")

	def __next__(self):
		self.__i += 1
		if(self.__i < len(self)): return self.__getitem__(self.__i)
		else: raise StopIteration()

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

	print("\n\nDeQueue / Delete, Deleted element = ", Q1.DeQueue())
