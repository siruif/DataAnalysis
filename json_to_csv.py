# Author: Sirui Feng
# This file transforms a json file to a csv file

import json
import csv

input_file_path = '../test2.json'	#input file has to be a json
output_file_path = '../test2.csv'	#output is in csv format
header_list = ['fullVisitorId', 'visitId', 'date', 'hits_time_seconds', \
'pagePath', 'member', 'mp', 'travel', 'FltStat', 'MyTrips', 'CkIn']

def json_to_csv(input_file_path, output_file_path):

	with open(output_file_path, 'w') as outfile:
		w = csv.writer(outfile, delimiter = ',')
		w.writerow(header_list)
		with open(input_file_path) as infile:
			for line in infile:
				row_dict = json.loads(line)

				writer_list = []
				for k in header_list:
					v = row_dict.get(k,'null')
					# if k == 'fullVisitorId':
					# 	v = str(v)
					writer_list.append(v)
				w.writerow(writer_list)



if __name__ == '__main__':
	json_to_csv(input_file_path, output_file_path)
	print("High Five! \nYour file", input_file_path, \
		"has been successfully converted to csv to the following address:", output_file_path)