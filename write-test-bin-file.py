#!/usr/bin/env python
# --------------------------------------------------------
# Creates a binary file for testing.  File length is zero.
#
# W. Newhall 1/2020 original
# --------------------------------------------------------


import os
import argparse


def main():
    # Get arguments from command line
    parser = argparse.ArgumentParser(description='Writes a binary file of specified for testing (written data is all zeros)')
    parser.add_argument('file_name', type=str, help="Name of file to write")
    parser.add_argument('num_bytes', type=int, help="Number of bytes to write")
    args = parser.parse_args()
    file_name = args.file_name
    num_bytes = args.num_bytes

    # Check if file exists.  If so, quit.
    if os.path.isfile(file_name):
        print('File already exists.  Will not write over existing file.  Quitting.')
        quit()

    print("Writing to file: {}".format(file_name))

    # Open file and write zeros
    with open(file_name,'wb') as h_file:
        print("File opened.")
        vals = bytearray(num_bytes)
        h_file.write(vals)
        print("Wrote {} zeros.".format(num_bytes))
        h_file.close()
        print("File closed.")


if __name__ == '__main__':
    main()