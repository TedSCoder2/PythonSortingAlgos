# demo of the bubble_sort function
from SortPackage.BubbleSort import bubble_sort
from random import randint
import time
start_time = time.time()

N = 10000
mylist = []

for x in range(0,N):
	mylist.append(randint(0,50))

mylist_sorted = bubble_sort(mylist)
print(mylist)
print(mylist_sorted)

print("--- %s seconds ---" % (time.time() - start_time))