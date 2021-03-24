
# Install LMS
Taken from https://www.hagensieker.com/wordpress/2018/06/12/302/
1. `sudo apt install libio-socket-ssl-perl libnet-libidn-perl libnet-ssleay-perl perl-openssl-defaults`
1. Find a LMS version you like from https://downloads.slimdevices.com/nightly/?ver=7.9
1. Download "arm.deb" package: `wget https://downloads.slimdevices.com/nightly/7.9/sc/776e969ec5f8101f20f7687f525d42674ea52900/logitechmediaserver_7.9.4~1603273368_arm.deb`
1. Install it: `sudo dpkg -i logitechmediaserver_7.9.4~1603273368_arm.deb`

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
