# Imports go at the top
from microbit import *
a = 0
flag = 0
kakudo = [107,104,100, 97, 93,
           90, 86, 83, 77, 72,
           68, 63, 59, 54, 50,
           54, 59, 63, 68, 72,
           77, 83, 86, 90, 93,
           97,100,104]
pin0.write_analog(40)
# Code in a 'while True:' loop repeats forever
def sabo():
    display.scroll(kakudo[a])
    pin0.write_analog(kakudo[a])

while True:
    if pin_logo.is_touched():
        if flag == 0:
            sabo()
            sleep(1000)
            flag = 1
        elif flag == 1:
            pin0.write_analog(40)
            sleep(1000)
            flag = 0
    if button_a.is_pressed():
        a -= 1
        if a < 0:
            a = 0
        display.scroll(a)
    if button_b.is_pressed():
        a += 1
        if a > 28:
            a = 28
        display.scroll(a)