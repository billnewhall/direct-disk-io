# Read directly from disk without file system
# For testing small file ops.
#
# W. Newhall 1/2020 original

import os
import sys

drive_name = "\\\\.\\\\PhysicalDrive2"

#with open(drive_name,'rb') as h_file:
h_file = os.open(drive_name, os.O_RDONLY | os.O_BINARY)
vals = os.read(h_file, 10)
for val in vals:
    print("{:02x} ".format(val), end = '')
print("")
h_file.close()