def main():
  import sys
  from sys import stdin, stdout
  from heapq import heappush, heappop
  sys.setrecursionlimit(9999999)
  def find(x):
    if x == parent[x]:
      return x
    parent[x] = find(parent[x])
    return parent[x]
 
  def union(x, y):
    compx = find(x)
    compy = find(y)
    if compx == compy:
      return False
    parent[compx] = compy
    return True
 
 
  n, m = stdin.readline().split()
  n = int(n)
  m = int(m)
 
  parent = range(n+1)
  heap = []
  for i in range(m):
    x,y,p = [int (i) for i in stdin.readline().split()]
    heappush(heap, (p,x,y))

  cont = 0
  while len(heap) > 0:
	  peso, x, y = heappop(heap)
	  if find(x) != find(y):
		  cont += peso
		  union(x,y)
  stdout.write(str(cont)+"\n")
 
if __name__ == "__main__":
	main()
