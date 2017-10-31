#!/usr/bin/env python

import sys

def main():
	file1_name = sys.argv[1]
	file2_name = sys.argv[2]

	file1 = open(file1_name, 'r')
	file2 = open(file2_name, 'r')

	data1 = []
	data2 = []

	for line in file1:
		data1.append(line)

	for line in file2:
		data2.append(line)

	file1.close()
	file2.close()

	same = 'Files are the same'
	for i, d in enumerate(data1):
		if data1[i] != data2[i]:
			print('file1: ' + data1[i])
			print('file2: ' + data2[i])
			same = 'Files are different'

	print(same)

if __name__ == '__main__':
	main()
