import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import time


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def main():
	GPIO.setmode(GPIO.BCM) #Set convention
	GPIO.setwarnings(False) #Dont print warnings
	GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)) #Set pin 18 to output
	alreadyOn = True #boll to keep track of current state of light
	
	while(true):
		if (mcp.read_adc(2)>900):
			clap= True
		else 
			clap=False
		if (clap):
			  if (!alreadyOn):     
					print ("LED ON") 
					GPIO.output(18,GPIO.HIGH) #Turn LED on
					alreadyOn = True
					time.sleep(1)
			   else:  
					Serial.println ("LED OFF")
					GPIO.output(18,GPIO.LOW) #Turn LED off
					alreadyOn= False
					time.sleep(1)

			 		  
main()
print("Main entered")

