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
1. Overclock from 1400 to 1550 MHZ, reduce video memory to 16 Mb, by replacing "config.txt" with
    ```
    temp_soft_limit=70
    arm_freq=1550
    gpu_freq=500
    core_freq=500
    sdram_freq=500
    sdram_schmoo=0x02000020
    over_voltage=6
    sdram_over_voltage=2

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

