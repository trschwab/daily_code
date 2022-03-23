def generate(numRows):
	return_list = [[1],[1,1], [1, 2, 1]]
	if numRows == 1:
		return [return_list[0]]
	if numRows == 2:
		return [return_list[0], return_list[1]]
	while numRows > 3:
		new_row = [1]
		for i in range(1, len(return_list[-1])):
			new_row += [return_list[-1][i] + return_list[-1][i-1]]
		new_row += [1]
		return_list += [new_row]
		numRows -= 1
	return return_list
