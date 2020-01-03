# Read directly from disk without file system
#
# W. Newhall 1/2020 original

import os
import sys

drive_name = "/dev/sde"

with open(drive_name,'rb') as h_file:
    vals = list(h_file.read(10))
    for val in vals:
        print("{:02x} ".format(val), end = '')
    print("")
    h_file.close()

