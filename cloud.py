import time, os
import pyfirmata
import httplib, urllib

def subealanube(sensor0, sensor1):
    params = urllib.urlencode({'field1': sensor0, 'field2': sensor1, 'key’:’YOURKEY’})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    conn.close()

#Please check the device name of the USB port.
board = pyfirmata.Arduino('/dev/ttyACM0')
analog_pin0 = board.get_pin('a:0:i')
analog_pin1 = board.get_pin('a:1:i')

it = pyfirmata.util.Iterator(board)
it.start()
analog_pin0.enable_reporting()
analog_pin1.enable_reporting()
while True:
 reading0 = analog_pin0.read()
 reading1 = analog_pin1.read()
 if reading0 != None:
  humedad0 = (1- reading0) * 100.0
  humedad1 = (1- reading1) * 100.0
  print("Humedad0=%f\tHumedad1=%f" % (humedad0, humedad1))
  subealanube(humedad0,humedad1)
  break
print 'Fuera del loop'

board.exit()
