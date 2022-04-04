# given a list of dictionaries in this form:
# data = [
# {'indication': 'A', 'level': '1'},
# {'indication': 'B', 'level': '2'},
# {'indication': 'A', 'level': '8'},
# {'indication': 'C', 'level': '1'},
# {'indication': 'D', 'level': '3'}
# ]
# reformat a dictionary that has indication as the key and level as the value
# for example
# here we would generate:
#
#
#
# { 
#	A:
#		[{'indication': 'A', 'level': '1'},
#		{'indication': 'A', 'level': '8'}],
#	B:
#		[{'indication': 'B', 'level': '2'}],
#	C:
#		[{'indication': 'C', 'level': '1'}],
#	D:
#		[{'indication': 'D', 'level': '3'}]
# }

data = [{'indication': 'A', 'level': '1'},{'indication': 'B', 'level': '2'},{'indication': 'A', 'level': '8'},{'indication': 'C', 'level': '1'},{'indication': 'D', 'level': '3'}]

def generate_output(data):
	output_dic = {}
	for i in range(len(data)):
		if data[i]['indication'] in output_dic.keys():
			output_dic[data[i]['indication']] += [data[i]]
		else:
			output_dic[data[i]['indication']] = [data[i]]
	return output_dic
