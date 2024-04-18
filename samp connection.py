from gpiozero import LED

from gpiozero.pins.pigpio import PiGPIOFactory

from time import sleep
import keyboard

factory = PiGPIOFactory('192.168.1.3',8888)

c = LED(14,pin_factory=factory)
a = LED(15,pin_factory=factory)
l = LED(23,pin_factory=factory)
r = LED(24,pin_factory=factory)

while True:
    if keyboard.is_pressed('up'):
            c.on()
    elif keyboard.is_pressed('down'):
            a.on()
    elif keyboard.is_pressed('left'):
            l.on()
    elif keyboard.is_pressed('right'):
            r.on()
    else:
        a.off()
        c.off()
        l.off()
        r.off()
    sleep(0.1)  



