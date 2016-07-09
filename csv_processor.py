# Author: Sirui Feng
# This file includes codes to read in and write out to csv file.

import csv

input_file_path = '../test2.csv'
output_file_path = 'test_output.csv'

def read_csv(input_file_path):

	with open(input_file_path) as f:
		reader = csv.DictReader(f)
		fieldnames = reader.fieldnames
		for row in reader:
			for field in fieldnames:
				print(field, "is", row[field])

	return None

def write_to_csv(input_file_path):

	fieldnames = ['first_attribute', 'second_attribute', 'third_attribute']
	with open(output_file_path, "w") as f:
	    writer = csv.DictWriter(f, fieldnames=fieldnames)
	    writer.writeheader()

	    # Modify the following codes as you need.
	    row = dict()
	    row['first_attribute'] = 'a'
	    row['second_attribute'] = 'b'
	    row['third_attribute'] = 'c'
	    writer.writerow(row)

	print("Your csv has been saved to", output_file_path)
	return None


if __name__=='__main__':
	#read_csv(input_file_path)
	write_to_csv(output_file_path)