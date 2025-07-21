On linux (ubuntu)

  sudo apt install rpi-imager

to enable X11 forwarding when running sudo
  xhost +local:

run imager as root to be able to write to sd card
  sudo -E rpi-imager
