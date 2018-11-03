"""Gradient Descent from Scratch for implementing Linear Regression 
Code by Paritosh Mahajan, github - https://github.com/paritoshM9 """ 
import numpy as np 
import matplotlib.pyplot as plt 



def error(m_current, b_current, x, y):
	""" Calculates total squared error in the predicted y value and the actual y value"""
	error = 0
	for i in range(len(x)):

		error += (y[i] - (m_current*x[i] + b_current))**2

	return error

def runner(m_current, b_current, x, y, num_iter, learning_rate):
	"""Main function for gradient descent, It returns the final value of b and m after doing num_iter iterations"""
	for i in range(num_iter):

		[m_current, b_current] = step_grad (m_current, b_current, x, y, learning_rate)

	b_final = b_current
	m_final = m_current
	return [b_final, m_final]

    

def step_grad(m, b, x, y, learning_rate):

	""" It consists of individual iterations , where the program updates the parameters b and m , after learning from the error"""
	m_grad = 0
	b_grad = 0

	N = len(x)

	for i in range(N):

		m_grad += (-2/N) * (x[i]*(y[i] - (m * x[i] + b)))
		b_grad += (-2/N) * ((y[i] - (m * x[i] + b)))
	m = m - (learning_rate * m_grad)
	b = b - (learning_rate * b_grad)
	cost = error(m,b,x,y)

	return [m,b] 



if __name__ == '__main__':
    
    X = [1,2,34,5,3,2,13,4,5] # independent variable
    y = [2,4,65,12,7,3.5,30,10,9] #dependent variable
    print(X,y)
     
	
    initial_b = 1
    initial_m = 1
    num_iterations = 5000
    learning_rate = 0.0001
    [b,m]  = runner(initial_m, initial_b, X, y, num_iterations, learning_rate)
    # line equation = m*x + b , m is the slope and b is the intercept
    print(m , b)
    
    plt.scatter(X,y)
    #fit function
    f = lambda x: m*x + b
    # x values of line to plot
    x = np.array([0,40])
    # plot fit
    plt.plot(x,f(x),lw=1, c="k",label="fit line between 0 and 40")

    plt.show()

    
   
