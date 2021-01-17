# LMS-on-Raspberry
Install LMS on Raspberry without monitor and without ethernet from scratch. 
Ideal for Raspberry 3 A+

## Install Raspbian
1)  Download Raspbian lite from https://www.raspberrypi.org/software/operating-systems/
2)  Write to SD card (e.g. with Balena Etcher https://www.balena.io/etcher/)

## Configure Wifi and SSH
3)  Create an empty "ssh.txt" file on the boot partition
4)  Create a "wpa_supplicant.conf" file which contains
    ```
    country=IT
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

    network={
      ssid="FASTWEB-5GHZ"
      psk="pietrotou"
      key_mgmt=WPA-PSK
    }
    ```

