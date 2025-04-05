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
from kmk.extensions.media_keys import MediaKeys
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

import board
pixel_pin = board.GP15
#num_pixels = 80  # 使用するNeoPixelの数
#pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=True)
#i = 0

#import board
num_pixels = 10
#pixels = neopixel.NeoPixel(board.GP15, num_pixels, brightness=0.1)

# シンプルなアニメーション関数（例としてカラーシフト）
def color_shift():
    for i in range(num_pixels):
        pixels[i] = (i * 25 % 255, 0, 255 - i * 25 % 255)
    pixels.show()

# KMKのループ内でアニメーションを追加
def custom_animation():
    while True:
        color_shift()
        time.sleep(0.1)  # アニメーションの速度調整
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
        self.led_timer3 = [None] * self.num_leds1F
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

keyboard.extensions.append(MediaKeys())

keyboard.diode_orientation = DiodeOrientation.ROWS
keyboard.debug_enabled = 0
#rgb = RGB(pixel_pin,80)
#keyboard.extensions.append(rgb)
rgb = RGB(board.GP15,80)
keyboard.extensions.append(rgb)


keyboard.keymap=[
    [KC.MUTE, KC.VOLD, KC.VOLU, KC.RGB_MODE_RAINBOW, KC.RGB_MODE_BREATHE_RAINBOW, KC.RGB_MODE_BREATHE, KC.RGB_MODE_KNIGHT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.KP_ASTERISK, KC.DEL,
    KC.ZKHK, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.NO,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.NO,
    KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENTER, KC.NO, KC.NO,
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLASH, KC.RCTL, KC.UP, KC.RALT, KC.NO,
    KC.LCTL, KC.LALT, KC.LWIN, KC.F12, KC.SPC, KC.LGUI(KC.V), KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO]
]

#for k in range(num_pixels):
#    pixels[k] = (10,15,10)

if __name__ == '__main__':
    #keyboard.go()
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
