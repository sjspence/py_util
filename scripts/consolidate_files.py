#!/usr/bin/env python

import os
import argparse

def main(options):

	if not os.path.exists(options.out_dir):
		os.makedirs(options.out_dir)

	for subdir, dirs, files in os.walk(options.in_dir):
		for d in dirs:
			if 'Sheets' in d:
				continue
			cmd = 'cp '
			cmd += options.in_dir + d + '/* '
			cmd += options.out_dir
			print(cmd)
			os.system(cmd)

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	parser.add_argument("-i", "--in_dir", action='store', required=True,
					  help="Input directory.",
					  metavar="INPUT")
	parser.add_argument("-o", "--out_dir", action='store', required=True,
					  help="Output directory.",
					  metavar="OUTPUT")

	options = parser.parse_args()
	
	main(options)