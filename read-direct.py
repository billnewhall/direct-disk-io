# Read directly from disk without file system
#
# W. Newhall 1/2020 original

import argparse
import os

def main():

    # Get arguments from command line
    parser = argparse.ArgumentParser(description='Read bytes directly from drive')
    parser.add_argument('phys_drive', type=str, help="Physical drive (e.g., sde for Linux or 2 for Windows)")
    parser.add_argument('start_byte', type=int, help="Byte index to start reading (0 is first byte)")
    parser.add_argument('num_bytes', type=int, help="Number of bytes to read")
    args = parser.parse_args()

    drive_name = create_drive_name(args.phys_drive)

    #drive_name = "/dev/sde"
    #drive_name = '\\\\.\\PhysicalDrive2'
    #drive_name = '\\\\.\\F:'

    print(drive_name)
    drive_data = read_drive(drive_name, args.start_byte, args.num_bytes)
    for data_byte in drive_data:
        print("{:02x} ".format(data_byte), end = '')
    print("")

def create_drive_name(phys_drive):
    # Determine they drive name to use based on the operating system.
    # For Windows, the physcial drive number must be used (0, 1, 2, etc.).
    if os.name == 'posix':  # Running on Linux
        drive_name = '/dev/' + phys_drive
    elif os.name == 'nt':   # Running on Windows
        drive_name = r'\\.\\PhysicalDrive%s' % phys_drive
    else:
        raise Exception('Unable to determine drive name on this operating system.')
    return drive_name

def read_drive(drive_name, start_byte, num_bytes):
    # Read data from drive named drive_name.  Start with start_byte
    # and read num_bytes of bytes.
    with open(drive_name,'rb') as h_file:
        h_file.seek(2)
        drive_data = h_file.read(num_bytes)
        h_file.close()
        return drive_data


if __name__ == '__main__':
    main()