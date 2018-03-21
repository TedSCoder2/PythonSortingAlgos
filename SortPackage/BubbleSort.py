'''
Bubblesort program using Python
main function: bubble_sort(mylist)
input: list of unsorted numbers
output: list of sorted numbers
'''
from SortPackage.SubPackage.validcheck import valid_list

# Compares two elements in a list puts larger number to "next" 
# index on the list and return back that list
# Otherwise, do nothing to the list and return it back
def compare_two(mylist,curr,curr_next):
	if mylist[curr] > mylist[curr_next]:
		placeholder = mylist[curr_next]
		mylist[curr_next] = mylist[curr]
		mylist[curr] = placeholder

	return mylist

# the main function
def bubble_sort(mylist):
	if not valid_list(mylist) and not valid_flag: 
		print("Please input valid list of numbers!")
		return mylist

	#list has been deemed valid from here
	#bubble sort by nature is O(n^2) on avg
	#bubble up decreasingly high number to the end
	for j in range(0,len(mylist)-2):
		#bubble up higher number in the list to the end
		for i in range(0,len(mylist)-j-1):
			mylist = compare_two(mylist,i,i+1)

	return mylist


