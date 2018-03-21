# Returns true if mylist is list of numbers with length > 0
# Otherwise returns False
# Complexity: O(n)
def valid_list(mylist):
	if len(mylist) == 0:
		return False

	for item in mylist:
		if type(item) != int:
			return False

	return True