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
import numpy

def find_step_length(f, fd, x, alpha, direction, c2):
  g = lambda alpha: f(x+alpha*direction)
  gd = lambda alpha: numpy.dot(fd(x + alpha*direction), direction)
  return interpolation(g, gd, alpha, c2)

def wolf1(f, fd, alpha):
  c1 = 1e-4
  return f(alpha) <= f(0) + c1*alpha*fd(alpha)

def wolf_strong(f, fd, alpha, c2):
  return abs(fd(alpha)) <= -c2*fd(0)

def simple_backtracking(f, fd, alpha, c2):
  rate = 0.5
  while not (wolf1(f, fd, alpha) or wolf_strong(f, fd, alpha, c2)):
    alpha = rate*alpha
  return alpha

def interpolation(f, fd, alpha, c2):
  lo = 0.0
  hi = 1.0
    
  for i in range(0, 20):
    if wolf1(f, fd, alpha):
      if wolf_strong(f, fd, alpha, c2):
        return alpha
    
    half = (lo+hi)/2.0
    alpha = - (fd(lo)*hi*hi) / (2*(f(hi)-f(lo)-fd(lo)*hi))
    
    if alpha < lo or alpha > hi: # quadratic interpolation failed. reduce by half instead
      alpha = half
    if fd(alpha) > 0:
      hi = alpha
    elif fd(alpha) <= 0:
      lo = alpha
  return alpha
