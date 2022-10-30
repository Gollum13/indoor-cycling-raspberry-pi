# indoor-cycling-raspberry-pi

Revive your fitness bike by adding real world road trips: pedal in front of your TV or monitor, and promenade on the roads faster or slower according to your cycling speed. 
No need for any trainer or app, you just need a fitness bike, a raspberry pi (any model), and a homemade cadence sensor (shown below)

## Components
- A fitness bike (I suppose you already have it)
- A Raspberry Pi, any model above 2 (VLC should play smoothly on it)
- A magnetic sensor (for example [PS-3150](https://www.amazon.com/PS-3150-Normally-Proximity-Magnetic-Contacts/dp/B07T8NF29J) or [KY-021](https://www.ebay.com/itm/382537951441) but honestly any other cheap magnetic sensor should work)
- Neodimium magnets (1 or 2 pieces), an example [here](https://www.amazon.com/DIYMAG-Refrigerator-Neodymium-Whiteboard-Billboard/dp/B09X1WWD3P/ref=sr_1_19?crid=3PDPO0IT7OP34&keywords=neodymium+magnet&qid=1667128351&qu=eyJxc2MiOiI3LjMwIiwicXNhIjoiNy4xMSIsInFzcCI6IjYuODYifQ%3D%3D&sprefix=neodimium%2Caps%2C259&sr=8-19)
- The scripts in this repository, which you need to copy on Raspberry
- A video file recording of your favourite road trip

## Scripts

**vlc-server.sh** -> starts the VLC's telnet server, which will be used to receive commands by the client script

**vlc-client.py** -> starts the client script, which is doing everything we need: connects to VLC telnet server and sends framerate commands based on values reads from our cadence sensor

**start.sh** -> the main script, which first starts the VLC server then the client script. This is the script you need to run. But before, you need to edit it and change the video file name and the seek value (the seconds you want to skip from the beginning of the file) 

## How it works

The idea behind this solution is to play a video file in VLC and control the frame rate (FPS) according to the speed we get from the pedal. In this matter, we build a simple cadence sensor, and attach it to one of the pedals. The sensor then sends the pulses on one GPIO input pin of Raspberry Pi, and then, based on the period we receive these pulses, we compute some speed. Finally, based on the value of the speed, we control VLC frame-rate

Fortunatelly, to control video playing in VLC is quite simple, we just need to start its embedded telnet server, to which we send commands from the client script.

## DIY Cadence sensor

The cadence sensor is the most important component, as it's attached to the pedal and "reads" the number of pedal rotations per minute.
It's composed of a magnetic sensor (attached to bike's shell) and a neodimium magnet (attached to the pedal). 

For the magnetic sensor I use a door sensor PS-3150, but you can use anything else, like the cheap KY-021

## Wiring

I'm using GPIO pin 13, which I set it as input pin. A cadence sensor is linked to this pin and VCC 3.3V pin

![Preview](https://github.com/Gollum13/indoor-cycling-raspberry-pi/blob/main/wiring.jpg)
