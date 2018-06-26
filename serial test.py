import serial
import time
#import serial.tools.list_ports

# Things to note
#~~~~~~~~~~~~~~~~
# Commands sent to devices need to be in binary format 

#Check which COM ports are being used, use the first comport
#comport = serial.tools.list_ports.comports()[0]


ser = serial.Serial(
    port = 'COM1', # Or port = comport
    baudrate=9600, 
    parity='N',    
    stopbits=1,
    bytesize=8,
    timeout=8
    )

def read_serial(ser):
	'''
    Check if there is data waiting to be read
    Read and return it.
    else return null string
    '''
	data_bytes = ser.inWaiting()
	if data_bytes:
		return ser.read(data_bytes)
	else:
		return ""


def type(command = '', ser = ser, delay = 0.5):
	'''
	Send a command down the channel 
	If output is too long, eg. show run, increase delay value
	'''
	#To convert string to binary and press enter after typing command
	command = command + '\r\n'
	command = str.encode(command)

	ser.write(command)
	time.sleep(delay)

#Commands to type, make sure that output is not too long
toType = [
	'enable',
	'terminal length 0',
	'show ip int br',
	'show vlan br',
	]

#Press enter to 'wake up' the switch
ser.write(b'\r\n')

#Opens txt file in append binary mode, creates a new file if file does not exist in os.getcwd()
with open('test.txt', 'ab') as txt:

	#Loops through commands in toType list
	for i in toType:
		type(i)
		time.sleep(0.5)
		txt.write(read_serial(ser))

	type('show run', delay = 3)
	txt.write(read_serial(ser))


#Closes the serial connection
ser.close()
