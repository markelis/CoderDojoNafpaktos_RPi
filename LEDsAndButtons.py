# -*- coding: utf-8 -*-
from gpiozero import LED
from time import sleep
ledR = LED(14)
ledG = LED(15)
ledB = LED(17)
while True:
	ledR.on()
	ledG.on()
	ledB.on()
	sleep(0.1)
	ledR.on()
	ledG.off()
	ledB.off()
	sleep(0.5)
	ledR.off()
	ledG.on()
	ledB.off()
	sleep(0.1)
	ledR.off()
	ledG.off()
	ledB.on()
	sleep(0.5)
