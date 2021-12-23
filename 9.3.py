import time, random
start_time=time.time()
lst=[randint(0,1000) for i in range(1000000)]
lst=sorted(lst)
def find_x(lst,left, right, x):
  if left>=right:
    m=round((left+right)/2)
    if lst[m]>x:
       return find_x(lst,left, right, x)
    elif lst[m]<x:
      return find_x(lst,left, right, x)
    if lst[m]==x:
      return print('Yes', time.time()-start_time)
  return print('No', time.time()-start_time)
   #1: 0.00024628639221191406
   #100: 0.0006239414215087891
   #1000: 0.0017595291137695312
   #1000000: 1.5827996730804443