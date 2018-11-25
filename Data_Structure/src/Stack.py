class Stack:
	
	def __init__(self, Size=10):
		self.__size = Size
		self.__stack=[]
		self.__i=-1
	
	def isEmpty(self):
		return len(self.__stack) == 0
	def isFull(self):
		return len(self.__stack) == self.__size
	
	def push(self, value):
		if(self.isFull()): raise IndexError("Overflow Error - Stack is Full")
		else: self.__stack.append(value)
	
	def pop(self):
		if(self.isEmpty()): raise IndexError("Unerflow Error - Stack is Empty")
		return self.__stack.pop()
		
	def __len__(self):
		return len(self.__stack)
			
	def __next__(self):
		self.__i+=1 
		if(self.__i < len(self)): return self.__stack[self.__i]
		else: raise StopIteration()
		
	def __iter__(self):
		self.__i=-1
		return self
		
if __name__ == '__main__':
	print("Create stack of size 10")
	S1 = Stack(10)
	
	print("\nPush 10 to stack")
	S1.push(10)
	print("Push 100 to stack")
	S1.push(100)
	
	print("\nPrint stack")
	for i in S1:
		print(i, end=", ")
	
	print("\n\nPop Stack, Popped value = ", S1.pop())
	print("Pop Stack, Popped value = ", S1.pop())
	
	print("\nStack is empty\n")
	
	print("\nPop Stack, Popped value = ", S1.pop())
