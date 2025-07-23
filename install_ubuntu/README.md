Use balena etcher to burn and install Ubuntu on USB disk
After the installation, first thing to do open a terminal:
## Install sshd

    sudo apt install openssh-server
    sudo service ssh start

From now on you can perfrom the other configurations from remote ssh from Mobaxterm for example


## Disable lid suspend
After install, disable lid close suspend on laptop

    sudo nano /etc/systemd/logind.conf

Inside the file uncomment or add

    HandleLidSwitch=ignore
    HandleLidSwitchExternalPower=ignore
    HandleLidSwitchDocked=ignore


Exit the file and restart logind

    sudo service systemd-logind restart



## smbd Media folder share with smbd
Let's say we wanto do share Media folder in pietro home

    mkdir Media

Install and configure samba
    
    sudo apt install samba samba-common-bin
    sudo nano /etc/samba/smb.conf

add this text the end of the **smb.conf**

    [DellMedia]
        path = /home/pietro/Media
        read only = no
        public = no
        writable = yes

add share password to existing user

    sudo smbpasswd -a pietro

From now the share is visible on windows

## Install docker
from convenience script

    sudo apt install curl
    
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh

enable docker to be run without sudo

    sudo usermod -aG docker $USER
    newgrp docker

test it with

    docker run hello-world

now you can proceed with loading compose.yaml for services like navidrome, lms, jellyfin
copy the contents of [jellyfin compose.yaml](compose.yaml) into:

    nano compose.yaml

precreate the shared folders before starting the container
    
    mkdir jellyfin
    mkdir jellyfin/config
    mkdir jellyfin/cache

start docker compose, force recreate resets mapped

    docker compose up -d
    docker compose up -d --force-recreate

# Firefox does not forward into remote ssh X11 server

    sudo snap remove firefox
    sudo add-apt-repository ppa:mozillateam/ppa
    sudo apt update

disable snap for firefox
        
    echo '
    Package: *
    Pin: origin ppa.launchpad.net
    Pin-Priority: 501
    ' | sudo tee /etc/apt/preferences.d/mozilla-firefox

install firefox

    sudo apt remove firefox
    sudo apt install firefox

now it should work remotely
