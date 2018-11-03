def find_zero_Newton(f,x0=1,df=None,dx=0.1,iterations=1000,precision=1e-7,epsilon=1e-15):
    """
        Uses Newton's method to find a root near the given point x0.
    """
	if df==None:    # Aproximates the derivative if missing
		def derivative(x):
			return (f(x+dx)-f(x))/dx
		df = derivative
	sol = False
	for i in range(iterations):
		y, dy = f(x0), df(x0)
		if abs(dy) < epsilon: break
		
		x1 = x0 - y/dy
		if abs(x1 - x0) <= precision*abs(x1):
			sol = True
			break
		x0 = x1
	if sol:
		print("Solution FOUND")
		return x1
	print("Solution NOT FOUND")
