import threading
import keyboard
from pynput.mouse import Controller
from time import sleep


def blockinput():
    global block_input_flag
    block_input_flag = 1
    t1 = threading.Thread(target=blockinput_start)
    t1.start()



def unblockinput():
    blockinput_stop()


def blockinput_start():
    mouse = Controller()
    global block_input_flag
    for i in range(150):
        keyboard.block_key(i)
    while block_input_flag == 1:
        mouse.position = (0, 0)

def blockinput_stop():
    global block_input_flag
    for i in range(150):
        keyboard.unblock_key(i)
    block_input_flag = 0

