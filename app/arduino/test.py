import sys
import time
from pymata4 import pymata4

DISTANCE_CM = 2
TRIGGER_PIN = 9
ECHO_PIN = 10

def the_callback(data):
    distance = data[DISTANCE_CM]
    print(f'Distance in cm: {distance}')
    # Write the latest distance to a file
    with open("new.txt", "w") as file:
        file.write(f'{distance}')

def sonar(my_board, trigger_pin, echo_pin, callback):
    my_board.set_pin_mode_sonar(trigger_pin, echo_pin, callback)
    while True:
        try:
            time.sleep(.01)
            print(f'data read: {my_board.sonar_read(TRIGGER_PIN)} cm')
        except KeyboardInterrupt:
            my_board.shutdown()
            sys.exit(0)

board = pymata4.Pymata4()
try:
    sonar(board, TRIGGER_PIN, ECHO_PIN, the_callback)
    board.shutdown()
except (KeyboardInterrupt, RuntimeError):
    board.shutdown()
    sys.exit(0)
