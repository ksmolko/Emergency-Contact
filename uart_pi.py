import time
import serial
import send_sms as contact

serialPort = "ENTER_SERIAL_PORT_HERE" # ex: /dev/ttyACM0

toNum = "ENTER_TO_NUMBER_HERE"
fromNum = "ENTER_TWILIO_NUMBER_HERE"

port = serial.Serial(serialPort, baudrate=9600, timeout=3.0)

while True:
	data = port.read(10)
	print(data)
	if(int(data) > 525):
		contact.sendSMS(toNum, fromNum)
		time.sleep(10)
		port.read(20)
		time.sleep(2)
	
