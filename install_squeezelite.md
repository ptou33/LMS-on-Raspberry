

# Install Squeezelite
1. Download: `wget https://sourceforge.net/projects/lmsclients/files/squeezelite/linux/squeezelite-1.9.9.1372-armhf.tar.gz`
1. Unzip and move executable `tar -xzf squeezelite-1.8.7.1053-armv6hf.tar.gz && sudo mv squeezelite /usr/bin/squeezelite`
1. Create a script to start squeezelite according to desired interface `nano start_squeezelite.sh`
    ```
    #!/bin/bash

    if squeezelite -l | grep -q "LS50"; then
        echo "squeezelite using LS50"
        amixer -c 1 sset PCM 100%
        squeezelite -o hw:CARD=Speaker,DEV=0 -n Raspberry
        exit $?
    elif squeezelite -l | grep -q "SA9023"; then
        echo "squeezelite using Hifimediy Sabre SA9023"
        amixer -c 1 sset PCM 100%
        squeezelite -o hw:CARD=Audio,DEV=0 -n Raspberry
        exit $?
    else
        echo "squeezelite using Raspberry internal headphone"
        amixer -c 0 sset Headphone 100%
        squeezelite -o hw:CARD=Headphones,DEV=0 -n Raspberry
        exit $?
    fi
    ```
1. Make it executable `chmod +x start_squeezelite.sh`
1. Use `alsamixer` to set the volume for the device (it starts very low)

## Automatically start squeezelite
1. To start automatically squeezelite: `sudo nano /etc/systemd/system/squeezelite.service`
    ```
    [Unit]
    Description=Squeezelite
    After=network.target

    [Service]
    User=pi
    Group=pi
    WorkingDirectory=/home/pi
    ExecStart=/home/pi/start_squeezelite.sh

    [Install]
    WantedBy=multi-user.target
    ```
1. Enable the service `sudo systemctl enable squeezelite.service`
1. In alternative, add the the scritp at the end of file before the exit, using `sudo nano /etc/rc.local`


