import RPi.GPIO as gpio
import time

gpio.setmode( gpio.BCM )

dac = [ 8, 11, 7, 1, 0, 5, 12, 6 ]

gpio.setup( dac, gpio.OUT )

def decimal2binary( value ):

    return[ int(bit) for bit in bin(value)[2:].zfill(8) ]

try:
    period = float( input("Input a period ") )

    real_time = period / 256

    for i in range(20):
        for value in range(256):
            gpio.output( dac, decimal2binary(value) )
            time.sleep( real_time )

        for value in range( 255, -1, -1 ):
            gpio.output( dac, decimal2binary(value) )
            time.sleep( real_time )

finally:
    gpio.output( dac, 0 )
    gpio.cleanup()