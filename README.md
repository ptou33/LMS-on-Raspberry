# LMS 7.x.x on RaspberryPi
Install any version of Logitech Media Server on RaspberryPi, without monitor and without ethernet 
(Raspberry 3 A+)

## Install Raspbian and enable SSH
[Raspbian from Ubuntu](raspbian_from_ubuntu.md)
[OLD: Raspbian from Windows](raspbian_from_windows.md)


## Mount USB disk
Taken from https://www.raspberrypi.org/documentation/configuration/external-storage.md
1. Connect USB disk, list partitions with `sudo lsblk -o NAME,LABEL,UUID,FSTYPE,SIZE,MOUNTPOINT,MODEL` Read and remember UUID
1. If file system is NTFS, install `sudo apt install ntfs-3g` (maybe not needed)
1. Create mount point `sudo mkdir /mnt/DISK_NAME`
1. Mount it automatically adding lines to `sudo nano /etc/fstab`
    ```
    UUID=my_disk_uuid /mnt/DISK_NAME ntfs defaults,auto,users,rw,nofail,umask=000,x-systemd.device-timeout=30 0 0
    ```
1. Reload fstab without rebooting `sudo mount -a`

## Mount Fritzbox USB disk network share

    //192.168.178.1/fritz.nas /mnt/fritz.nas cifs username=fritznas,password=,uid=1000,gid=1000,file_mode=0775,dir_mode=0775,vers=3.1.1,x-systemd.automount,_netdev,actimeo=30,cache=none,noserverino 0 0

    //192.168.178.1/fritz.nas on /mnt/fritz.nas type cifs (rw,relatime,vers=3.1.1,cache=none,upcall_target=app,username=fritznas,uid=1000,forceuid,gid=1000,forcegid,addr=192.168.178.1,file_mode=0775,dir_mode=0775,soft,nounix,mapposix,reparse=nfs,nativesocket,symlink=native,rsize=65536,wsize=65536,bsize=1048576,retrans=1,echo_interval=60,actimeo=30,closetimeo=1,x-systemd.automount,_netdev)

    //192.168.178.1/fritz.nas /mnt/fritz.nas cifs username=fritznas,password=,uid=1000,gid=1000,file_mode=0775,dir_mode=0775,vers=3.1.1,x-systemd.automount,_netdev,actimeo=30,cache=none,noserverino,soft

## Install Samba
Taken from https://www.raspberrypi.org/documentation/remote-access/samba.md and https://pimylifeup.com/raspberry-pi-samba/
1. `sudo apt install samba samba-common-bin`
1. Do not use WINS when asked
1. Add these lines at the end of file `sudo nano /etc/samba/smb.conf`
    ```
    [DISK_NAME]
        path = /mnt/DISK_NAME
        read only = no
        public = no
        writable = yes
    ```
1. Set a password `sudo smbpasswd -a pi`
1. Connect from windows to "\\\IP_ADDRESS\DISK_NAME", with user pi and password


## Overclock Raspberry 3 A+
2. to monitor frequency and temperature: `watch -n 0 "vcgencmd measure_clock arm && vcgencmd  measure_temp"`
3. to overclock add these line to `sudo nano /boot/config.txt`
     ```
    temp_soft_limit=70
    arm_freq=1550
    gpu_freq=500
    core_freq=500
    sdram_freq=500
    sdram_schmoo=0x02000020
    over_voltage=6
    sdram_over_voltage=2
     ```
 
## Remove swap file
To reduce sd-card wear, disable the default 100MB swap file
```
sudo dphys-swapfile swapoff && \
sudo dphys-swapfile uninstall && \
sudo systemctl disable dphys-swapfile
```

