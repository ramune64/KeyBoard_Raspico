""" import time
from board import *
import digitalio

led = digitalio.DigitalInOut(GP25)
led.direction = digitalio.Direction.OUTPUT
while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
    print("hellow world!!") """
import asyncio

import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules import Module
import adafruit_ssd1306
import busio
from kmk.handlers.sequences import simple_key_sequence
import neopixel
import digitalio
import time
from kmk.extensions.rgb import RGB
from kmk.extensions import Extension
num_leds = 10
""" pixels = neopixel.NeoPixel(board.GP28,num_leds,auto_write=False)
for i in range(num_leds):
    pixels[i] = (0,10,10)
pixels.show() """
#led_ext = RGB(board.GP28, 10)

class CustomRGB(Extension):
    def __init__(self, pin=board.GP28, num_leds=10, led_delay=5,row_nums=[2,2]):
        self.led = neopixel.NeoPixel(pin, num_leds)
        for i in range(num_leds):
            self.led[i] = (0,10,10)

        self.num_leds = num_leds
        self.led_delay = led_delay
        self.row_nums = row_nums
        self.num_leds1 = 0
        for i in self.row_nums:
            self.num_leds1 += i
        self.led_timer1 = [None] * self.num_leds1
        self.led_timer2 = [None] * self.num_leds1
        self.led_timer3 = [None] * self.num_leds1
        self.led_timer4 = [None] * self.num_leds1
        self.led_timer5 = [None] * self.num_leds1
        self.led_timerdel1 = [None] * self.num_leds1
        self.led_timerdel2 = [None] * self.num_leds1
        self.led_timerdel3 = [None] * self.num_leds1
        self.led_timerdel4 = [None] * self.num_leds1
        self.led_timerdel5 = [None] * self.num_leds1
        self.led_index = 0

    def set_led(self, index, color):
        self.led[index] = color
        self.led.show()

    def start_timer(self,keyindex):
        print("start_timer")
        self.led_timer1[keyindex] = time.monotonic() + self.led_delay
        self.led_timerdel1[keyindex] = time.monotonic() + self.led_delay + 1
        print(time.monotonic())
        print(self.led_timer1)

    def after_matrix_scan(self, keyboard):
        # タイマーが設定されていて、現在の時間がタイマーを超えた場合
        #print("Process method called")


        for nums in range(self.num_leds1):
            if self.led_timer1[nums] and time.monotonic() >= self.led_timer1[nums]:
                print("turn_on")
                self.set_led(nums, (20, 0, 0))  # LEDを赤色に点灯
                self.led_timer1[nums] = None  # タイマーをリセット
            if self.led_timerdel1[nums] and time.monotonic() >= self.led_timerdel1[nums]:
                print("turn_off")
                self.set_led(nums, (0, 20, 20))  # LEDを赤色に点灯
                self.led_timerdel1[nums] = None  # タイマーをリセット



#pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
#pixels[0] = (10, 0, 0)
#pixels[9] = (0, 10, 0)
#pixels.show()


#WOW = send_string("Wow, KMK is awesome!")
#from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.GP21,board.GP20)
oled = adafruit_ssd1306.SSD1306_I2C(128,64,i2c)
oled.fill(0)

oled.show()
oled.rect(10,0,118,64,1)
oled.show()
#oled.text("EN",15,5,1,size=3)
#oled.show()
HID_KEYCODE_MAP = {
    0x04: 'A', 0x05: 'B', 0x06: 'C', 0x07: 'D', 0x08: 'E',
    0x09: 'F', 0x0A: 'G', 0x0B: 'H', 0x0C: 'I', 0x0D: 'J',
    0x0E: 'K', 0x0F: 'L', 0x10: 'M', 0x11: 'N', 0x12: 'O',
    0x13: 'P', 0x14: 'Q', 0x15: 'R', 0x16: 'S', 0x17: 'T',
    0x18: 'U', 0x19: 'V', 0x1A: 'W', 0x1B: 'X', 0x1C: 'Y',
    0x1D: 'Z', 0x1E: '1', 0x1F: '2', 0x20: '3', 0x21: '4',
    0x22: '5', 0x23: '6', 0x24: '7', 0x25: '8', 0x26: '9',
    0x27: '0', 0x28: 'Enter', 0x29: 'Esc', 0x2A: 'Backspace',
    0x2B: 'Tab', 0x2C: 'Space', 0x2D: '-', 0x2E: '=', 0x2F: '[',
    0x30: ']', 0x31: '\\', 0x32: '#', 0x33: ';', 0x34: "'",
    0x35: '`', 0x36: ',', 0x37: '.', 0x38: '/', 0x39: 'CapsLock',
    # 他のキーコードも必要に応じて追加
}


""" async def on_neopixel(num,times):
    pixels[num] = (10,0,0)
    pixels.show()
    await asyncio.sleep(times)
    pixels[num+4] = (10,0,0)
    pixels.show() """

class Mykeyboard(KMKKeyboard):
    def process_key(self, key, is_pressed, coord_int,coord_row):
        #row = int_coord >> 4
        #col = int_coord & 0x0F
        if is_pressed == 1:
            if coord_row != None:
                print(coord_row)
                l_num = coord_row[0]*2 + coord_row[1]
                print(l_num)
                custom_rgb.start_timer(l_num)
                #asyncio.create_task(on_neopixel(l_num,5))
            
            oled.fill_rect(15,5,15,21,0)
            key_name = HID_KEYCODE_MAP.get(key.code, 'Unknown')
            if len(key_name)  == 1:
                oled.text(key_name,15,5,1,size=3)
            oled.show()

        super().process_key(key, is_pressed, coord_int, coord_row)



keyboard = Mykeyboard()
custom_rgb = CustomRGB(pin=board.GP28, num_leds=10, led_delay=1,row_nums=(2,2))
aaa = Exception()
#custom_keycode_module = CustomKeycodeModule()
#keyboard.modules.append(custom_keycode_module)


keyboard.row_pins = (board.GP0,board.GP1)
keyboard.col_pins = (board.GP15,board.GP14)

keyboard.diode_orientation = DiodeOrientation.ROWS
keyboard.debug_enabled = 0
#keyboard.modules.append(mykey.process_key(keyboard=keyboard))
WOW = simple_key_sequence(( KC.LSHIFT(KC.N), KC.I, KC.C, KC.E,))
keyboard.keymap=[
   [KC.A, KC.B,
    KC.C, WOW]
]

keyboard.extensions.append(custom_rgb)
import time
from board import *
import digitalio

led = digitalio.DigitalInOut(GP25)
led.direction = digitalio.Direction.OUTPUT

if __name__ == '__main__':
    #keyboard.go()
    while True:
        led.value = True
        time.sleep(1)
        led.value = False
        time.sleep(1)
        print("led")
    exit()
    

""" # 列ピンの定義
keyboard.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
# 行ピンの定義
keyboard.row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12) """