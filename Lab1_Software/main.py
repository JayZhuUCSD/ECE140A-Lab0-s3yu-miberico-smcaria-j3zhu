# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time
import sys

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT


# Software SPI configuration:
#CLK  = 18
#MISO = 23
#MOSI = 24
#CS   = 25
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# print('Reading MCP3008 values, press Ctrl-C to quit...')
# # Print nice channel column headers.
# print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} ||'.format(*range(8)))
# print('-' * 57)
# Main program loop.
sensor = Adafruit_DHT.DHT22
pin = 4
curr = time.time()
pre = curr - 60
i = 0
light = []
gate = []
audio = []
envelop = []
temp = []
humid = []
while i < 60:
	curr = time.time()
	if curr - pre >= 60:
		pre = curr
		# Read all the ADC channel values in a list.
		# values = [0]*8
		# for j in range(8):
		#     # The read_adc function will get the value of the specified channel (0-77).
		#     values[j] = mcp.read_adc(j)
		for j in range(4):
			print(mcp.read_adc(j))
		light.append(mcp.read_adc(0))
		gate.append(mcp.read_adc(1))
		envelop.append(mcp.read_adc(2))
		audio.append(mcp.read_adc(3))
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		temp.append(int(temperature))
		humid.append(int(humidity) if humidity else 0 )
		# Print the ADC values.
		s = '\nTime = ' + time.strftime("%H:%M:%S", time.localtime()) + '\nTemp = ' + str(temp[-1]) + '\nHum = '+str(humid[-1])+ \
			'%\n' + 'Light = '+ str(light[-1]) \
			+ '\nGate = ' + str(gate[-1]) + '\nEnvelop = ' + str(envelop[-1]) + '\nAudio = '+str(audio[-1])
		file = open('record.txt','a+')
		file.write(s)

		i += 1

	# Pause for half a second.
	time.sleep(5)
s = 'light: ' + str(light) + '\nGate: ' + str(gate) + '\nEnvelop: ' + str(envelop) + '\nAudio: ' + str(audio) + '\nHum: ' + str(humid) + '\nTemp: ' + str(temp)
data = open('data.txt','a+')
data.write(s)