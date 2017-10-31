#!/usr/bin/env python

import os

in_dir = 'TJ1708311-R1-48080230_Validation_Run_1/'
out_dir = 'SD2_SES_TJ1708311_validation_fastq/'

if not os.path.exists(out_dir):
	os.makedirs(out_dir)

for subdir, dirs, files in os.walk(in_dir):
	for d in dirs:
		if 'Sheets' in d:
			continue
		cmd = 'cp '
		cmd += in_dir + d + '/* '
		cmd += out_dir
		print(cmd)
		os.system(cmd)
