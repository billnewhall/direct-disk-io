#!/usr/bin/env python
"""Creates a binary file for testing.

File contains zeros plus an optional specified series of bytes at the start.

    Typical usage:

    Creates a file with 100 bytes, and all bytes are zeros:
    python write-test-bin-file.py testfile.bin 100

    Creates a file with 100 bytes, and all bytes are zeros except for
    the first four bytes, which are 10, 11, 12, 255 (0x0A, 0x0B, 0x0C, 
    and 0xFF):
    python write-test-bin-file.py testfile.bin 100 --first-bytes 10 11 12 255

W. Newhall 1/2019 (original)
"""

import os
import argparse


def main():
    # Get arguments from command line
    parser = argparse.ArgumentParser(description='Writes a binary file of specified for testing (written data is all zeros)')
    parser.add_argument('file_name', type=str, help="Name of file to write")
    parser.add_argument('num_bytes', type=int, help="Number of bytes to write")
    parser.add_argument('--first-bytes', type=int, nargs='+', help="Number of bytes to write")
    args = parser.parse_args()
    file_name = args.file_name
    num_bytes = args.num_bytes
    if args.first_bytes is not None:
        first_bytes = args.first_bytes


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
        if 'first_bytes' in locals():   # If first bytes specified, write them
            h_file.seek(0)
            h_file.write(bytearray(first_bytes))
        h_file.close()
        print("File closed.")


if __name__ == '__main__':
    main()