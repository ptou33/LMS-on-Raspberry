

# Install Squeezelite
1. Download: `wget https://sourceforge.net/projects/lmsclients/files/squeezelite/linux/squeezelite-1.9.9.1372-armhf.tar.gz`
1. Unzip and move executable `tar -xzf squeezelite-1.8.7.1053-armv6hf.tar.gz && sudo mv squeezelite /usr/bin/squeezelite`

1. To start automatically squeezelite: `sudo nano /etc/systemd/system/squeezelite.service`
    ```
    [Unit]
    Description=Squeezelite

    After=network.target

    [Service]
    ExecStart=/usr/bin/squeezelite -o hw:CARD=Headphones,DEV=0 -n Raspberry

    [Install]
    WantedBy=multi-user.target
    ```
1. Create a script to start squeezelite according to desired interface `nano start_squeezelite.sh`
    ```
        if squeezelite -l | grep -q "LS50"; then
        echo "squeezelite using LS50"
        squeezelite -o hw:CARD=Speaker,DEV=0 -n Raspberry
        exit $?
    else
        echo "squeezelite using Raspberry internal headphone"
        squeezelite -o hw:CARD=Headphones,DEV=0 -n Raspberry
        exit $?
    fi
    ```
1. Use `alsamixer` to set the volume for the device (it starts very low)

