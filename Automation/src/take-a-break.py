import time
import subprocess
import os
i = 0
x = 3
print(" The program started on " + time.ctime())
while(i < x):
  time.sleep(1800)
  print(str(i + 1) + " break is taking place on " + time.ctime())
  p = subprocess.Popen(["firefox", "http://www.youtube.com"])
  time.sleep(600)
  i = i + 1
  browserExe = "firefox"
os.system("pkill "+browserExe)
