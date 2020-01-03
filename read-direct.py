#!/usr/bin/env python
"""Reads binary data.

Read and print binary data from a file or from a disk (even unformatted, if on linux).

    Typical usage:

    Read 25 bytes from the start of a binary file:
    python read-direct.py testfile.bin 0 25

    Read 10 bytes from a binary file starting at byte 2 (third byte) (first 
    byte is position 0):
    python read-direct.py testfile.bin 2 10

    Linux
    =====

    To deterimine windows physical drive in Linux:  
    $ sudo lsblk

    Read 10 bytes from a binary file starting at byte 2 (third byte) (first 
    byte is position 0):
    python read-direct.py /dev/sde 2 10

    Windows
    =======

    To deterimine windows physical drive in PowerShell:  
    Get-WmiObject Win32_DiskDrive

    Read 10 bytes from an unformatted Windows drive starting at byte 0 (first
    byte):
    python read-direct.py \\.\PHYSICALDRIVE2 0 10
    (Fails in Windows if start byte is not 0 due to failure to read() after 
    seek() function is called -- don't know why)

W. Newhall 1/2019 (original)
"""

import argparse
import os


def main():

    # Get arguments from command line
    parser = argparse.ArgumentParser(description='Read bytes directly from drive')
    parser.add_argument('data_source', type=str, help="File name or drive (e.g., /dev/sde for Linux or \\\\.\\PhysicalDrive2 for Windows)")
    parser.add_argument('start_byte', type=int, help="Byte index to start reading (0 is first byte)")
    parser.add_argument('num_bytes', type=int, help="Number of bytes to read")
    args = parser.parse_args()

    data_source = args.data_source
    start_byte = args.start_byte
    num_bytes = args.num_bytes

    print("Getting data from {}.".format(data_source))
    source_data = read_source(data_source, start_byte, num_bytes)

    n_byte = 0
    for data_byte in source_data:
        print("{:02X} ".format(data_byte), end = '')
        n_byte = n_byte + 1
        if (n_byte % 10) == 0:
            print("")   # CR/LF every 10 columns
    print("")


def read_source(source_name, start_byte, num_bytes):

    # Read data from the source.  Start with <start_byte>
    # and read <num_bytes> of bytes.
    with open(source_name, 'rb') as h_file:
        h_file.seek(start_byte, 0)
        source_data = h_file.read(num_bytes)
        h_file.close()
        return source_data


if __name__ == '__main__':
    main()