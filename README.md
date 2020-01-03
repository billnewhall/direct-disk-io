# direct-disk-io
Read and write bytes directly to disk (even unformatted or unpartitioned)


# Determine Physical Drives in Windows

PS E:\git\direct-disk-io> Get-WmiObject Win32_DiskDrive

```
Partitions : 1
DeviceID   : \\.\PHYSICALDRIVE1
Model      : Samsung Portable SSD T5 SCSI Disk Device
Size       : 500105249280
Caption    : Samsung Portable SSD T5 SCSI Disk Device

Partitions : 4
DeviceID   : \\.\PHYSICALDRIVE0
Model      : Micron 1100 SATA 256GB
Size       : 256052966400
Caption    : Micron 1100 SATA 256GB

Partitions : 0
DeviceID   : \\.\PHYSICALDRIVE2
Model      : TS-RDF5 SD  Transcend USB Device
Size       : 31914086400
Caption    : TS-RDF5 SD  Transcend USB Device
```
