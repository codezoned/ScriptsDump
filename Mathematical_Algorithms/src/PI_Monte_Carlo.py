def Pi_Monte_Carlo(n):
    #Returns PI number generated with Monte Carlo method.
    #We have a 1x1 square and a circle with R=1 on the coordinates, with the middle point (0,0).
    #We draw n points randomly to check whether they are included in the circle.

    import random as rd
    k = 0 #number of points included in the circle inside the square
    
    for i in range(n):      #draw the x & y coordinates randomly (uniform distribution) from the square
        x = rd.uniform(-1,1)
        y = rd.uniform(-1,1)
        if x**2 + y**2 <= 1:
            k+=1

    #circle_surface = pi * r**2
    #square_surface = 4  * r**2     
    #circle_surface / square_surface = pi / 4
    #pi = 4 * circle_surface / square_surface = 4 * n / k
    pi = 4 * k/n
    return(pi)
