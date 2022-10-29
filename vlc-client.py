import RPi.GPIO as GPIO
import time
import sys
import telnetlib

# constants
GPIO_PIN = 13  # change according to your wiring
INFINITE_PERIOD = 10000
VLC_HOST = "localhost"
VLC_PORT = 9999
VLC_PASSW = "abc123"

# vars
last_tick = 0
period = INFINITE_PERIOD
speed = 0
paused = True

# inits
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN, GPIO.PUD_DOWN)
tn = telnetlib.Telnet(VLC_HOST, VLC_PORT)

# script params
videoFile = sys.argv[1]
seek = sys.argv[2]

def state_interrupt(GPIO_PIN):
    if GPIO.input(GPIO_PIN) == GPIO.HIGH:
    	play_video_according_to_speed()
    return

GPIO.add_event_detect(GPIO_PIN, GPIO.RISING, callback=state_interrupt, bouncetime=5)

def play_video_according_to_speed():
	global last_tick
    	global period
        global speed
	global paused
	global INFINITE_PERIOD

    	period = time.time()-last_tick

	if period > INFINITE_PERIOD:
		period = INFINITE_PERIOD

    	last_tick = time.time()

    	if period > 0.1:   # workaround for rpi gpio debounce bug
		if paused == True:
			tn.write("play\n")
			paused = False

                speed = float("{0:.2f}".format(1/period))

		if speed > 3:
			speed = 3

		print "Speed ", speed

		tn.write("rate " + str(speed) + "\n")

    	time.sleep(0.05)

def initialize_video():
	print "[VLC] Adding video file"
	tn.write("add " + videoFile + "\n")
	time.sleep(5)

	print "[VLC] Seeking ", seek, " seconds"
	tn.write("seek " + str(seek) + "\n")
	time.sleep(0.5)

	print "[VLC] Switching to fullscreen"
	tn.write("fullscreen\n")
	time.sleep(0.1)

	print "[VLC] Pausing until speeding is detected"
	tn.write("pause\n")
	time.sleep(0.1)
        paused = True

def vlc_login():
	print "[VLC] Authenticating"
	line = tn.read_until("Password:")
	tn.write(VLC_PASSW + "\n")
	time.sleep(0.1)

def cleanup():
	GPIO.cleanup([GPIO_PIN])
        print "[VLC] Adding video file"
	tn.write("stop\n")
	time.sleep(0.1)
        tn.write("quit\n")
        print "Resources closed" 

def main():
    try:
	vlc_login()
	initialize_video()

        while True:
            pass

    except KeyboardInterrupt:
        pass
    finally:
        cleanup()


if __name__ == '__main__':
    main()