""" from kmk.keys import KC
import time
import board
from board import *
import digitalio
from analogio import AnalogIn
import time
import pwmio



def get_voltage(pin):
    # ピンの値を読み取り、電圧に変換
    return (pin.value * 3.3) / 65536

potentiometer = AnalogIn(board.A2)
led = digitalio.DigitalInOut(GP25)
led.direction = digitalio.Direction.OUTPUT
while True:
    led.value = True
    time.sleep(0.3)
    led.value = False
    time.sleep(0.3)
    print("Hello World!!")
    voltage = get_voltage(potentiometer)
    print("Voltage: {:.2f} V".format(voltage))

buzzer = pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=440, variable_frequency=True)
def play_tone(frequency, duration):
    buzzer.frequency = frequency
    buzzer.duty_cycle = 32768  # 50% Duty Cycle (0-65535 range)
    time.sleep(duration)
    buzzer.duty_cycle = 0  # Turn off the buzzer
while True:
    play_tone(1200, 1.0)  # 880 Hz (A5) の音を1秒間鳴らす """

import board
import neopixel
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules import Module
#import adafruit_ssd1306
import busio
from kmk.handlers.sequences import simple_key_sequence
import neopixel
import digitalio
import time
from kmk.extensions.rgb import RGB
from kmk.extensions import Extension
pixel_pin = board.GP15
num_pixels = 80  # 使用するNeoPixelの数
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=True)
i = 0


""" for k in range(num_pixels):
    
    pixels[k] = (255,255, 255)
    time.sleep(0.005)
time.sleep(1)
for k in range(num_pixels):
    pixels[k] = (0, 0, 0)
    time.sleep(0.005)
time.sleep(0.5) """
print("GO!")
p = 3
#R = [250] * num_pixels
#G = [0] * num_pixels
#B = [0] * num_pixels
t = 0
def rainbow(t):
    t = t%(250*7)
    #print(t)
    if t < 250:
        G = 0.6*t
        #print("1-2")
        return 250, G, 0
    elif 250 <= t and t< 250*2:
        G = 0.36*t+60
        #print("2-3")
        return 250, G, 0
    elif 250*2 <= t and t< 250*3:
        R = -t + 750
        G = -0.42*t+450
        #print("3-4")
        return R, G, 0
    elif 250*3 <= t and t< 250*4:
        G = 0.04*t+105
        B = t-750
        #print("4-5")
        return 0, G, B
    elif 250*4 <= t and t< 250*5:
        G = -0.18*t+325
        B = -0.24*t+490
        #print("5-6")
        return 0, G, B
    elif 250*5 <= t and t< 250*6:
        R = 0.58*t-725
        G = -0.4*t+600
        B = -0.24*t+490
        #print("6-7")
        return R, G, B
    elif 250*6 <= t and t< 250*7:
        R = 0.42*t-485
        B = -0.52*t+910
        #print("7-1")
        return R, 0, B

class Mykeyboard(KMKKeyboard):
    #def process_key(self, key, is_pressed, coord_int,coord_row):
        #row = int_coord >> 4
        #col = int_coord & 0x0F
        #if is_pressed == 1:
            #if coord_row != None:
                #print(coord_row)
                #l_num = coord_row[0]*2 + coord_row[1]
                #print(l_num)
                #custom_rgb.start_timer(l_num)
                #asyncio.create_task(on_neopixel(l_num,5))
            
            """ oled.fill_rect(15,5,15,21,0)
            key_name = HID_KEYCODE_MAP.get(key.code, 'Unknown')
            if len(key_name)  == 1:
                oled.text(key_name,15,5,1,size=3)
            oled.show() """

        #super().process_key(key, is_pressed, coord_int, coord_row)

keyboard = Mykeyboard()

keyboard.row_pins = (board.GP22,board.GP16,board.GP17,board.GP18,board.GP19,board.GP26,board.GP27)
keyboard.col_pins = (board.GP14,board.GP13,board.GP12,board.GP11,board.GP10,board.GP9,board.GP8,board.GP7,board.GP6,board.GP5,board.GP4,board.GP3,board.GP2,board.GP1,board.GP0)



keyboard.diode_orientation = DiodeOrientation.ROWS
keyboard.debug_enabled = 0

keyboard.keymap=[
    [KC.A, KC.A, KC.A, KC.A, KC.A, KC.A, KC.W, KC.A, KC.A, KC.A, KC.A, KC.A, KC.A, KC.A, KC.W,
    KC.B, KC.B, KC.B, KC.B, KC.B, KC.B, KC.B, KC.B, KC.B, KC.B, KC.B, KC.B, KC.B, KC.B, KC.Q,
    KC.C, KC.C, KC.C, KC.C, KC.C, KC.C, KC.C, KC.C, KC.C, KC.C, KC.C, KC.C, KC.C, KC.P, KC.P,
    KC.D, KC.D, KC.D, KC.D, KC.D, KC.D, KC.D, KC.D, KC.D, KC.D, KC.D, KC.D, KC.D, KC.O, KC.O,
    KC.E, KC.E, KC.E, KC.E, KC.E, KC.E, KC.E, KC.E, KC.E, KC.E, KC.E, KC.E, KC.L, KC.E, KC.L,
    KC.F, KC.F, KC.F, KC.F, KC.F, KC.F, KC.F, KC.F, KC.F, KC.F, KC.F, KC.F, KC.F, KC.M, KC.M,
    KC.G, KC.G, KC.G, KC.G, KC.G, KC.G, KC.G, KC.G, KC.G, KC.S, KC.G, KC.G, KC.G, KC.G, KC.S,
    KC.G, KC.G, KC.G, KC.G, KC.G, KC.G, KC.G, KC.G, KC.G, KC.S, KC.G, KC.G, KC.G, KC.G, KC.S]
]

for k in range(num_pixels):
    pixels[k] = (20,20,20)

if __name__ == '__main__':
    keyboard.go()


n_row1 = 15
n_row2 = 14
n_row3 = 14
n_row4 = 13
n_row5 = 14
n_row6 = 10
while True:
    #time.sleep(1)
    #print(t)
    for k in range(n_row1):
        R,G,B = rainbow(50*0+t+50*k)
        pixels[k] = (R,G,B)
    for k in range(n_row2):
        R,G,B = rainbow(50*1+t+50*k)
        k += n_row1
        pixels[k] = (R,G,B)
    for k in range(n_row3):
        R,G,B = rainbow(50*2+t+50*k)
        k += (n_row1 + n_row2)
        pixels[k] = (R,G,B) 
    for k in range(n_row4):
        R,G,B = rainbow(50*3+t+50*k)
        k += (n_row1 + n_row2 + n_row3)
        pixels[k] = (R,G,B)
    for k in range(n_row5):
        R,G,B = rainbow(50*4+t+50*k)
        k += (n_row1 + n_row2 + n_row3 + n_row4)
        pixels[k] = (R,G,B)
    for k in range(n_row6):
        R,G,B = rainbow(50*5+t+50*k)
        #print(k)
        k += (n_row1 + n_row2 + n_row3 + n_row4 + n_row5)
        #print(k)
        pixels[k] = (R,G,B)
    time.sleep(0.01)
    
    t += 50
    #print("R:",R,"G:",G,"B:",B,"t:",t)
    #time.sleep(1)
