# LMS 7.x.x on RaspberryPi
Install any version of Logitech Media Server on RaspberryPi, without monitor and without ethernet 
(Raspberry 3 A+)

## Install Raspbian
1. Download Raspbian lite from https://www.raspberrypi.org/software/operating-systems/
1. Write to SD card (e.g. with Balena Etcher https://www.balena.io/etcher/)

## Configure Wifi and SSH
1. Create an empty "ssh.txt" file on the boot partition
1. Create a "wpa_supplicant.conf" file which contains
    ```
    country=IT
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

    network={
      ssid="WIFI_NAME"
      psk="WIFI_PASSWORD"
      key_mgmt=WPA-PSK
    }
    ```
1. Replace "config.txt" with
    ```
    #overscan_bottom=16

    # uncomment to force a console size. By default it will be display's size minus
    # overscan.
    #framebuffer_width=1280
    #framebuffer_height=720

    # uncomment if hdmi display is not detected and composite is being output
    #hdmi_force_hotplug=1

    # uncomment to force a specific HDMI mode (this will force VGA)
    #hdmi_group=1
    #hdmi_mode=1

    # uncomment to force a HDMI mode rather than DVI. This can make audio work in
    # DMT (computer monitor) modes
    #hdmi_drive=2

    # uncomment to increase signal to HDMI, if you have interference, blanking, or
    # no display
    #config_hdmi_boost=4

    # uncomment for composite PAL
    #sdtv_mode=2

    #uncomment to overclock the arm. 700 MHz is the default.
    #arm_freq=800
    temp_soft_limit=70
    arm_freq=1550
    gpu_freq=500
    core_freq=500
    sdram_freq=500
    sdram_schmoo=0x02000020
    over_voltage=6
    sdram_over_voltage=2



    # Uncomment some or all of these to enable the optional hardware interfaces
    #dtparam=i2c_arm=on
    #dtparam=i2s=on
    #dtparam=spi=on

    # Uncomment this to enable infrared communication.
    #dtoverlay=gpio-ir,gpio_pin=17
    #dtoverlay=gpio-ir-tx,gpio_pin=18

    # Additional overlays and parameters are documented /boot/overlays/README

    # Enable audio (loads snd_bcm2835)
    dtparam=audio=on

    [pi4]
    # Enable DRM VC4 V3D driver on top of the dispmanx display stack
    dtoverlay=vc4-fkms-v3d
    max_framebuffers=2

    [all]
    #dtoverlay=vc4-fkms-v3d
    gpu_mem=16
    ```


## Log in with SSH
1. If needed, find IP_ADDRESS of RaspberryPi with "Advance IP scanner"
1. Log in in SSH, using Putty or MobaXterm. User "pi", password "raspberry". Change it if needed


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


## Install LMS
Taken from https://www.hagensieker.com/wordpress/2018/06/12/302/
1. `sudo apt install libio-socket-ssl-perl libnet-libidn-perl libnet-ssleay-perl perl-openssl-defaults`
1. Find a LMS version you like from https://downloads.slimdevices.com/nightly/?ver=7.9
1. `wget https://downloads.slimdevices.com/nightly/7.9/sc/776e969ec5f8101f20f7687f525d42674ea52900/logitechmediaserver_7.9.4~1603273368_arm.deb`
1. `sudo dpkg -i logitechmediaserver_7.9.4~1603273368_arm.deb`

## Configure LMS
1. Connect to http://IP_ADDRESS:9000/ to configure the server
1. Set Interface Title format: "TRACKNUM. TITLE (TRACKSTATRATINGDYNAMIC)"
1. Leave only these plugins:
    * AudioScrobbler - to save played songs to last.fm
    * DontStopTheMusic
    * Programma di gestione di servizi mysqueezebox.com
    * InternetRadio
    * Rescan - Rescan library at 3 am
1. Install these plugins:
    * Trackstat - it will use automatically any backup in the playlists folder
    * Material Skin - accessible on http://IP_ADDRESS:9000/material
    * Music and Artist Information - to get artist photo
    * Lastmix - to continue playing songs


## On every client
1. Use Smart Gain
1. Use LastMix Don't stop the music
1. Use Audioscrobbler

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
