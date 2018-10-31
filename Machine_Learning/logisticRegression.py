from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

iris=load_iris()
x=iris.data[0:100, :2]
y=[]
for i in iris.target:
	if i==0 or i==1:
		y.append(i)
print(len(y))
print(x.shape)

class LogisticRegression:
	def __init__(self,learning_rate,epochs):
		self.learning_rate = learning_rate
		self.epochs = int(epochs)
	def sigmoid(self,z):
		return 1 / (1 + np.exp(-z))


	def loss(self,h,y):
		return (-y * np.log(h) -  (1-y) * np.log(1 - h)).mean()


	def fit(self,x,y):
		y=np.array(y)
		self.w=np.random.randn(x.shape[1])
		for i in range(self.epochs):
			z = np.dot(x,self.w)
			h=self.sigmoid(z)
			difference = np.dot(x.T,(h - y ))/len(y)
			self.w -= self.learning_rate*difference
			if i % 10 ==0:
				lo=self.loss(h,y)
				print("Loss at {} epoch is {} ".format(i,lo))
		return self.w

		
	def predict(self,x):
		return(self.sigmoid(np.dot(x,self.w)))

model = LogisticRegression(0.1,1000)
x_train,x_test,y_train,y_test=train_test_split(x,y)
print(model.fit(x_train,y_train))
y_pred = model.predict(x_test)
for i in range(len(y_pred)):
	if y_pred[i] > 0.5:
		y_pred[i]=1
	else:
		y_pred[i]=0
print(y_pred)
y_test=np.array(y_test)
print((y_test == y_pred ).mean())
