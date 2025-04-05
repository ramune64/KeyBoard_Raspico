import board
import digitalio

# GPIO27ピンを出力として設定
pin27 = digitalio.DigitalInOut(board.GP27)
pin27.direction = digitalio.Direction.OUTPUT

# ピンをHighに設定して電圧を測定
pin27.value = True
print("High Output Test: ", pin27.value)  # True (3.3V) が返るべき

# ピンをLowに設定して電圧を測定
pin27.value = False
print("Low Output Test: ", pin27.value)  # False (0V) が返るべき
