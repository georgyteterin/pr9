import time, random
from random import randint
def find_x(x,n):
  start_time=time.time()
  lst=[randint(0,1000) for i in range(n)]
  lst=sorted(lst)
  left=0
  right=len(lst)-1
  while left<=right:
    m=round((left+right)/2)
    if lst[m]>x:
      right=m-1
    elif lst[m]<x:
      left=m+1
    if lst[m]==x:
      return print('Yes', time.time()-start_time)
      break
  return print('No', time.time()-start_time)
find_x(10,1) 
find_x(10,100)  
find_x(10,1000) 
find_x(10,1000000)  

#10 - 0.000019073486328125
#100 - 0.0001590251922607422
#10^3 - 0.0015716552734375
#10^6 - 1.587099313735962
