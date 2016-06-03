LED controlling on Raspberry Pi
===============================

Only for demonstration
-----------------------

Tested on Raspbian version 2016-05-27, should work on other debian based system or so.

### Install dependencies

1. `sudo apt-get install python-pip python-dev wiringpi`
2. `pip install -r requirements.txt`

### Attach a LED for testing

Attach a LED and a 220--400 Ohm resistor to Raspberry Pi.

Long leg of LED light -> Pin 18 (GPIO) on Raspberry Pi

Short leg of LED light -> Pin GND on Raspberr Pi


This is tested on Raspberry Pi 1 B+ but it should also work on Raspberry Pi 2 / 3 B+ and later on.

![image](http://cnlearn.linksprite.com/wp-content/uploads/2014/01/%E5%9B%BE%E7%89%871.png)

### Light on and light off

#### In Python

> Notice: Python `wiringpi` needs **super user** privilege while commands in bash don't

```
sudo python blink.py
```

#### In binary from bash

```
bash blink.sh
```

Then you will see the LED light blinks every 1 second.

##### Happy hacking
