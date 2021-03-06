#!/usr/bin/env python

import sys

def checkFiles():
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

        same = 'Files are exactly the same'

        if len(data1) != len(data2):
                print('First file length: ' + str(len(data1)))
                print('Second file length: ' + str(len(data2)))
                same = 'Files are different lengths'
                return same

        differences = 0

        for i, d in enumerate(data1):
                if data1[i] != data2[i]:
                        print(data1[i])
                        print(data2[i])
                        differences += 1
                        same = 'Files have different data'

        print('First file length: ' + str(len(data1)))
        print('Second file length: ' + str(len(data2)))
        print('Number of lines with differences: ' + str(differences))

        return same

def main():
        message = checkFiles()
        print(message)

if __name__ == '__main__':
        main()
