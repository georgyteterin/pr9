import random
import  time
p = int(input('insert p value ', ))
k = int(input('insert k value ',))
s = []
for i in range(1, p):
    s.append(random.randint(1, 9))
actual_list  = random.sample(s, k)
print(sorted(actual_list))
finding = int(input("insert your desired number ", ))
t_start = time.time()
print(t_start)
for i in range(len(sorted(actual_list))):
    if actual_list[i] == finding:
        print('key is', i)
        break
    if finding not in actual_list:
        print("there is no", finding, " in your list")
        break
t_end = time.time() - t_start
print("time is", t_end)


#10 - 0.0004944801330566406
#100 - 0.00047469139099121094
#10^3 - 0.0004961490631103516
#10^6 - 0.15069222450256348
