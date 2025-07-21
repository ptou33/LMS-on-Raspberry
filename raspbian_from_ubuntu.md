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
