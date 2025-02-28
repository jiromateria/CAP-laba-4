import RPi.GPIO as gpio

dac = [ 8, 11, 7, 1, 0, 5, 12, 6 ]

gpio.setmode( gpio.BCM )

gpio.setup( dac, gpio.OUT )

def decimal2binary( value ):

    return[ int(bit) for bit in bin(value)[2:].zfill(8) ]

try:
    while True:
        value = input("Input number from 0 to 255: ")
        error_flag = False
        if value == "q":
            break
        try:
            value = int( value )
        
        except:
            if isinstance( value, str ):
                print("Value has to be a number, not a srting ")
            else:
                print("Value has to be int type ")
            error_flag = True
        
        if not(error_flag):
            if 0<= value <= 255:
                    bin_value = decimal2binary( value )
                    gpio.output( dac, bin_value )
                    voltage = float( value ) / 256 * 3.3
                    print( " Voltage is around ", voltage ,"volt")
            else:
                    if value < 0:
                        print( "Value has to be more than zero" )
                    else:
                        print( "Value has to be less than 255" )

finally:
    gpio.output( dac, 0 )
    gpio.cleanup()