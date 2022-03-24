def groupAnagrams(strs):
	if len(strs) == 1 and strs[0] == "":
		return [[""]]
	if len(strs) == 1:
		return [strs[0]]
	dic = {}
	return_list = []
	for i in range(len(strs)):
		key = "".join(sorted(strs[i]))
		if len(return_list) == 0:
			dic[key] = 0
			return_list = [[strs[i]]]
		elif key in dic.keys():
			return_list[dic[key]] += [strs[i]]
		else:
			return_list += [[strs[i]]]
			dic[key] = len(return_list) - 1
	return return_list
