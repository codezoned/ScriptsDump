import numpy as np
import matplotlib.pyplot as plt  
class SimpleLinearRegression:
	def __init__(self):
		self.w_0 = 0
		self.w_1 = 0

	def fit(self,x,y):
		n = len(x)
		m_x,m_y = np.mean(x),np.mean(y)
		self.w_1 = np.sum(y * x - n * m_x * m_y) / np.sum(x * x - n * m_x * m_x)
		self.w_0 = m_y - (self.w_1 * m_x)
		return(self.w_0,self.w_1)

	def predict(self,x_test):
		y_pred = self.w_0 + self.w_1 * x_test
		return y_pred

	def plot(self,x,y):
		plt.scatter(x,y,color="r",marker="o")
		line=self.w_0 + self.w_1 * x
		plt.plot(x,line,color="g")
		plt.xlabel("X")
		plt.ylabel("Y")
		plt.show()

if __name__ == "__main__":
	x=np.array([1,2,3,4,5,6,7,8,9,10])
	y=np.array([300,400,500,600,700,800,900,1000,1200,1400])
	model=SimpleLinearRegression()
	model.fit(x,y)
	print(model.predict(11))
	model.plot(x,y)