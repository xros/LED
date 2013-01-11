gpio export 18 out
gpio -g mode 18 out		#set pin 18 mode out
gpio -g write 18 1		#set pin 18 on
while true; do
	gpio -g write 18 0	#LED light off
	echo LED light is off
	sleep 1
	gpio -g write 18 1	#LED light on
	echo LED light is on
	sleep 1
done
