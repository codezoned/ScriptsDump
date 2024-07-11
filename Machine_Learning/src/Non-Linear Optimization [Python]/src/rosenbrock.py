'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from numpy import *
from newton import *
from quasi_newton import *
from steepest_descent import *
from conjugate_gradient import *

if __name__ == '__main__':
  def f(x): return 100 * math.pow(x[1] - math.pow(x[0], 2), 2) + math.pow(1 - x[0], 2)
  def df_dx1(x): return 400*math.pow(x[0], 3) - 400*x[0]*x[1] + 2*x[0] - 2
  def df_dx2(x): return 200*x[1] - 200*math.pow(x[0], 2)
  def fd(x): return array([ df_dx1(x), df_dx2(x) ])
  
  def df_dx1_dx1(x): return 1200*math.pow(x[0], 2) - 400*x[1] + 2
  def df_dx1_dx2(x): return-400*x[0]
  
  def fdd(x):
    return array([
        [df_dx1_dx1(x), df_dx1_dx2(x)],
        [df_dx1_dx2(x), 200]])
  
  def print_error(i, direction, alpha, x):
    opt = f(array([1,1]))
    print("%d, %.20f" % (i, f(x)-opt))
  
  def print_gradient(i, direction, alpha, x):
    print("%d, %.20f" % (i, linalg.norm(fd(x))))
  
  def print_all(i, direction, alpha, x):
    print("iteration %d: \t direction: %s \t alpha: %.7f \t x: %s"
        % (i, ["%.7f" % _ for _ in direction], alpha, ["%.7f" % _ for _ in x]))
  
  x = array([0, 0])
  precision = 10e-6
  max_iterations = 100
  callback = print_all
  
  print("steepest descent:")
  steepest_descent(f, fd, x, max_iterations, precision, callback)
  
  print("\nnewton:")
  newton(f, fd, fdd, x, max_iterations, precision, callback)
  
  print("\nquasi newton:")
  quasi_newton(f, fd, x, max_iterations, precision, callback)
  
  print("\nconjugate gradient:")
  conjugate_gradient(f, fd, x, max_iterations, precision, callback)
  
