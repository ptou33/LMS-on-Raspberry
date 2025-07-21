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
https://lyrion.org/getting-started/beginners-guide-qnap-docker/#assumptions

    services:
        lms:
            image: lmscommunity/lyrionmusicserver
            volumes:
                - /share/Container/app-data/lms-config/:/config:rw
                - /share/Multimedia/Music/:/mnt/fritz.nas/5TB/music:ro
                - /share/Multimedia/Playlists/LMS/:/mnt/fritz.nas/5TB/playlist:rw
            ports:
                - "9000:9000"
                - "9090:9090"
                - "3483:3483/udp"
                - "3483:3483/tcp"
