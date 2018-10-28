# Code by MASTER-FURY
# and Matlmr

from math import sqrt

def discriminant(a, b, c):

    if a == 0 and b == 0:

        print('This is a Constant')

        print('Hence No Solution')

    elif a == 0:

        print('This is a Linear Equation')

        print('Hence One Solution: {}'.format(-c / b))

    else:

        discriminant = (b ** 2) - (4 * a * c)

        if discriminant > 0:

            print('Discriminant is {} which is Positive'.format(discriminant))

            print('Hence Two Solutions: {} and {}'.format((-b + sqrt(discriminant)) / (2 * a),
                                                          (-b - sqrt(discriminant)) / (2 * a)))

        elif discriminant == 0:

            print('Discriminant is {} which is Null'.format(discriminant))

            print('Hence One Solution: {}'.format(-b / (2 * a)))

        else:

            print('Discriminant is {} which is Negative'.format(discriminant))

            print('Hence No Real Solutions')

            print('There a Two Complex roots : {} and {}'.format(complex(-b, -sqrt(-discriminant)) / (2 * a),
                                                                 complex(-b, +sqrt(-discriminant)) / (2 * a)))

# Driver Code
a = 2
b = 2
c = 2
discriminant(a, b, c)