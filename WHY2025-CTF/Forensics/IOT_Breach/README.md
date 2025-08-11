## IOT Breach

- Extarct image.img.gz 
```bash
7z x image.img.gz
```
- Mount the filesystem
```bash
image: DOS/MBR boot sector; partition 1 : ID=0xee, start-CHS (0x0,0,2), end-CHS (0x3ff,255,63), startsector 1, 2097151 sectors, extended partition table (last)
[avelin@byzantium Forensics]$ fdisk -l soal
Disk soal: 1 GiB, 1073741824 bytes, 2097152 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 87C45929-6BB7-4A2E-8B3A-57CF8E4EF775

Device  Start     End Sectors  Size Type
image    2048  329727  327680  160M EFI System
image  329728  854015  524288  256M Linux swap
image  854016 2095103 1241088  606M Linux filesystem
[avelin@byzantium Forensics]$
```
```
Offset = Start sector × 512
Offset = 854016 × 512 = 437379072 bytes
```
Then

```bash
sudo mount -o loop,offset=437379072 image /mnt
```
- There is an encrypted files in the files directory, checking __var/log/lighttpd/access.log__ got interesting clue, an attacker using compromised ping perl script to perform command injection for encrypting victim files. 

Got password _L0s3@llYourF1l3s_ and IV _R4ND0MivR4ND0Miv_ from the logs

- Solve

```bash
cd files
python decrypt.py L0s3@llYourF1l3s
```

![Flag](docs/flag.jpg)
