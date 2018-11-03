import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt  

class LinearRegression:
	def fit(self, x, y, learning_rate):
		self.n_weights = np.zeros(x.shape[1])
		self.learning_rate = learning_rate
		self.loss_=[]
		print("Initial cost {} ".format(model.cost_function(x, y, self.n_weights)))
		model.gradient(x, y, self.n_weights, 10000)
		print("Final cost {} ".format(model.cost_function(x, y, self.n_weights)))
		return self.n_weights


	def cost_function(self, x, y, n_weights):
		n = len(y)
		cost = np.sum((x.dot(self.n_weights.T) - y) ** 2) / (2 * n)
		return cost
	


	def gradient(self, x, y, n_weights, epochs):
		m = len(y)
		for i in range(epochs):
			h = x.dot(n_weights.T)
			loss = h - y
			change=(x.T.dot(loss) / m) * self.learning_rate
			self.n_weights -= change
			self.loss_.append(model.cost_function(x, y, self.n_weights))
			if i % 10 == 0:
				print("Loss of {}th epoch is {} ".format(i , model.cost_function(x, y, self.n_weights)))
		return self.n_weights

	def predict(self, x):
		x=np.insert(x, 0 ,1)
		print(x.T.dot(self.n_weights))



	def plot(self):
		plt.plot(self.loss_)
		plt.xlabel("Epochs")
		plt.ylabel("Loss")
		plt.show()



if __name__ == "__main__":
	#Importing data and some preprocessing
	data = pd.read_csv('student.csv')
	data["one"] = [1 for i in data["Math"]]
	math = data["Math"]
	write = data["Writing"]
	read = data["Reading"]
	one = data["one"]
	x = np.array([one,math,read]).T
	y = np.array(write)
	learning_rate = 0.0001
	model = LinearRegression()
	model.fit(x, y, learning_rate)
	print("Plotting loss")
	model.plot()
	model.predict(np.array([45,48]))
