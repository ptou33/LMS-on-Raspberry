On linux (ubuntu), install imager

    sudo apt update
    sudo apt install rpi-imager

to enable X11 forwarding when running sudo:
    
    xhost +local:

run imager as root to be able to write to sd card
    
    sudo -E rpi-imager

choose Raspberry OS Lite 32 bit

configure
- user
- ssh
- wifi


To access network disk from Fritzbox:

    sudo apt install cifs-utils    
    sudo mkdir /mnt/fritz.nas/
    sudo mount -t cifs //192.168.178.1/fritz.nas /mnt/fritz.nas -o username=___,password=___,uid=pi,gid=pi

Docker compose for Lyrion (LMS)
[compose.yaml](compose.yaml)
https://hub.docker.com/r/lmscommunity/lyrionmusicserver
https://lyrion.org/getting-started/beginners-guide-qnap-docker/#assumptions


Start Docker compose

    docker compose up -d

To stop

    docker compose down

To update the image

    docker compose pull
