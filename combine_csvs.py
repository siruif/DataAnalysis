# Author: Sirui Feng
# This file combines different csvs into an integrated one.

import csv
import time


input_paths = ['../data/unsorted000000000009.csv','../data/unsorted000000000009.csv', \
'../data/unsorted000000000009.csv', '../data/unsorted000000000009.csv', \
'../data/unsorted000000000009.csv', \
'../data/unsorted000000000009.csv', '../data/unsorted000000000009.csv', \
'../data/unsorted000000000009.csv','../data/unsorted000000000009.csv', \
'../data/unsorted000000000009.csv']

output_path = '../data/output/combined.csv'

fieldnames_outfile=['customerId', 'date', 'hits_time_seconds', 'pagePath', 'member', 'device', 'browser', 'homepage']

def combine_csv(input_paths, output_path, fieldnames_outfile, default_value=None):
	with open(output_path,'w') as outfile:
		writer = csv.DictWriter(outfile, fieldnames = fieldnames_outfile)

		writer.writeheader()

		num_row = 0

		for input_path in input_paths:
			with open(input_path) as infile:
				reader = csv.DictReader(infile)
				for row_infile in reader:
					row_outfile = dict()
					for attr in fieldnames_outfile:
						row_outfile[attr] = row_infile.get(attr, default_value)
					writer.writerow(row_outfile)
					num_row+=1

	print("Done writing a total of", num_row, "rows into", output_path)

if __name__ == '__main__':
	start_time = time.time()
	combine_csv(input_paths, output_path, fieldnames_outfile)
	end_time = time.time()
	print("Combining files took", end_time - start_time, 'seconds.')