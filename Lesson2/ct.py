from microbit import *
import radio

radio.on()
radio.config(group=1)

light_sensor = pin0
pir_sensor = pin1
servo = pin2
buzzer = pin3
crash_sensor = pin4
noise_sensor = pin5
temp_sensor = pin6
led = pin9

def set_servo(angle):
    duty = int((angle / 180) * 102 + 26)
    servo.write_analog(duty)

while True:

    # LIGHTING SYSTEM (automatic)
    light_level = light_sensor.read_analog()
    if light_level < 300:
        led.write_digital(1)
    else:
        led.write_digital(0)

    # MOTION SECURITY
    if pir_sensor.read_digital() == 1:
        buzzer.write_digital(1)
        set_servo(90)
        display.show("M")
        radio.send("MOTION DETECTED")
        sleep(1000)
    else:
        buzzer.write_digital(0)
        set_servo(0)

    # DOOR SENSOR (intrusion)
    if crash_sensor.read_digital() == 1:
        buzzer.write_digital(1)
        display.show("D")
        radio.send("DOOR OPENED")
        set_servo(90)
        sleep(1000)

    # SOUND DETECTION
    if noise_sensor.read_analog() > 600:
        display.show("N")
        radio.send("LOUD NOISE")
        sleep(500)

    # TEMPERATURE MONITORING
    temp = temperature()
    if temp > 28:
        display.show("H")
        radio.send("HOT")
    elif temp < 18:
        display.show("C")
        radio.send("COLD")
    else:
        display.show("OK")

    sleep(500)