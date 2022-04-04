# given a list of dictionaries in this form:
# data = [
# {'indication': 'A', 'level': '1', 'ID': '174'},
# {'indication': 'A', 'level': '15', 'ID': '174'},
# {'indication': 'B', 'level': '2', 'ID': '222'},
# {'indication': 'A', 'level': '8', 'ID': '241'},
# {'indication': 'C', 'level': '1', 'ID': '543'},
# {'indication': 'D', 'level': '3', 'ID': '111'}
# ]
# reformat a dictionary that has keys idenfitied by a list of keys with values that subsequently match
# for example
# an input list of keys as ['indication', 'ID'] would generate
#
#
#
# { 
#	A:
#		174:
#			[{'indication': 'A', 'level': '1', 'ID': '174'}],
#			{'indication': 'A', 'level': '15', 'ID': '174'}]
#		241:
#			[{'indication': 'A', 'level': '8', 'ID': '241'}]
#	B:
#		222:
#			[{'indication': 'B', 'level': '2', 'ID': '222'}]
#	C:
#		543:
#			[{'indication': 'C', 'level': '1', 'ID': '543'}]
#	D:
#		111:
#			[{'indication': 'D', 'level': '3', 'ID': '111'}]
# }

data = [
	{'indication': 'A', 'level': '1', 'ID': '174'},
	{'indication': 'A', 'level': '15', 'ID': '174'},
	{'indication': 'B', 'level': '2', 'ID': '222'},
	{'indication': 'A', 'level': '8', 'ID': '241'},
	{'indication': 'C', 'level': '1', 'ID': '543'},
	{'indication': 'D', 'level': '3', 'ID': '111'}
	]

def generate_nested_dictionary(data, keys):
	output_dic = {}
	for i in range(len(data)):
		inner_dic = output_dic
		location = []
		for j in range(len(keys)):
			location += [data[i][keys[j]]]
			if j == len(keys) - 1:
				# we're there.. add the value
				print(inner_dic)
				print(data[i])
				#inner_dic[data[i][keys[j]]] = [data[i]]
				#inner_dic = output_dic
			elif data[i][keys[j]] in inner_dic.keys():
				inner_dic = inner_dic[data[i][keys[j]]]
			else:
				inner_dic[data[i][keys[j]]] = "something"
			#if j == len(keys) - 1:
				#print(location)
				#print(data[i])
	return output_dic

generate_nested_dictionary(data, ['indication', 'ID'])
