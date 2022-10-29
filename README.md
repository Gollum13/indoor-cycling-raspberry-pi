# indoor-cycling-raspberry-pi

Revive your fitness bike by adding real world road trips: pedal in front of your TV or monitor, and promenade on the roads faster or slower according to your cycling speed. 
No need for any trainer or app, you just need a fitness bike, a raspberry pi (any model), and a homemade cadence sensor (shown below)

## Scripts

**vlc-server.sh** -> starts the VLC's telnet server, which will be used to receive commands by the client script

**vlc-client.sh** -> starts the client script, which is doing everything we need: connects to VLC telnet server and sends framerate commands based on values reads from our cadence sensor

**start.sh** -> the main script, which first starts the VLC server then the client script. This is the script you need to run. But before, you need to edit it and change the video file name and the seek value (the seconds you want to skip from the beginning of the file) 
