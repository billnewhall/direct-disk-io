# Read directly from disk without file system
#
# W. Newhall 1/2020 original




print("You really don't want to use this unless you REALLY know what you're doing!")
exit()




drive_name = "/dev/sde"

#with open(drive_name,'rb+') as h_file:
with open(drive_name,'wb') as h_file:
    print("Writing a byte")
    #write_val = bytearray(10)
    #h_file.write(write_val)
    h_file.seek(4)
    h_file.write(b'\x04')
    print("Wrote a byte")
    h_file.close()

with open(drive_name,'rb') as h_file:
    vals = list(h_file.read(10))
    for val in vals:
        print("{:02x} ".format(val), end = '')
    print("")
    h_file.close()
