import asyncio
import sys
from pymata_express.pymata_express import PymataExpress

# This program continuously monitors an HC-SR04 Ultrasonic Sensor
# It reports changes to the distance sensed.
class SonarMonitor():
    def __init__(self):
        self.new_data=0
    # A callback function to display the distance
    async def the_callback(self,data):
        #print("Distance in cm: ", data[2])
        self.new_data=int(data[2])
        #print( self.new_data )
        
    
    def get_data(self):
        print( self.new_data ,"\t",end="")

    async def sonar(self,my_board, trigger_pin, echo_pin, callback):

        # set the pin mode for the trigger and echo pins
        await my_board.set_pin_mode_sonar(9, 10,callback)
        # wait forever
        while True:
            try:
                await asyncio.sleep(3)
            except KeyboardInterrupt:
                await my_board.shutdown()

s= SonarMonitor()
loop = asyncio.get_event_loop()
board = PymataExpress()
try:
    loop.run_until_complete(s.sonar(board, 9, 10, s.the_callback))
    loop.run_until_complete(board.shutdown())
except (KeyboardInterrupt, RuntimeError):
    loop.run_until_complete(board.shutdown())
    sys.exit(0)

