#!/bin/bash
if [ $1 == "start" ]; then
	echo "########  ########  ####    ########   #######  ##     ## ######## ########"  
	echo "##     ## ##     ##  ##     ##     ## ##     ## ##     ## ##       ##     ##"
	echo "##     ## ##     ##  ##     ##     ## ##     ## ##     ## ##       ##     ##" 
	echo "########  ########   ##     ########  ##     ## ##     ## ######   ########"  
	echo "##   ##   ##         ##     ##   ##   ##     ##  ##   ##  ##       ##   ##"   
	echo "##    ##  ##         ##     ##    ##  ##     ##   ## ##   ##       ##    ##"  
	echo "##     ## ##        ####    ##     ##  #######     ###    ######## ##     ##" 
	echo "Startng camera interface"
	bash /home/pi/RPi_Cam_Web_Interface/start.sh
	echo "Done"
	echo "Starting Motor Control interface"
	sudo python ./MotorControl.py
elif [ $1 == "stop" ]; then 
	echo "Stopping camera interface"
	bash /home/pi/RPi_Cam_Web_Interface/stop.sh
	echo "Done"
fi
