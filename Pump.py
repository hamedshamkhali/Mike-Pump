import sys
from urllib.request import urlopen
import serial
from time import sleep

# Enter Your API key here
myAPI = 'DUW2CPI1N3I6A8T0' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
#Serial port
ser = serial.Serial('/dev/ttyACM0',115200)
R=0
P=0

while True:
	
            read_serial=ser.readline()
            
            while (read_serial!=b'R0\r\n' and read_serial!=b'R1\r\n'):
                read_serial=ser.readline()
                print(read_serial)
                
                

            if (read_serial==b'R0\r\n'):
                print(read_serial)
                R=0
                P=0

            elif (read_serial==b'R1\r\n'):
                print(read_serial)
                read_serial=ser.readline()
                
                if (read_serial==b'P0\r\n'):
                    print(read_serial)
                    R=1
                    P=0
                
                elif (read_serial==b'P1\r\n'):
                    print(read_serial)
                    R=1
                    P=1
                else:
                    print('No pump data')
            # Sending the data to thingspeak
            conn=urlopen(baseURL + '&field1=%s&field2=%s' % (R, P))
            # Closing the connection
            conn.close()
            sleep(20)
       
