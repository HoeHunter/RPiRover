#!/bin/bash
if [ -z $1 ]; then
	echo "Error, please include an argument [start/stop]"
elif [ $1 == "start" ]; then
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
	
	echo "Would you like the full version or easy version? [full/easy]"
	read selection
	
	if [ $selection == "full" ]; then
		echo "Starting full motor control interface"
		sudo python ./MotorControl.py
	elif [ $selection == "easy" ]; then
		echo "Starting easy motor control interface"
		sudo python ./EasyControl.py
	fi
elif [ $1 == "stop" ]; then 
	echo "Stopping camera interface"
	bash /home/pi/RPi_Cam_Web_Interface/stop.sh
	echo "Done"
fi
